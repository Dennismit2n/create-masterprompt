# Werkzeugkette für die Übersichtstafeln von create-masterprompt

Liegt im Repo unter `tools/uebersicht/`, per `export-ignore` aber nicht im
Release-Zip. Die Tafeln tragen seit dem 22.09.2026 keinen Versionsstempel mehr;
neu gebaut werden sie nur, wenn sich ihr Inhalt ändert — die Texte in
`strings-<code>.json` oder der Aufbau in `vorlage.html`.

Reihenfolge, ausgeführt in diesem Ordner:

    python bau-tafeln.py                      # strings-<code>.json + vorlage.html -> index-<code>.html
    node schiessen-alle.cjs                   # -> uebersicht-<code>.png (braucht Playwright, siehe unten)
    python quantisiere.py                     # 64 Farben, ~85 KB je Bild
    cp uebersicht-??.png ../../docs/
    python pruefe-skills.py ../.. <version>   # Strukturprüfung aller SKILL.<code>.md gegen SKILL.md

Alle Skripte nehmen optional Sprachcodes als Argumente (`python bau-tafeln.py ja ko`).
`index-<code>.html` und `uebersicht-<code>.png` in diesem Ordner sind Zwischenstände
und stehen in `.gitignore`; die fertigen Bilder liegen in `docs/`.

Playwright: `schiessen-alle.cjs` lädt es aus `PLAYWRIGHT_PATH` (Pfad zu einem
`node_modules/playwright`) oder, ohne die Variable, per gewöhnlichem
`require('playwright')`. PowerShell:

    $env:PLAYWRIGHT_PATH = 'C:/pfad/zu/node_modules/playwright'; node schiessen-alle.cjs

`quantisiere.py` braucht Pillow (`pip install pillow`).

Die `strings-<code>.json` sind die Quelle der Bildtexte in allen vierzehn Sprachen —
nicht neu übersetzen lassen, hier ändern. `vorlage.html` setzt `<html lang>`; ohne
das wählt Chromium für Chinesisch und Japanisch falsche Glyphenvarianten.
`pruefnotizen.md` hält fest, was die Gegenprüferinnen am 15.09.2026 je Sprache
repariert haben.
