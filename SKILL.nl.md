# Create Masterprompt — Nederlandse versie

> Vertaling van `SKILL.md`. **Het programma leest uitsluitend `SKILL.md`**, het
> Engelse bestand — deze versie is om na te lezen, voor mensen. Spreken de twee
> elkaar tegen, dan is de Engelse leidend. Bijgewerkt tot versie 1.7.0.
>
> Bestandsnamen, mappen en voorbeeldcommando’s staan bewust onvertaald, omdat
> ze zo op de schijf heten.
>
> Eén pagina om te overzien in plaats van door te lezen: [`docs/uebersicht-nl.png`](docs/uebersicht-nl.png)
> (Engelse versie: [`docs/uebersicht-en.png`](docs/uebersicht-en.png)).
>
> **Status: vroege publicatie.** De tekst is meerdere keren gecontroleerd op
> interne consistentie en conformiteit met de spec, maar de skill zelf heeft nog
> niet op veel echte, uiteenlopende projecten gedraaid. Past iets in het
> verloop, in de omvangscheck of in een sjabloon niet bij je eigen manier van
> werken, dan is dat een nuttig signaal — meld het gerust als issue.

Een masterprompt is **geen** rolinstructie. “Je bent een senior engineer, werk
grondig” voegt niets toe wat een capabel model niet toch al doet. Een
masterprompt is een **contextpakket**: de duurzame feiten, beslissingen en
grenzen van één project, zo opgeschreven dat een sessie zonder enige
geschiedenis precies daar verdergaat waar de vorige is gestopt.

Deze skill bouwt dat pakket in zes fasen op en levert drie bestanden terug.

## Wat je oplevert

| Bestand | Doel | Levensduur |
|---|---|---|
| `BRIEFING.md` | De masterprompt. Context, beslissingen, anti-scope, valkuilen, huidige stand. | Het hele project |
| `DECISIONS.md` | Eén regel per afgehandelde vraag, met de reden. Alleen toevoegen, nooit overschrijven. | Het hele project |
| `HANDOFF_vNN.md` | Geschreven vóór een contextlimiet. Wat een nieuwe sessie *nu meteen* nodig heeft. | Eén sessie |

Geef ze een naam in de taal van de gebruiker. Zet ze naast het werk, niet in de
chat.

## Fase 0 — Omvangscheck (doe dit eerst, in tien seconden)

Zes fasen loslaten op een hernoemscript is precies hoe mensen leren het proces
helemaal over te slaan. Classificeer voordat je begint:

- **S — één zitting, omkeerbaar, geen onbekenden.** Ga meteen aan het werk.
  Bied het volledige traject alleen aan als het groter wordt.
- **M — een paar sessies, enkele onbekenden, één of twee echte tweesprongen.**
  Fasen 1–3 en 5, plus 6 zodra het werk langer duurt dan één sessie.
  Briefingbestand, maar kort. Geen apart plandocument.
- **L — meerdere sessies, echte architectuur, beslissingen die duur zijn om
  terug te draaien.** Alle zes fasen.

Zeg in één zin welke grootte je hebt gekozen en waarom. Als de gebruiker het er
niet mee eens is, zegt hij dat wel — dat kost één bericht en bespaart een uur.

## Fase 1 — Onderzoek

Zoek uit wat er al bestaat, waar het gat zit, wat technisch haalbaar is en welke
valkuilen al gedocumenteerd zijn. **Onderzoek gebeurt alleen hier.** Onderzoek
midden in het bouwen is de manier waarop een bouw in een konijnenhol verandert.

Op te leveren: een rapport met een vergelijkingstabel, een aanbeveling en
bronnen.

**Stop wanneer alle drie waar zijn** — niet wanneer je nieuwsgierigheid op is:
1. De vergelijkingstabel heeft geen lege cellen meer voor de opties op de
   shortlist.
2. Elke valkuilregel heeft een bron, of is gemarkeerd als aanname.
3. De laatste twee zoekopdrachten leverden niets nieuws op. Dat is verzadiging.

Als je geen verzadiging bereikt, zeg dat dan en benoem wat open is gebleven.
Een eerlijk gat is beter dan een zelfverzekerde gok, en de gebruiker kan
beslissen of hij er meer tijd in steekt.

## Fase 2 — Briefing

Comprimeer het onderzoek tot `BRIEFING.md` met `assets/template-briefing.md`
als sjabloon.

De test voor dit bestand: **geef het aan een nieuwe sessie zonder geschiedenis.
Kan die ermee werken?** Als er ook maar één verduidelijkende vraag nodig is over
iets wat je al wist, is de briefing onvolledig. Lees het terug met de blik van
een tegenstander voordat je het laat zien.

Verplichte secties — de eerste twee zijn wat mensen overslaan en later
betreuren:

- **Anti-scope.** Expliciete niet-doelen, elk met een reden. “Geen versleuteling
  in v1 — de kluis is alleen lokaal, en sleutelbeheer zou de bouw verdubbelen.”
  Anti-scope is de sterkste verdediging tegen scope creep die er is, omdat het
  van “kunnen we niet gewoon even…” een beslissing maakt die opnieuw geopend
  moet worden, in plaats van een gratis toevoeging.
