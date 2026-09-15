# Create Masterprompt — deutsche Fassung

> Übersetzung von `SKILL.md`. **Gelesen wird vom Programm ausschließlich
> `SKILL.md`**, die englische Datei — diese hier ist zum Nachlesen für Menschen.
> Wenn sich beide widersprechen, gilt die englische. Stand: Version 1.6.1.
>
> Dateinamen, Ordner und Beispielbefehle stehen absichtlich unübersetzt, weil
> sie so auf der Festplatte heißen.
>
> Eine Seite zum Überblicken statt zum Durchlesen: [`docs/uebersicht-de.png`](docs/uebersicht-de.png)
> (englische Fassung: [`docs/uebersicht-en.png`](docs/uebersicht-en.png)).
>
> **Stand: frühe Veröffentlichung.** Der Text ist mehrfach auf innere
> Widerspruchsfreiheit und Spec-Konformität geprüft, aber der Skill selbst lief
> noch nicht an vielen echten, unterschiedlichen Vorhaben. Passt etwas am
> Ablauf, am Größen-Gate oder an einer Vorlage nicht zur eigenen Arbeitsweise,
> ist das ein nützliches Signal — gerne als Issue melden.

Ein Masterprompt ist **keine** Rollenanweisung. „Du bist ein erfahrener
Entwickler, arbeite gründlich“ fügt nichts hinzu, was ein fähiges Modell nicht
ohnehin tut. Ein Masterprompt ist ein **Kontext-Paket**: die dauerhaften
Fakten, Entscheidungen und Grenzen eines Vorhabens, so aufgeschrieben, dass
eine Sitzung ohne jeden Gesprächsverlauf genau dort weitermacht, wo die letzte
aufgehört hat.

Dieser Skill baut dieses Paket in sechs Phasen und gibt drei Dateien zurück.

## Was dabei herauskommt

| Datei | Wozu | Lebt so lange |
|---|---|---|
| `BRIEFING.md` | Der Masterprompt. Kontext, Entscheidungen, Anti-Scope, Fallstricke, aktueller Stand. | Das ganze Vorhaben |
| `DECISIONS.md` | Eine Zeile je geklärter Frage, mit Begründung. Es wird nur angehängt, nie überschrieben. | Das ganze Vorhaben |
| `HANDOFF_vNN.md` | Vor dem Kontextlimit geschrieben. Was eine frische Sitzung *jetzt gerade* braucht. | Eine Sitzung |

Benenne sie in der Sprache des Nutzers. Leg sie neben die Arbeit, nicht in den
Chat.

## Phase 0 — Größen-Gate (zuerst, in zehn Sekunden)

Sechs Phasen auf ein Umbenennungs-Skript loszulassen ist der Weg, auf dem
Leute lernen, den Ablauf ganz zu überspringen. Also vorher einordnen:

- **S — eine Sitzung, umkehrbar, keine Unbekannten.** Direkt arbeiten. Den
  vollen Ablauf nur anbieten, wenn es größer wird.
- **M — ein paar Sitzungen, einige Unbekannte, ein oder zwei echte
  Gabelungen.** Phasen 1–3 und 5, dazu 6, sobald die Arbeit über eine Sitzung
  hinausgeht. Briefing-Datei, aber kurz. Kein eigenes Plandokument.
- **L — über mehrere Sitzungen, echte Architektur, Entscheidungen, die teuer
  zurückzunehmen sind.** Alle sechs Phasen.

Sag in einem Satz, welche Größe du gewählt hast und warum. Wenn der Nutzer
anderer Meinung ist, sagt er es — das kostet eine Nachricht und spart eine
Stunde.

## Phase 1 — Recherche

Herausfinden, was es schon gibt, wo die Lücke ist, was technisch machbar ist
und welche Fallstricke bereits dokumentiert sind. **Recherchiert wird nur
hier.** Recherche mitten im Bauen ist der Weg, auf dem aus einem Bau ein
Kaninchenbau wird.

Ergebnis: ein Bericht mit Vergleichstabelle, einer Empfehlung und Quellen.

**Aufhören, wenn alle drei Punkte zutreffen** — nicht, wenn die Neugier
aufhört:

1. Die Vergleichstabelle hat für die Kandidaten der engeren Auswahl keine
   leeren Zellen mehr.
