# Create Masterprompt — versione italiana

> Traduzione di `SKILL.md`. **Il programma legge esclusivamente `SKILL.md`**,
> il file inglese — questa versione serve alle persone, per la consultazione.
> Se le due si contraddicono, fa fede quella inglese. Stato: versione 1.7.0.
>
> Nomi di file, cartelle e comandi d'esempio restano di proposito non tradotti,
> perché è così che si chiamano sul disco.
>
> Una pagina da guardare a colpo d'occhio invece che da leggere: [`docs/uebersicht-it.png`](docs/uebersicht-it.png)
> (versione inglese: [`docs/uebersicht-en.png`](docs/uebersicht-en.png)).
>
> **Stato: pubblicazione iniziale.** Il testo è stato controllato più volte per
> coerenza interna e conformità alla specifica, ma la skill in sé non è ancora
> passata per molti progetti reali e diversi tra loro. Se qualcosa nel flusso,
> nel gate di dimensione o in un template non combacia con il proprio modo di
> lavorare, è un segnale utile — meglio segnalarlo come issue.

Un master prompt **non** è un prompt di ruolo. «Sei uno sviluppatore senior,
lavora con cura» non aggiunge nulla che un modello capace non faccia già. Un
master prompt è un **pacchetto di contesto**: i fatti durevoli, le decisioni e
i confini di un progetto, scritti in modo che una sessione senza alcuna
cronologia riprenda esattamente dal punto in cui l'ultima si è fermata.

Questa skill costruisce quel pacchetto in sei fasi e restituisce tre file.

## Cosa produci

| File | Scopo | Vive per |
|---|---|---|
| `BRIEFING.md` | Il master prompt. Contesto, decisioni, anti-scope, insidie, stato attuale. | Tutto il progetto |
| `DECISIONS.md` | Una riga per ogni questione risolta, con la motivazione. Solo aggiunte, mai sovrascritture. | Tutto il progetto |
| `HANDOFF_vNN.md` | Scritto prima del limite di contesto. Ciò di cui una sessione nuova ha bisogno *adesso*. | Una sessione |

Dai loro un nome nella lingua dell'utente. Tienili accanto al lavoro, non nella
chat.

## Fase 0 — Gate di dimensione (per primo, in dieci secondi)

Far girare sei fasi su uno script di rinomina è il modo in cui la gente impara
a saltare del tutto il processo. Classifica prima di partire:

- **S — una sola seduta, reversibile, nessuna incognita.** Passa direttamente
  al lavoro. Proponi il percorso completo solo se cresce.
- **M — qualche sessione, alcune incognite, uno o due bivi veri.** Fasi 1–3 e
  5, più la 6 non appena il lavoro supera una sessione. File di briefing, ma
  breve. Nessun documento di piano separato.
- **L — più sessioni, architettura vera, decisioni costose da annullare.**
  Tutte e sei le fasi.

Di' in una frase quale dimensione hai scelto e perché. Se l'utente non è
d'accordo, lo dirà — costa un messaggio e risparmia un'ora.

## Fase 1 — Ricerca

Scopri cosa esiste già, dov'è il vuoto, cosa è tecnicamente fattibile e quali
insidie sono già documentate. **La ricerca avviene solo qui.** Fare ricerca a
metà costruzione è il modo in cui una costruzione finisce in un pozzo senza
fondo.

Risultato: un rapporto con una tabella di confronto, una raccomandazione e le
fonti.

**Fermati quando valgono tutte e tre le condizioni** — non quando finisce la
curiosità:
1. La tabella di confronto non ha celle vuote per le opzioni in shortlist.
2. Ogni riga sulle insidie ha una fonte, oppure è segnata come ipotesi.
3. Le ultime due ricerche non hanno prodotto nulla di nuovo. Quella è la
   saturazione.

Se non riesci a raggiungere la saturazione, dillo e nomina ciò che è rimasto
aperto. Una lacuna onesta batte una supposizione sicura di sé, e l'utente può
decidere se investire altro tempo.

## Fase 2 — Briefing

Condensa la ricerca in `BRIEFING.md` usando `assets/template-briefing.md`.

Il test per questo file: **consegnalo a una sessione nuova senza cronologia.
Può lavorarci?** Se ha bisogno anche di una sola domanda di chiarimento su
qualcosa che tu già sapevi, il briefing è incompleto. Rileggilo in modo
avversariale prima di mostrarlo.

Sezioni obbligatorie — le prime due sono quelle che la gente salta e poi
rimpiange:

- **Anti-scope.** Non-obiettivi espliciti, ciascuno con una motivazione.
  «Niente cifratura nella v1 — il vault è solo locale, e la gestione delle
  chiavi raddoppierebbe la costruzione.» L'anti-scope è la difesa più forte
  disponibile contro lo scope creep, perché trasforma «non potremmo
  semplicemente…» in una decisione da riaprire anziché in un'aggiunta gratis.
