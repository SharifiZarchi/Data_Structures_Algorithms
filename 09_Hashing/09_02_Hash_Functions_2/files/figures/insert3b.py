import _dictdraw, sys

d = {'ali': 6, 'reza': 9, 'nasim': 8}
surface = _dictdraw.draw_dictionary(d, [5])
surface.write_to_png(sys.argv[1])
