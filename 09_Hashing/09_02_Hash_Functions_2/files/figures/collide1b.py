import _dictdraw, sys

d = {'arya': 666}
surface = _dictdraw.draw_dictionary(d, [3])
surface.write_to_png(sys.argv[1])