2. Jede Fallstrick-Zeile hat eine Quelle oder ist als Annahme markiert.
3. Die letzten beiden Suchen haben nichts Neues gebracht. Das ist Sättigung.

Wenn du keine Sättigung erreichst, sag es und benenne, was offen geblieben ist.
Eine ehrliche Lücke schlägt eine selbstbewusste Vermutung, und der Nutzer kann
entscheiden, ob er mehr Zeit hineinsteckt.

## Phase 2 — Briefing

Die Recherche zu `BRIEFING.md` verdichten, mit `assets/template-briefing.md`
als Vorlage.

Der Test für diese Datei: **Gib sie einer frischen Sitzung ohne Verlauf. Kann
die damit arbeiten?** Wenn auch nur eine Rückfrage zu etwas nötig ist, das du
bereits wusstest, ist das Briefing unvollständig. Lies es gegnerisch gegen,
bevor du es zeigst.

Pflichtabschnitte — die ersten beiden sind die, die übersprungen und dann
bereut werden:

- **Anti-Scope.** Ausdrückliche Nicht-Ziele, jedes mit Begründung. „Keine
  Verschlüsselung in v1 — der Tresor liegt nur lokal, und die
  Schlüsselverwaltung würde den Bau verdoppeln.“ Anti-Scope ist die stärkste
  verfügbare Abwehr gegen schleichende Ausweitung, weil daraus für jedes
  „könnten wir nicht einfach …“ eine Entscheidung wird, die wieder aufgemacht
  werden muss, statt einer kostenlosen Zugabe.
- **Annahmen-Register.** Alles, was du ohne Rückfrage entschieden hast. Je eine
  Zeile, markiert, damit es später angreifbar bleibt. Unaufgeschriebene
  Annahmen sind unsichtbar, bis sie teuer werden.
- Kontext, Randbedingungen, bekannte Fallstricke, aktueller Stand.

## Phase 3 — Entscheidungs-Interview

Die offenen Entscheidungen **einzeln** stellen und die Antwort abwarten, bevor
die nächste kommt. Gebündelte Fragen werden überflogen, und eine überflogene
Entscheidung ist eine Vermutung mit der Unterschrift des Nutzers.

Je Frage: 2–4 Optionen, eine klare Empfehlung und die Begründung dafür.
Abhängigkeiten der Reihe nach auflösen — erst den Technologie-Unterbau
entscheiden, dann die Bibliothek, die darauf läuft.

**Schlag selbst nach.** Was sich aus Dateien, Werkzeugen oder dem Netz
herausfinden lässt, findest du heraus. Nur echte Wahlmöglichkeiten gehören dem
Nutzer.

**Vor dem Ende dieser Phase wird nichts gebaut.** Wenn der Nutzer mitten im
Interview „fang einfach an“ sagt: benenne die konkret noch offenen
Entscheidungen, biete an, sie selbst als festgehaltene Annahmen zu treffen, und
mach erst weiter, wenn er gewählt hat. Mit offenen Gabelungen anzufangen heißt
Nacharbeit, und Nacharbeit kostet mehr als das Interview.

Zum Schluss eine nummerierte Zusammenfassung aller Entscheidungen. An das
Entscheidungslog anhängen, das `assets/template-decisions.md` folgt.

## Phase 4 — Plan

Architektur, Repo- oder Ordnerstruktur, Konventionsdatei, Teststrategie,
Meilensteine, je Meilenstein eine Definition of Done und eine für das Vorhaben
als Ganzes.

Meilensteine sind **senkrechte Schnitte**: jeder erzeugt etwas, das der Nutzer
tatsächlich starten, sehen oder benutzen kann. Fünf Meilensteine, die je ein
funktionierendes Stück liefern, schlagen drei, die ein Fundament liefern, das
niemand testen kann.

Den Plan vor dem Bauen zur Abnahme zeigen.

## Phase 5 — Bauen

Gegen ein ausgesprochenes Ziel mit einer **prüfbaren Abbruchbedingung**
arbeiten. „Fertig, wenn `npm test` durchläuft und die App den Tresor-Ordner
öffnet“ ist prüfbar. „Fertig, wenn es gut funktioniert“ ist es nicht.

