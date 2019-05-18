import _dictdraw, sys

d = {'ali': 6, 'reza': 9}
surface = _dictdraw.draw_dictionary(d, [4])
surface.write_to_png(sys.argv[1])
