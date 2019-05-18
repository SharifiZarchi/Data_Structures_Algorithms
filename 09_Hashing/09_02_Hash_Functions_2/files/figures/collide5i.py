import _dictdraw, sys

d = {'arya': 666, 'john': 858, 'snow':1, 'alive': 2, 'dead':3}
del d["snow"], d['john'], d['arya'], d['alive']
surface = _dictdraw.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
