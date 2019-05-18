import _dictdraw, sys

d = {'smtp': 21, 'svn': 3690, 'dict': 2628, 'ircd': 6667, 'zope': 9673,
     'fido': 60179}
surface = _dictdraw.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
