#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from math import ceil, pi
import cairo, sys
import _dictinfo

cr = None

from contextlib import contextmanager

def bits(n):
    sign = '1' if n < 0 else '0'
    m = n if n >= 0 else (n + 2**31)
    s = '%31s' % bin(m)[2:][-31:]
    return sign + s.replace(' ', '0')

def myrepr(obj):
    if isinstance(obj, unicode):
        return u"'%s'" % (obj,)
    return repr(obj)

@contextmanager
def save(cr):
    cr.save()
    p = cr.get_current_point()
    yield
    cr.restore()
    cr.move_to(*p)

pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba(1, 0.7, 0, 0, 1) # First stop, 100% opacity
pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1) # Last stop, 100% opacity

def center_text(cr, x, y, text):
    tx, ty, twidth, theight = cr.text_extents(text)[:4]
    cr.move_to(x - tx - twidth / 2, y - ty - theight / 2)
    cr.show_text(text)
    cr.fill()

def draw_textbox(texts, rectcolor):
    global cr

    with save(cr):
        colors = [ a for i, a in enumerate(texts) if i%2 == 0 ]
        texts = [ a for i, a in enumerate(texts) if i%2 == 1 ]

        x, y = cr.get_current_point()
        cr.translate(x, y)

        extents = cr.text_extents('M' * len(''.join(texts)))
        ty = ceil(extents[1])
        twidth = ceil(extents[2])
        theight = ceil(extents[3])

        padding = ceil(theight / 3)

        width = twidth + 2 * padding
        height = theight + 2 * padding
        cr.rectangle(0,0, width,height)
        cr.set_source_rgb(*rectcolor)
        cr.fill()

        cr.move_to(padding, padding + -ceil(ty))
        for i in range(len(colors)):
            cr.set_source_rgb(*colors[i])
            if texts[i] == '/':  # special code for not-equals
                with save(cr):   # so the '/' will display atop the '='
                    cr.show_text('=')
            cr.show_text(texts[i])

    cr.rel_move_to(width, 0)
    return height

def draw_arrowhead(x, y):
    with save(cr):
        cr.translate(x, y)
        cr.move_to(0, -10)
        cr.line_to(20, 0)
        cr.line_to(0, 10)
        cr.fill()

#

black = (0, 0, 0)
white = (1, 1, 1)
red = (0.7, 0, 0)
green = (0, 0.7, 0)
gold = (1, 0.9, 0.5)
gray = (0.5, 0.5, 0.5)
lightgray = (0.8, 0.8, 0.8)

def draw_button(cr, x, y, is_collision=True):
    """Draw a green or red circle showing a hit or a collision."""
    with save(cr):
        cr.translate(x, y)

        if is_collision:
            cr.set_source_rgb(*red)
        else:
            cr.set_source_rgb(*green)

        cr.set_font_size(32)
        cr.arc(0, 0, 13.5, 0, pi * 2)  # red or green circle
        cr.fill()

        if is_collision:
            cr.set_source_rgb(*white)
            center_text(cr, 0.8, -1, '×')

