import _dictdraw, sys

d = {3: 1, 3+8: 2, 3+16: 3, 3+24: 4, 3+32: 5}
surface = _dictdraw.draw_dictionary(d, [3, 1, 6, 7])
surface.write_to_png(sys.argv[1])