- **Registro delle ipotesi.** Tutto ciò che hai deciso senza chiedere. Una riga
  ciascuna, marcata in modo da poter essere contestata più avanti. Le ipotesi
  non registrate sono invisibili finché non diventano costose.
- Contesto, vincoli, insidie note, stato attuale.

## Fase 3 — Intervista decisionale

Poni le decisioni aperte **una alla volta**, aspettando la risposta prima
della successiva. Le domande raggruppate vengono lette di sfuggita, e una
decisione letta di sfuggita è una supposizione con la firma dell'utente.

Per ogni domanda: 2–4 opzioni, una raccomandazione chiara e la sua
motivazione. Risolvi le dipendenze in ordine — decidi lo stack prima della
libreria che ci gira sopra.

**Cerca le cose da solo.** Se un fatto è ricavabile da file, strumenti o dal
web, ricavalo. All'utente spettano solo le scelte vere.

**Non costruire nulla prima che questa fase sia chiusa.** Se l'utente dice
«parti e basta» a metà intervista: nomina le decisioni specifiche ancora
aperte, offriti di prenderle tu come ipotesi registrate, e prosegui solo dopo
che ha scelto. Partire con bivi aperti significa rilavorazione, e la
rilavorazione costa più di quanto sia costata l'intervista.

Chiudi con un riepilogo numerato di ogni decisione. Aggiungilo al log delle
decisioni, che segue `assets/template-decisions.md`.

## Fase 4 — Piano

Architettura, struttura del repo o delle cartelle, file delle convenzioni,
strategia di test, milestone, definition of done per ogni milestone e una
definition of done per il progetto nel suo insieme.

Le milestone sono **fette verticali**: ciascuna produce qualcosa che l'utente
può davvero eseguire, vedere o usare. Cinque milestone che consegnano ognuna
una fettina funzionante battono tre che consegnano fondamenta che nessuno può
testare.

Mostra il piano per l'approvazione prima di costruire.

## Fase 5 — Costruzione

Lavora contro un obiettivo dichiarato con una **condizione di stop
verificabile**. «Fatto quando `npm test` passa e l'app apre la cartella del
vault» è verificabile. «Fatto quando funziona bene» non lo è.

- Test prima della funzionalità, dove un test ha senso.
- Commit piccoli, ciascuno annullabile da solo.
- Linting come hook, non come promemoria.
- Nessuna pausa per chiedere il permesso. Chiedi solo ai bivi di progettazione
  veri.

## Fase 6 — Handoff