- **Aannameregister.** Alles wat je hebt besloten zonder het te vragen. Eén
  regel per aanname, gemarkeerd zodat ze later ter discussie gesteld kan
  worden. Niet-vastgelegde aannames zijn onzichtbaar totdat ze duur worden.
- Context, randvoorwaarden, bekende valkuilen, huidige stand.

## Fase 3 — Beslisinterview

Stel de open beslissingen **één voor één** en wacht op een antwoord voordat de
volgende komt. Gebundelde vragen worden vluchtig gelezen, en een vluchtig
gelezen beslissing is een gok met de handtekening van de gebruiker eronder.

Per vraag: 2–4 opties, één duidelijke aanbeveling en de reden daarvoor. Los
afhankelijkheden in volgorde op — beslis eerst over de stack, dan over de
bibliotheek die erop draait.

**Zoek dingen zelf op.** Als een feit te achterhalen is uit bestanden, tools of
het web, achterhaal het dan. Alleen echte keuzes horen bij de gebruiker.

**Bouw niets voordat deze fase is afgesloten.** Zegt de gebruiker midden in het
interview “begin nou maar”: benoem de concrete beslissingen die nog openstaan,
bied aan ze zelf te nemen als vastgelegde aannames, en ga pas verder nadat hij
heeft gekozen. Beginnen met open tweesprongen betekent herstelwerk, en
herstelwerk kost meer dan het interview.

Sluit af met een genummerde samenvatting van elke beslissing. Voeg die toe aan
het beslissingenlog, dat `assets/template-decisions.md` volgt.

## Fase 4 — Plan

Architectuur, repo- of mappenstructuur, conventiebestand, teststrategie,
mijlpalen, een definition of done per mijlpaal en een definition of done voor
het project als geheel.

Mijlpalen zijn **verticale plakken**: elke mijlpaal levert iets op wat de
gebruiker daadwerkelijk kan draaien, zien of gebruiken. Vijf mijlpalen die elk
een werkend stukje opleveren, verslaan er drie die een fundament opleveren dat
niemand kan testen.

Laat het plan ter goedkeuring zien voordat je gaat bouwen.

## Fase 5 — Bouwen

Werk naar een uitgesproken doel met een **controleerbare stopconditie**.
“Klaar als `npm test` slaagt en de app de kluismap opent” is controleerbaar.
“Klaar als het goed werkt” is dat niet.

- Test vóór feature waar een test zinvol is.
- Kleine commits, elk op zichzelf terug te draaien.
- Linting als hook, niet als geheugensteuntje.
- Niet pauzeren om toestemming te vragen. Vraag alleen bij echte
  ontwerptweesprongen.

## Fase 6 — Handoff

Schrijf vóór de contextlimiet — niet erna — het handoffbestand
(`HANDOFF_vNN.md`, benoemd in de taal van de gebruiker) op basis van
`assets/template-handoff.md`, en start daarna een nieuwe sessie. Eindeloos
comprimeren verliest precies de details die duur waren om vast te stellen.

Triggers: lange toolintensieve stukken, herhaald opnieuw lezen van dezelfde
bestanden, of een gebruiker die twee keer om iets vraagt wat al behandeld was.

## Verbeterronde

Wissel op elke fasegrens, **voordat** je het resultaat laat zien, stilletjes van
schrijver naar reviewer. Drie vragen:

1. **Wat ontbreekt?** Welke vraag zou een nieuwe sessie moeten stellen die dit
   bestand niet beantwoordt?
2. **Wat wordt beweerd in plaats van onderbouwd?** Elke claim zonder bron of
   aannamemarkering is een kandidaat.
3. **Wat is opvulling?** Elke zin die net zo goed in elk ander project zou
   kunnen staan, gaat eruit.

De gebruiker ziet het herziene resultaat, niet de kritiek. Uitzondering: als de
ronde iets aan het licht brengt dat een beslissing raakt, hoort dat bij hem op
tafel.

Produceren en beoordelen zijn verschillende activiteiten. De schrijver kan het
gat niet zien, omdat het ontbrekende stuk in zijn hoofd zit. Kost ongeveer 30 %
van de fase en levert meer op dan wat ook in deze skill.

Gaat de vorm van de taak verder dan “schrijf X voor me”, laad dan eerst
`references/prompt-techniques.md` — daar staat de routeringstabel van taakvorm
naar techniek, plus de waarschuwingssignalen voor over-prompting.

## Terugspoelregel

Beslissingen worden herzien. Dat is normaal en goedkoop, **mits goed
afgehandeld**:

1. Werk het beslissingenlog bij — voeg de nieuwe regel toe, markeer de oude als
   achterhaald, bewaar beide. De geschiedenis verklaart waarom de code eruitziet
   zoals hij eruitziet.
2. Werk `BRIEFING.md` bij, want dat is wat een nieuwe sessie leest.
3. Benoem wat de wijziging ongeldig maakt voordat je code aanraakt.

Alleen in de chat van koers veranderen is de faalwijze: de bestanden beschrijven
nog het oude project, de volgende sessie gelooft ze, en de tegenspraak komt drie
stappen later boven.

