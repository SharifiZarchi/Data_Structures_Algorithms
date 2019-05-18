import _dictdraw, sys

d = {'ali': 9}
surface = _dictdraw.draw_dictionary(d, [7])
surface.write_to_png(sys.argv[1])