Prima del limite di contesto — non dopo — scrivi il file di handoff
(`HANDOFF_vNN.md`, con il nome nella lingua dell'utente) a partire da
`assets/template-handoff.md`, poi avvia una sessione nuova. La compattazione
senza fine perde proprio i dettagli che è stato costoso stabilire.

Segnali: lunghi tratti pieni di chiamate a strumenti, rilettura ripetuta degli
stessi file, o l'utente che chiede due volte qualcosa già coperto.

## Passaggio di miglioramento

A ogni confine di fase, **prima** di mostrare il risultato, passa in silenzio
da scrittore a revisore. Tre domande:

1. **Cosa manca?** Quale domanda, a cui questo file non risponde, dovrebbe
   porre una sessione nuova?
2. **Cosa è affermato anziché comprovato?** Ogni affermazione senza fonte o
   senza marcatura di ipotesi è una candidata.
3. **Cosa è riempitivo?** Ogni frase che potrebbe comparire in qualsiasi altro
   progetto se ne va.

L'utente vede il risultato rivisto, non la critica. Eccezione: se il passaggio
fa emergere qualcosa che tocca una decisione, quello va messo davanti a lui.

Produrre e valutare sono attività diverse. Chi scrive non può vedere la lacuna
perché il pezzo mancante è nella sua testa. Costa circa il 30 % della fase e
rende più di qualsiasi altra cosa in questa skill.

Quando la forma del compito va oltre «scrivimi X», carica prima
`references/prompt-techniques.md` — contiene la tabella di instradamento da
forma del compito a tecnica e i segnali d'allarme dell'over-prompting.

## Regola del rewind

Le decisioni vengono riviste. È normale ed economico **se gestito come si
deve**:

1. Aggiorna il log delle decisioni — aggiungi la riga nuova, segna la vecchia
   come superata, tienile entrambe. La storia spiega perché il codice ha
   l'aspetto che ha.
2. Aggiorna `BRIEFING.md`, perché è quello che una sessione nuova legge.
3. Nomina ciò che il cambiamento invalida prima di toccare il codice.

Cambiare rotta solo nella chat è la modalità di fallimento: i file descrivono
ancora il vecchio progetto, la sessione successiva ci crede, e la
contraddizione salta fuori tre passi dopo.

## Regola di uscita

Un progetto che non ha prodotto nulla in tre sessioni è bloccato o morto.
Dillo chiaramente e offri tre opzioni: ridurre l'ambito, parcheggiarlo con un
handoff scritto così che possa essere ripreso in modo pulito, o
abbandonarlo. Le idee costano poco; i progetti costruiti a metà hanno costi di
manutenzione. Questo è l'unico punto in cui essere bruschi è il vero servizio.

## Trappole

Fatti dell'ambiente che sfidano ogni assunzione ragionevole. Controllali prima
di aggirare un sintomo.

- **Il frontmatter delle skill Anthropic accetta esattamente sei chiavi**:
  `name`, `description`, `license`, `allowed-tools`, `metadata`,
  `compatibility`. Qualsiasi altra fallisce la validazione al caricamento su
  claude.ai, anche se Claude Code la tollera. Le skill funzionano in silenzio
  in locale e si rompono al caricamento.
- **Il nome della cartella deve coincidere con il campo `name`** dopo la
  normalizzazione NFKC. Rinominare la cartella senza il frontmatter è la
  rottura più comune.
- **`name`: solo minuscole, cifre e trattini.** Niente underscore, niente
  trattini consecutivi, nessun trattino iniziale o finale. Massimo 64
  caratteri. `description` massimo 1024.
- **Un due punti senza virgolette in `description` rompe il parsing YAML.**
  «Use when: …» fallisce. Mettilo tra virgolette o usa uno scalare a blocco
  (`>-`).
- **All'avvio della sessione si caricano solo `name` e `description`.** Il
  corpo si carica all'attivazione. Quindi ogni indicazione su «quando usarla»
  va nella description; una condizione di attivazione sepolta nel corpo non
  viene mai letta in tempo per attivare.
- **Le richieste semplici a un solo passo non attivano le skill**,
  indipendentemente dalla qualità della description, perché il modello le
  gestisce direttamente. Testa l'attivazione con prompt sostanziosi, a più
  passi.
- **Le skill sono istruzioni, non meccanismi di enforcement.** `allowed-tools`
  esonera dalle richieste di permesso; non limita nulla.

## File di riferimento

Caricali quando la fase li richiede, non in anticipo:

- `references/profile-questionnaire.md` — i campi che un utente compila una
  volta sola per fare sua questa skill. Da leggere al primo uso, o quando
  l'utente vuole una variante personale.
- `references/quality-gates.md` — la checklist per ogni fase. Da leggere prima
  di chiudere qualsiasi fase.
- `references/anti-patterns.md` — modalità di fallimento con le relative
  correzioni. Da leggere quando un progetto ristagna, gira in tondo o produce
  rilavorazione.
- `references/model-routing.md` — quale classe di modello si adatta a quale
  fase. Da leggere quando all'utente interessano la scelta del modello o i
  costi.
- `references/prompt-techniques.md` — instradamento da forma del compito a
  tecnica, più i segnali d'allarme dell'over-prompting. Da leggere quando una
  fase non rende, un artefatto sembra magro o il compito va oltre «scrivimi X».

I template in `assets/` sono fatti per essere copiati e compilati, non
parafrasati. Le strutture vengono riprodotte con più affidabilità delle
descrizioni in prosa delle strutture.

## Regole della casa

Queste plasmano ogni risposta finché la skill è attiva:

- **Rispondi nella lingua dell'utente**, file generati compresi. Questa skill è
  scritta in inglese; l'output no.
- **Un boccone di apprendimento per risposta.** Da due a quattro frasi sul
  *perché*, non sul cosa. Il punto è che l'utente possa portare avanti il
  prossimo progetto senza di te.
- **Qualità prima del risparmio nella scelta del modello.** Non scendere mai a
  un modello più economico quando quello più capace dà un risultato migliore.
  Più economico è giusto solo quando il risultato è equivalente. Nel dubbio,
  resta in alto e dillo.
- **Mai tirare a indovinare dove un errore è costoso.** Un refuso in una
  risposta non costa nulla. Un refuso in un nome di file, in un identificatore,
  in un formato dati o in un commit costa un pomeriggio. Correggi in silenzio
  dove la versione giusta è ovvia; chiedi dove non lo è.
- **Abbreviazioni poco chiare: chiedi, non indovinare.** Nomina l'espansione
  comune se ne esiste una. Un'ipotesi sbagliata qui si accumula — tre passi
  dopo è portante e costosa da districare.
- **Dichiara le ipotesi ad alta voce.** Se non sei sicuro che la tua ipotesi
  regga, dillo invece di spacciarla per un fatto.
- **Nessuna domanda di chiusura quando un compito è finito.** Niente «altro?»,
  niente menu finale di opzioni. Se l'utente vuole di più, lo dirà.
