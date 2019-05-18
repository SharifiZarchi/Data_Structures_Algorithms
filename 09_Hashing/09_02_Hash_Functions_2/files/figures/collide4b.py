import _dictdraw, sys

d = {'arya': 666, 'john': 858, 'snow':1, 'alive': 2}
surface = _dictdraw.draw_dictionary(d, [6])
surface.write_to_png(sys.argv[1])
