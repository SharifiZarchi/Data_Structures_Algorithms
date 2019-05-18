"""Routines that examine the internals of a CPython dictionary."""

from ctypes import Structure, c_ulong, POINTER, cast, py_object
from math import log

UMAX = 2 ** 32

def cbin(n):
    """Return `n` as a clean 32-bit binary number, without a leading '0b'."""
    if n < 0:
        n = UMAX + n
    return '{0:0>32}'.format(bin(n)[2:])

# Create a singleton with which the dictionary routines below can
# represent null C pointers.

class NULL(object):
    def __repr__(self):
        return 'NULL'

NULL = NULL()

# Create Structures representing the dictionary object and entries, and
# give them useful methods making them easier to use.

class PyDictEntry(Structure):
    """An entry in a dictionary."""
    _fields_ = [
        ('me_hash', c_ulong),
        ('me_key', py_object),
        ('me_value', py_object),
        ]

class PyDictObject(Structure):
    """A dictionary object."""
    _fields_ = [
        ('ob_refcnt', c_ulong),
        ('ob_type', c_ulong),
        ('ma_fill', c_ulong),
        ('ma_used', c_ulong),
        ('ma_mask', c_ulong),
        ('ma_table', POINTER(PyDictEntry)),
        ]

    def __len__(self):
        """Return the number of dictionary entry slots."""
        return self.ma_mask + 1

    def slot_of(self, key):
        """Find and return the slot at which `key` is stored."""
        for i in range(len(self)):
            try:
                k = self.ma_table[i].me_key
            except ValueError:
                continue  # me_key is NULL
            if (k is key) or (k == key):
                return i
        raise KeyError('cannot find key %r' % (key,))

    def slot_map(self):
        """Return a mapping of keys to their integer slot numbers."""
        m = {}
        for i in range(len(self)):
            entry = self.ma_table[i]
            try:
                entry.me_value
            except:
                continue  # me_value is NULL
            m[entry.me_key] = i
        return m

def dictobject(d):
    """Return the PyDictObject lying behind the Python dict `d`."""
    if not isinstance(d, dict):
        raise TypeError('cannot create a dictobject from %r' % (d,))
    return cast(id(d), POINTER(PyDictObject)).contents

# Retrieve the secret dummy object (it is a simple string, in current
# versions of Python) used internally by dictionaries to represent a
# previously occupied slot.

dummy = None
d = {0: 0}
del d[0]
dummy = dictobject(d).ma_table[0].me_key
del d

#

def _probe_steps(dummydict, key, final_slot):
    """Find the slots searched to put `key` in `final_slot` of `dummydict`.

    The `dummydict` should be a dictionary in which `key` once resided
    in position `final_slot`, but whose entries have all been deleted,
    leaving dummy entries.  This routine will repeatedly try to insert
    `key` into the dictionary, and each time that it does not land at
    `final_slot` an obstacle is placed where it has landed instead,
    until finally the obstacles make `key` land in the `final_slot`.

    A list of the slots searched is returned.  The last element of this
    list will always be `final_slot`.

    """
    o = dictobject(dummydict)

    # Compute the first slot rather than do an expensive search.
    slot = hash(key) & o.ma_mask
    slots = [ int(slot) ]   # since slot often arrives as a long

    # Keep adding obstacles until `key` winds up in `final_slot`.
    while slots[-1] != final_slot:
        if slot == key:  # make sure the integer `slot` is not `key` itself
            slot += len(o)
        dummydict[slot] = None  # add the obstacle

        dummydict[key] = None  # add the key
        slot = o.slot_of(key)
        slots.append(slot)
        del dummydict[key]

    # Return the sequence of slots that we searched.
    return slots


def probe_steps(keys, key):
    """Return the search sequence for `key` for a dict built with `keys`.

    `keys` - Dictionary keys, in order of their insertion, including `key`.
    `key` - The key whose collision path we want to explore.
    """
    # Create a dictionary with the given `keys` and figure out at which
    # slot the target `key` wound up.
    d = dict.fromkeys(keys)
    o = dictobject(d)
    final_slot = o.slot_of(key)

    # Empty the dictionary so that it contains only dummy entries, then
    # pass it to the internal _probe_steps() routine.
    for k in list(d):
        del d[k]
    return _probe_steps(d, key, final_slot)

def probe_all_steps(keys):
    """Return the search sequence for each key in a dict built with `keys`.

    `keys` - Dictionary keys, in order of their insertion, including `key`.

    The return value looks like ``{key: [slot, slot, slot], ...}``.

    """
    # Create a dictionary with the given `keys` and find out in which
    # slot each key wound up.
    d = dict.fromkeys(keys)
    o = dictobject(d)
    m = o.slot_map()

    # For each key in the dictionary, find its probe list.
    for key, final_slot in m.items():
        for k in list(d):
            del d[k]  # empty the dictionary
        m[key] = _probe_steps(d, key, final_slot)
    return m

def display_dictionary(d):
    """Print a dictionary hash table to the screen."""
    do = dictobject(d)
    bits = int(log(do.ma_mask + 1, 2))
    for i in range(len(do)):
        entry = do.ma_table[i]
        entry_bits = cbin(i)[-bits:]
        try:
            key = entry.me_key
        except ValueError:  # me_key is NULL
            print '   ' + entry_bits, 'empty'
            continue

        hash_bits = cbin(entry.me_hash)[-bits:]
        if hash_bits == entry_bits:
            print '...' + entry_bits,
        else:
            print '***' + hash_bits,
        print '[%r] =' % (entry.me_key),
        if entry.me_value:
            print '%r' % entry.me_value
        else:
            print

if __name__ == '__main__':

    # Two tiny tests.
    steps = probe_steps([2, 3, 10, 18, 1], 10)
    assert steps == [2, 5]

    stepmap = probe_all_steps([2, 3, 10, 18, 1])
    assert stepmap == {1: [1], 2: [2], 3: [3], 10: [2, 5], 18: [2, 5, 3, 0]}
