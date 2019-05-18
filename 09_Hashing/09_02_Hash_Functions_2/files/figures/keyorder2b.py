import _dictdraw, sys

d = {'john': 858, 'snow': 1, 'arya':666, 'dead':3, 'alive': 2}
surface = _dictdraw.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
