import _dictdraw, sys

d = {'arya': 666, 'john': 858}
surface = _dictdraw.draw_dictionary(d, [3, 1])
surface.write_to_png(sys.argv[1])
