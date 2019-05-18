import _dictdraw, sys

d = {'nasim': 8, 'reza': 9, 'ali': 6}
surface = _dictdraw.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