def draw_dictionary(d, lookup_paths = None, show_dummy=False):
    """Supply `d` a Python dictionary."""
    global cr

    o = _dictinfo.dictobject(d)

    WIDTH=960
    if len(o) == 8:
        HEIGHT=406
    else:
        HEIGHT=480


    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    cr = cairo.Context(surface)

    cr.select_font_face('Inconsolata',
                        cairo.FONT_SLANT_NORMAL,
                        cairo.FONT_WEIGHT_BOLD)

    cr.rectangle(0,0, WIDTH,HEIGHT)
    cr.set_source_rgb(1,1,1)
    cr.fill()

    with save(cr):

        mask = o.ma_mask
        sigbits = 0
        while mask:
            sigbits += 1
            mask >>= 1

        if len(o) == 8:
            xoffset = 140
            hashwidth = 9 # width of the hash field
            font_size = 40
            gap = 2
            show_value = True
        else:
            if len(o) == 32:
                xoffset = 360
                hashwidth = 16 # width of the hash field
                show_value = True
                font_size = 12
            else:
                xoffset = 140
                hashwidth = sigbits + 1 # width of the hash field
                show_value = False
                font_size = 10

            gap = 0

        yoffset = font_size # room for header at top

        cr.set_font_size(font_size)
        charwidth = cr.text_extents(u'M')[2]
        width = 100 #actually compute from font size later

        cr.translate(xoffset, yoffset)  # upper-left corner of the dictionary

        with save(cr):
            cr.set_source_rgb(0,0,0)
            cr.translate(2,-6)
            if len(o) == 8:
                cr.show_text(u'Idx      Hash     Key   Value')

        height = 0

        for i in range(len(o)):
            if i == 0 or i % 32:
                cr.rel_move_to(0, height + gap)
            else:
                cr.rel_move_to(176, -31 * height + -30 * gap)

            with save(cr):
                entry = o.ma_table[i]

                height = draw_textbox([gold, bits(i)[-sigbits:]], gray)
                cr.rel_move_to(gap, 0)

                try:
                    k = entry.me_key
                except ValueError:
                    # This is a completely empty entry.
                    draw_textbox([white, u' '], lightgray)
                    cr.rel_move_to(gap, 0)
                    draw_textbox([white, u' ' * hashwidth], lightgray)
                    cr.rel_move_to(gap, 0)
                    draw_textbox([white, u' ' * 7], lightgray)
                    if show_value:
                        cr.rel_move_to(gap, 0)
                        draw_textbox([white, u' ' * 6], lightgray)
                    continue

                if k is _dictinfo.dummy:
                    if not show_dummy:
                        draw_textbox([white, u'!'], red)
                        cr.rel_move_to(gap, 0)
                        draw_textbox([white, u' ' * hashwidth], gray)
                        cr.rel_move_to(gap, 0)
                        draw_textbox([white, u'<dummy>'], gray)
                        if show_value:
                            cr.rel_move_to(gap, 0)
                            draw_textbox([white, u' ' * 6], gray)
                    else:
                        draw_textbox([white, u' '], black)
                        cr.rel_move_to(gap, 0)
                        draw_textbox([white, u' ' * hashwidth], black)
                        cr.rel_move_to(gap, 0)
                        draw_textbox([white, u' ' * 7], black)
                        if show_value:
                            cr.rel_move_to(gap, 0)
                            draw_textbox([white, u' ' * 6], black)
                    continue

                h = entry.me_hash
                v = entry.me_value

                if h & o.ma_mask == i:
                    draw_textbox([white, u'='], green)
                else:
                    draw_textbox([white, u'/'], red)
                cr.rel_move_to(gap, 0)
                bstr = bits(h)[-hashwidth+1:]
                texts = [lightgray, u'…' + bstr[:-sigbits],
                         gold, bstr[-sigbits:]]
                draw_textbox(texts, gray)
                cr.rel_move_to(gap, 0)
                draw_textbox([white, u'%-7s' % myrepr(k)], gray)
                if show_value:
                    cr.rel_move_to(gap, 0)
                    draw_textbox([white, u'%-6s' % myrepr(v)], gray)

    if lookup_paths is None:
        lookup_paths = ()
    else:
        lookup_paths = (lookup_paths, )
    for lookup_path in lookup_paths:
        with save(cr):
            n = lookup_path[0]
            cr.translate(xoffset, yoffset)

            y = 2 + n * (height + gap + 0.5) + height / 2
            cr.set_source_rgb(*black)
            cr.set_line_width(6)
            cr.move_to(-100, y)
            cr.rel_line_to(40, 0)
            cr.stroke()
            draw_arrowhead(-60, y)

            draw_button(cr, -20, y, len(lookup_path) > 1)

            if len(lookup_path) > 1:
                cr.move_to(650, y)
                cr.rel_line_to(40, 0)
                cr.stroke()

            for i in range(1, len(lookup_path)):
                from_slot = lookup_path[i - 1]
                dest_slot = lookup_path[i]
                
                yf = 2 + from_slot * (height + gap + 0.5) + height / 2
                yd = 2 + dest_slot * (height + gap + 0.5) + height / 2
                y0 = min(yf, yd)
                y1 = max(yf, yd)

                cr.set_source_rgb(*black)
                cr.set_line_width(6)
                cr.move_to(690, y0)
                cr.arc(690, (y0 + y1) / 2, (y1 - y0) / 2, 3 * pi / 2, pi / 2)
                cr.stroke()

                draw_button(cr, 652, yd, i + 1 < len(lookup_path))

                with save(cr):
                    cr.translate(690, yd)
                    cr.rotate(pi)
                    draw_arrowhead(0, 0)

    return surface
#

if __name__ == '__main__':
    d = {'ftp': 21}
    surface = draw_dictionary(d, [1])
    # surface.write_to_png(sys.argv[1])