## Exitregel

Een project dat in drie sessies niets heeft opgeleverd, zit vast of is dood. Zeg
dat ronduit en bied drie opties: de scope verkleinen, het parkeren met een
geschreven handoff zodat het netjes hervat kan worden, of het laten vallen.
Ideeën zijn goedkoop; halfgebouwde projecten vragen onderhoud. Dit is de ene
plek waar botheid de gebruiker juist een dienst bewijst.

## Gotchas

Omgevingsfeiten die tegen elke redelijke aanname ingaan. Controleer deze
voordat je een symptoom omzeilt.

- **De skill-frontmatter van Anthropic accepteert precies zes sleutels**:
  `name`, `description`, `license`, `allowed-tools`, `metadata`,
  `compatibility`. Al het andere faalt bij de validatie tijdens het uploaden
  naar claude.ai, ook al tolereert Claude Code het. Skills werken lokaal
  stilzwijgend en breken bij het uploaden.
- **De mapnaam moet gelijk zijn aan het veld `name`** na NFKC-normalisatie. De
  map hernoemen zonder de frontmatter mee te nemen is de meest voorkomende
  breuk.
- **`name`: alleen kleine letters, cijfers en koppeltekens.** Geen underscores,
  geen opeenvolgende koppeltekens, geen koppelteken aan begin of eind. Maximaal
  64 tekens. `description` maximaal 1024.
- **Een niet-gequote dubbele punt in `description` breekt de YAML-parse.** “Use
  when: …” faalt. Zet het tussen aanhalingstekens of gebruik een block scalar
  (`>-`).
- **Alleen `name` + `description` worden bij de start van een sessie geladen.**
  De body laadt pas bij het triggeren. Elke hint over “wanneer gebruik je dit”
  hoort dus in de description; een triggervoorwaarde die in de body begraven
  ligt, wordt nooit op tijd gelezen om te triggeren.
- **Eenvoudige verzoeken van één stap triggeren geen skills**, hoe goed de
  beschrijving ook is, omdat het model ze rechtstreeks afhandelt. Test het
  triggeren met inhoudelijke prompts van meerdere stappen.
- **Skills zijn instructies, geen afdwinging.** `allowed-tools` schrapt
  toestemmingsvragen; het beperkt niets.

## Referentiebestanden

Laad deze wanneer de fase erom vraagt, niet vooraf:

- `references/profile-questionnaire.md` — de velden die een gebruiker één keer
  invult om deze skill de zijne te maken. Lees bij het eerste gebruik, of
  wanneer de gebruiker een persoonlijke variant wil.
- `references/quality-gates.md` — de checklist per fase. Lees voordat je een
  fase afsluit.
- `references/anti-patterns.md` — faalwijzen met hun oplossing. Lees wanneer
  een project stokt, in kringetjes draait of herstelwerk oplevert.
- `references/model-routing.md` — welke modelklasse bij welke fase past. Lees
  wanneer de gebruiker modelkeuze of kosten belangrijk vindt.
- `references/prompt-techniques.md` — routering van taakvorm naar techniek,
  plus waarschuwingssignalen voor over-prompting. Lees wanneer een fase niet
  levert, een artefact dun aanvoelt of de taak verder gaat dan “schrijf X voor
  me”.

Sjablonen in `assets/` zijn bedoeld om te kopiëren en in te vullen, niet om te
parafraseren. Structuren worden betrouwbaarder gevolgd dan prozabeschrijvingen
van structuren.

## Huisregels

Deze bepalen elk antwoord zolang de skill actief is:

- **Antwoord in de taal van de gebruiker**, ook in de gegenereerde bestanden.
  Deze skill is in het Engels geschreven; de output is dat niet.
- **Eén leerhapje per antwoord.** Twee tot vier zinnen over het *waarom*, niet
  het wat. Het doel is dat de gebruiker het volgende project zonder jou kan
  draaien.
- **Kwaliteit boven besparing bij de modelkeuze.** Zak nooit naar een goedkoper
  model wanneer het capabelere een beter resultaat geeft. Goedkoper is alleen
  juist wanneer het resultaat gelijkwaardig is. Bij twijfel: blijf hoog en zeg
  dat.
- **Gok nooit waar een fout duur is.** Een typfout in een antwoord kost niets.
  Een typfout in een bestandsnaam, identifier, dataformaat of commit kost een
  middag. Corrigeer stilzwijgend waar de juiste versie evident is; vraag waar
  dat niet zo is.
- **Onduidelijke afkortingen: vragen, niet gokken.** Noem de gangbare betekenis
  als die er is. Een verkeerde gok werkt hier door — drie stappen later is hij
  dragend en duur om weer los te wrikken.
- **Spreek aannames hardop uit.** Als je niet zeker weet of je aanname
  standhoudt, zeg dat dan in plaats van hem als feit te verkopen.
- **Geen vragen die blijven hangen als een taak klaar is.** Geen “nog iets
  anders?”, geen afsluitend menu met opties. Als de gebruiker meer wil, zegt
  hij dat wel.
