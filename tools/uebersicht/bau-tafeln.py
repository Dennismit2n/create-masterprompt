# -*- coding: utf-8 -*-
"""Baut aus vorlage.html + strings-<code>.json je Sprache eine index-<code>.html.
Prueft dabei die Laengenbudgets der Texte selbst nach — unabhaengig von den
Agentinnen. Aufruf: python bau-tafeln.py [code ...]"""
import io, json, re, sys, glob, os, html

HIER = os.path.dirname(os.path.abspath(__file__))
CODES = sys.argv[1:] or sorted(
    re.search(r'strings-([a-z]{2})\.json$', p).group(1)
    for p in glob.glob(os.path.join(HIER, 'strings-*.json')))

KEYS = ['unter', 'band_kind', 'band_lang', 'lead',
        'h_produce', 'f1_desc', 'f1_lives', 'f2_desc', 'f2_lives', 'f3_desc', 'f3_lives',
        'h_runs', 'gate_title', 'gate_text',
        'p1_name', 'p1_desc', 'p2_name', 'p2_desc', 'p3_name', 'p3_desc',
        'p4_name', 'p4_desc', 'p5_name', 'p5_desc', 'p6_name', 'p6_desc',
        'h_install', 'code_comment', 'hint_claudeai', 'hint_then', 'footer']

BUDGET = {'unter': 60, 'band_kind': 30, 'band_lang': 30, 'lead': 420,
          'h_produce': 28, 'h_runs': 28, 'h_install': 28,
          'f1_desc': 110, 'f2_desc': 110, 'f3_desc': 110,
          'f1_lives': 34, 'f2_lives': 34, 'f3_lives': 34,
          'gate_title': 30, 'gate_text': 150,
          'code_comment': 50, 'hint_claudeai': 190, 'hint_then': 190, 'footer': 170}
for i in range(1, 7):
    BUDGET['p%d_name' % i] = 26
    BUDGET['p%d_desc' % i] = 80

# **x** -> <strong>/<b>, `x` -> <code>; vorher HTML-escapen, damit & < > in
# Uebersetzungen nichts zerlegen. Ost-asiatische Sprachen brauchen keinen
# Sonderfall — die Markierungen sind sprachneutral.
def markup(s, fett):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<%s>\1</%s>' % (fett, fett), s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s

vorlage = io.open(os.path.join(HIER, 'vorlage.html'), encoding='utf-8').read()
fehler = 0
for code in CODES:
    p = os.path.join(HIER, 'strings-%s.json' % code)
    try:
        d = json.load(io.open(p, encoding='utf-8'))
    except Exception as e:
        print('%s  JSON KAPUTT: %s' % (code, e)); fehler += 1; continue
    fehlend = [k for k in KEYS if k not in d]
    extra = [k for k in d if k not in KEYS]
    zulang = [(k, len(d[k]), BUDGET[k]) for k in KEYS if k in d and k in BUDGET and len(d[k]) > BUDGET[k]]
    kein_stern = [k for k in ('lead', 'hint_claudeai', 'hint_then', 'footer') if k in d and '**' not in d[k]]
    kein_code = [k for k in ('hint_claudeai', 'footer') if k in d and '`' not in d[k]]
    if fehlend or extra or zulang or kein_stern or kein_code:
        fehler += 1
        print('%s  PROBLEME' % code)
        if fehlend: print('    fehlende Schluessel:', fehlend)
        if extra: print('    unbekannte Schluessel:', extra)
        for k, n, b in zulang: print('    zu lang: %s %d > %d' % (k, n, b))
        if kein_stern: print('    ohne **Betonung**:', kein_stern)
        if kein_code: print('    ohne `Code`:', kein_code)
        if fehlend: continue
    out = vorlage
    for k in KEYS:
        fett = 'strong' if k == 'lead' else 'b'
        out = out.replace('{{%s}}' % k, markup(d[k], fett))
    out = out.replace('{{code}}', code)
    rest = re.findall(r'\{\{\w+\}\}', out)
    if rest:
        print('%s  Platzhalter uebrig: %s' % (code, rest)); fehler += 1
    io.open(os.path.join(HIER, 'index-%s.html' % code), 'w', encoding='utf-8', newline='\n').write(out)
    if not (fehlend or extra or zulang or kein_stern or kein_code):
        print('%s  ok  (laengster Text: %s)' % (code, max((len(d[k]), k) for k in KEYS)))
print('---', len(CODES), 'Sprachen,', fehler, 'mit Problemen')
sys.exit(1 if fehler else 0)
