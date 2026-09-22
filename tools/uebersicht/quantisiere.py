# -*- coding: utf-8 -*-
"""Palette statt Vollton fuer alle uebersicht-<code>.png im Ordner — dieselbe
Methode wie bei den ersten beiden Tafeln (64 Farben, kein Dithering: das Blatt
ist flaechig, Dithering wuerde nur Rauschen und Bytes erzeugen).
Aufruf: python quantisiere.py [code ...]"""
import glob, os, re, sys
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
codes = sys.argv[1:] or sorted(
    re.search(r'uebersicht-([a-z]{2})\.png$', p).group(1)
    for p in glob.glob(os.path.join(HIER, 'uebersicht-*.png')))
for code in codes:
    p = os.path.join(HIER, 'uebersicht-%s.png' % code)
    roh = os.path.getsize(p)
    im = Image.open(p).convert('RGB')
    q = im.quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE)
    q.save(p, optimize=True)
    print('%s  %4d x %4d  %7d -> %6d Bytes' % (code, im.width, im.height, roh, os.path.getsize(p)))
