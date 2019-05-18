import _dictdraw, sys

d = {}
surface = _dictdraw.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
