# -*- coding: utf-8 -*-
"""Strukturpruefung aller SKILL.<code>.md gegen SKILL.md — unabhaengig von den
Gegenpruef-Agentinnen. Aufruf: python pruefe-skills.py <repo> <version> [code ...]"""
import io, re, sys, glob, os

REPO, VERSION = sys.argv[1], sys.argv[2]
CODES = sys.argv[3:] or sorted(
    re.search(r'SKILL\.([a-z]{2})\.md$', p).group(1)
    for p in glob.glob(os.path.join(REPO, 'SKILL.*.md')))

def lade(p):
    return io.open(p, encoding='utf-8', newline='').read()

def rumpf(t):
    # YAML-Frontmatter abschneiden, falls vorhanden
    if t.startswith('---'):
        e = t.find('\n---', 3)
        return t[e + 4:]
    return t

def abschnitte(t):
    """Liste (H2-Titel, Text) in Dateireihenfolge; Text vor der ersten H2 als ''."""
    teile = re.split(r'^## ', t, flags=re.M)
    out = []
    for s in teile[1:]:
        titel, _, rest = s.partition('\n')
        out.append((titel.strip(), rest))
    return out

def zaehle(txt):
    return {
        'bullets': len(re.findall(r'^\s*- ', txt, re.M)),
        'nummern': len(re.findall(r'^\s*\d+\. ', txt, re.M)),
        'tabelle': len(re.findall(r'^\|(?!-)', txt, re.M)),
        'fett': len(re.findall(r'\*\*', txt)) // 2,
    }

orig = rumpf(lade(os.path.join(REPO, 'SKILL.md')))
orig_abs = abschnitte(orig)
orig_spans = set(re.findall(r'`([^`\n]+)`', orig))
print('Original: %d H2, %d Code-Spans' % (len(orig_abs), len(orig_spans)))
print()

gesamt_fehler = 0
for code in CODES:
    p = os.path.join(REPO, 'SKILL.%s.md' % code)
    t = lade(p)
    probleme = []
    if t.startswith('---'): probleme.append('Frontmatter vorhanden')
    if not t.startswith('# '): probleme.append('beginnt nicht mit H1')
    if '\r' in t: probleme.append('CRLF statt LF')
    kopf = '\n'.join(t.split('\n')[:25])
    if VERSION not in kopf: probleme.append('Version %s fehlt im Kopf' % VERSION)
    for link in ('docs/uebersicht-%s.png' % code, 'docs/uebersicht-en.png'):
        if code != 'en' and link not in kopf: probleme.append('Link fehlt: ' + link)
    abs_ = abschnitte(t)
    if len(abs_) != len(orig_abs):
        probleme.append('H2-Anzahl %d statt %d' % (len(abs_), len(orig_abs)))
    else:
        # Phasen-H2s (Index 1..7) muessen die Ziffern 0..6 in Reihenfolge tragen
        for i, z in zip(range(1, 8), '0123456'):
            if z not in abs_[i][0]:
                probleme.append('H2 #%d ohne Ziffer %s: %r' % (i + 1, z, abs_[i][0][:40]))
        for i, ((ot, otxt), (tt, ttxt)) in enumerate(zip(orig_abs, abs_)):
            zo, zt = zaehle(otxt), zaehle(ttxt)
            for k in ('bullets', 'nummern', 'tabelle'):
                if zo[k] != zt[k]:
                    probleme.append('H2 #%d (%s): %s %d statt %d' % (i + 1, ot[:22], k, zt[k], zo[k]))
    spans = set(re.findall(r'`([^`\n]+)`', t))
    fehlend = sorted(orig_spans - spans)
    if fehlend: probleme.append('Code-Spans fehlen/veraendert: ' + ', '.join(fehlend[:8]) + (' …' if len(fehlend) > 8 else ''))
    zeilen = t.count('\n')
    if probleme:
        gesamt_fehler += 1
        print('%s  FEHLER  (%d Zeilen)' % (code, zeilen))
        for x in probleme: print('    - ' + x)
    else:
        print('%s  ok      (%d Zeilen, %d H2, %d Spans)' % (code, zeilen, len(abs_), len(spans)))
print()
print('---', len(CODES), 'Dateien,', gesamt_fehler, 'mit Fehlern')
sys.exit(1 if gesamt_fehler else 0)
