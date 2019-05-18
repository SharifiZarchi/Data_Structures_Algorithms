import _dictdraw, sys

d = {'arya': 666, 'john': 858, 'snow':1, 'alive': 2, 'dead':3}
del d["snow"]
surface = _dictdraw.draw_dictionary(d, [6, 5], True)
surface.write_to_png(sys.argv[1])