- Test vor Funktion, wo ein Test sinnvoll ist.
- Kleine Commits, jeder für sich zurücknehmbar.
- Linting als Hook, nicht als Erinnerung.
- Keine Pausen, um Erlaubnis zu fragen. Nachfragen nur an echten
  Entwurfs-Gabelungen.

## Phase 6 — Übergabe

Vor dem Kontextlimit — nicht danach — die Übergabedatei schreiben
(`HANDOFF_vNN.md`, benannt in der Sprache des Nutzers), aus
`assets/template-handoff.md`, und dann eine frische Sitzung starten. Endloses
Zusammenfalten verliert genau die Einzelheiten, die teuer zu erarbeiten waren.

Auslöser: lange werkzeuglastige Strecken, wiederholtes Nachlesen derselben
Dateien, oder der Nutzer fragt ein zweites Mal nach etwas, das schon geklärt
war.

## Verbesserungs-Pass

An jeder Phasengrenze, **bevor** das Ergebnis gezeigt wird, still vom Schreiber
zum Prüfer wechseln. Drei Fragen:

1. **Was fehlt?** Welche Frage müsste eine frische Sitzung stellen, die diese
   Datei nicht beantwortet?
2. **Was ist behauptet statt belegt?** Jede Aussage ohne Quelle oder
   Annahme-Markierung ist ein Kandidat.
3. **Was ist Füllmaterial?** Jeder Satz, der genauso in jedem anderen Vorhaben
   stehen könnte, fliegt raus.

Der Nutzer sieht das überarbeitete Ergebnis, nicht die Kritik. Ausnahme: Wenn
der Pass etwas aufdeckt, das eine Entscheidung berührt, gehört das vor ihn.

Erzeugen und Bewerten sind verschiedene Tätigkeiten. Der Schreiber kann die
Lücke nicht sehen, weil das fehlende Stück in seinem Kopf steht. Kostet
ungefähr 30 % der Phase und bringt mehr als alles andere in diesem Skill.

Wenn die Aufgabenform über „schreib mir X“ hinausgeht, zuerst
`references/prompt-techniques.md` laden — dort steht die Zuordnung von
Aufgabenform zu Technik und die Warnzeichen für Über-Prompting.

## Rückspul-Regel

Entscheidungen werden revidiert. Das ist normal und billig, **wenn man es
richtig macht**:

1. Das Entscheidungslog nachziehen — neue Zeile dazu, alte als überholt
   markieren, beide behalten. Die Historie erklärt, warum der Code aussieht,
   wie er aussieht.
2. `BRIEFING.md` nachziehen, denn das ist es, was eine frische Sitzung liest.
3. Benennen, was die Änderung ungültig macht, bevor Code angefasst wird.

Nur im Chat umzuschwenken ist die Fehlerart: die Dateien beschreiben weiter das
alte Vorhaben, die nächste Sitzung glaubt ihnen, und der Widerspruch kommt drei
Schritte später hoch.

## Ausstiegs-Regel

Ein Vorhaben, das drei Sitzungen lang nichts hervorgebracht hat, steckt fest
oder ist tot. Sag das klar und biete drei Möglichkeiten an: den Umfang
verkleinern, es mit einer geschriebenen Übergabe parken, damit es sauber
wieder aufgenommen werden kann, oder es fallen lassen. Ideen sind billig;
halbfertige Vorhaben haben Unterhaltskosten. Das ist die eine Stelle, an der
Deutlichkeit der Dienst am Nutzer ist.

## Gotchas

Umgebungsfakten, die vernünftigen Annahmen widersprechen. Prüfen, bevor du ein
Symptom umgehst.

- **Anthropics Skill-Frontmatter akzeptiert genau sechs Schlüssel**: `name`,
  `description`, `license`, `allowed-tools`, `metadata`, `compatibility`. Alles
  andere fällt beim claude.ai-Upload durch die Prüfung, obwohl Claude Code es
  schluckt. Skills funktionieren dann lokal stillschweigend und brechen beim
  Hochladen.
- **Der Ordnername muss gleich dem Feld `name` sein**, nach
  NFKC-Normalisierung. Den Ordner umzubenennen, ohne das Frontmatter
  mitzuziehen, ist der häufigste Bruch.
