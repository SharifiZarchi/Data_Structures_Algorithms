import _dictdraw, sys

d = {'arya': 666, 'john': 858, 'snow':1}
surface = _dictdraw.draw_dictionary(d, [5])
surface.write_to_png(sys.argv[1])