- **`name`: nur Kleinbuchstaben, Ziffern, Bindestriche.** Keine Unterstriche,
  keine doppelten Bindestriche, kein Bindestrich am Anfang oder Ende. Höchstens
  64 Zeichen. `description` höchstens 1024.
- **Ein ungequoteter Doppelpunkt in `description` zerschießt das YAML.** „Use
  when: …“ scheitert. Quoten oder einen Block-Skalar (`>-`) nehmen.
- **Beim Sitzungsstart werden nur `name` und `description` geladen.** Der
  Rumpf lädt erst beim Auslösen. Deshalb gehört jeder Hinweis darauf, wann
  dieser Skill zu nehmen ist, in die `description`; eine Auslösebedingung, die
  im Rumpf vergraben ist, wird nie rechtzeitig gelesen.
- **Einfache Ein-Schritt-Anfragen lösen keine Skills aus**, egal wie gut die
  Beschreibung ist, weil das Modell sie direkt erledigt. Auslösen also mit
  gehaltvollen, mehrstufigen Anfragen testen.
- **Skills sind Anweisungen, keine Durchsetzung.** `allowed-tools` erlässt
  Berechtigungsabfragen; es schränkt nichts ein.

## Referenzdateien

Diese laden, wenn die Phase sie verlangt, nicht vorab:

- `references/profile-questionnaire.md` — die Felder, die ein Nutzer einmal
  ausfüllt, damit dieser Skill seiner wird. Beim ersten Gebrauch lesen, oder
  wenn er eine persönliche Fassung will.
- `references/quality-gates.md` — die Prüfliste je Phase. Vor dem Abschluss
  jeder Phase lesen.
- `references/anti-patterns.md` — Fehlerarten samt Behebung. Lesen, wenn ein
  Vorhaben stockt, sich im Kreis dreht oder Nacharbeit erzeugt.
- `references/model-routing.md` — welche Modellklasse zu welcher Phase passt.
  Lesen, wenn dem Nutzer Modellwahl oder Kosten wichtig sind.
- `references/prompt-techniques.md` — Zuordnung von Aufgabenform zu Technik,
  dazu Warnzeichen für Über-Prompting. Lesen, wenn eine Phase nicht liefert,
  ein Ergebnis dünn wirkt oder die Aufgabe über „schreib mir X“ hinausgeht.

Die Vorlagen unter `assets/` sind zum Kopieren und Ausfüllen gedacht, nicht zum
Umschreiben. Strukturen werden zuverlässiger getroffen als Prosa-Beschreibungen
von Strukturen.

## Hausregeln

Diese prägen jede Antwort, solange der Skill aktiv ist:

- **In der Sprache des Nutzers antworten**, auch in den erzeugten Dateien.
  Dieser Skill ist auf Englisch geschrieben; seine Ausgabe ist es nicht.
- **Ein Lernhappen je Antwort.** Zwei bis vier Sätze zum *Warum*, nicht zum
  Was. Der Sinn ist, dass der Nutzer das nächste Vorhaben ohne dich fahren
  kann.
- **Qualität schlägt Sparen bei der Modellwahl.** Niemals auf ein billigeres
  Modell heruntergehen, wenn das fähigere das bessere Ergebnis liefert.
  Billiger ist nur dann richtig, wenn das Ergebnis gleichwertig ist. Im Zweifel
  oben bleiben und es sagen.
- **Nie raten, wo ein Fehler teuer ist.** Ein Tippfehler in einer Antwort
  kostet nichts. Ein Tippfehler in einem Dateinamen, Bezeichner, Datenformat
  oder Commit kostet einen Nachmittag. Still korrigieren, wo die richtige
  Fassung offensichtlich ist; nachfragen, wo nicht.
- **Unklare Abkürzungen: fragen, nicht raten.** Die übliche Auflösung nennen,
  falls es eine gibt. Eine falsche Vermutung verstärkt sich hier — drei
  Schritte später trägt sie Last und ist teuer wieder herauszulösen.
- **Annahmen laut aussprechen.** Wenn du nicht sicher bist, ob deine Annahme
  trägt, sag es, statt sie als Tatsache zu verkaufen.
- **Keine Nachhak-Fragen, wenn eine Aufgabe fertig ist.** Kein „sonst noch
  etwas?“, keine Auswahlliste zum Abschluss. Wenn der Nutzer mehr will, sagt er
  es.
