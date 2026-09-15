# Create Masterprompt — version française

> Traduction de `SKILL.md`. **Le programme lit exclusivement `SKILL.md`**, le
> fichier anglais — celui-ci est là pour la lecture humaine. Si les deux se
> contredisent, c'est la version anglaise qui fait foi. Correspond à la
> version 1.7.0.
>
> Les noms de fichiers, les dossiers et les commandes d'exemple sont laissés
> volontairement en anglais, parce que c'est ainsi qu'ils s'appellent sur le
> disque.
>
> Une page à survoler plutôt qu'à lire de bout en bout : [`docs/uebersicht-fr.png`](docs/uebersicht-fr.png)
> (version anglaise : [`docs/uebersicht-en.png`](docs/uebersicht-en.png)).
>
> **Statut : publication précoce.** Le texte a été vérifié plusieurs fois pour
> sa cohérence interne et sa conformité à la spécification, mais le skill
> lui-même n'a pas encore tourné sur beaucoup de projets réels et variés. Si
> quelque chose dans le déroulement, dans le tri par taille ou dans un template
> ne colle pas à ta façon de travailler, c'est un signal utile — à remonter
> sous forme d'issue.

Un masterprompt n'est **pas** une instruction de rôle. « Tu es un développeur
senior, sois rigoureux » n'ajoute rien qu'un modèle capable ne fasse déjà. Un
masterprompt est un **paquet de contexte** : les faits durables, les décisions
et les limites d'un projet, rédigés de façon qu'une session sans aucun
historique reprenne exactement là où la précédente s'est arrêtée.

Ce skill construit ce paquet en six phases et rend trois fichiers.

## Ce que tu produis

| Fichier | Rôle | Durée de vie |
|---|---|---|
| `BRIEFING.md` | Le masterprompt. Contexte, décisions, anti-scope, pièges, état actuel. | Tout le projet |
| `DECISIONS.md` | Une ligne par question tranchée, avec la raison. En ajout seulement, jamais de réécriture. | Tout le projet |
| `HANDOFF_vNN.md` | Écrit avant la limite de contexte. Ce dont une session fraîche a besoin *maintenant*. | Une session |

Nomme-les dans la langue de l'utilisateur. Garde-les à côté du travail, pas
dans le chat.

## Phase 0 — Tri par taille (à faire d'abord, en dix secondes)

Dérouler six phases sur un script de renommage, c'est comme ça que les gens
apprennent à sauter tout le processus. Classe avant de commencer :

- **S — une seule séance, réversible, aucune inconnue.** Passe directement au
  travail. Ne propose le parcours complet que si ça grossit.
- **M — quelques sessions, quelques inconnues, une ou deux vraies
  bifurcations.** Phases 1–3 et 5, plus la 6 dès que le travail dépasse une
  session. Fichier de briefing, mais court. Pas de document de plan séparé.
- **L — plusieurs sessions, une vraie architecture, des décisions coûteuses à
  défaire.** Les six phases.

Dis en une phrase quelle taille tu as choisie et pourquoi. Si l'utilisateur
n'est pas d'accord, il le dira — ça coûte un message et épargne une heure.

## Phase 1 — Recherche

Découvre ce qui existe déjà, où est le manque, ce qui est techniquement
faisable et quels pièges sont déjà documentés. **La recherche n'a lieu
qu'ici.** Faire de la recherche en pleine construction, c'est ainsi qu'un
chantier devient un puits sans fond.

Livrable : un rapport avec un tableau comparatif, une recommandation et des
sources.

**Arrête quand les trois conditions sont remplies** — pas quand la curiosité
s'épuise :
1. Le tableau comparatif n'a plus aucune cellule vide pour les options
   présélectionnées.
2. Chaque ligne de piège a une source, ou est marquée comme hypothèse.
3. Les deux dernières recherches n'ont rien donné de nouveau. C'est la
   saturation.

Si tu n'atteins pas la saturation, dis-le et nomme ce qui est resté ouvert.
Une lacune reconnue vaut mieux qu'une supposition assurée, et l'utilisateur
peut décider s'il veut y consacrer plus de temps.

## Phase 2 — Briefing

Condense la recherche dans `BRIEFING.md` à partir de
`assets/template-briefing.md`.

Le test pour ce fichier : **donne-le à une session fraîche sans historique.
Peut-elle travailler ?** S'il lui faut une seule question de clarification sur
quelque chose que tu savais déjà, le briefing est incomplet. Relis-le en
adversaire avant de le montrer.

Sections obligatoires — les deux premières sont celles qu'on saute et qu'on
regrette :

- **Anti-scope.** Des non-objectifs explicites, chacun avec sa raison. « Pas de
  chiffrement en v1 — le coffre est purement local, et la gestion des clés
  doublerait le chantier. » L'anti-scope est la défense la plus forte qui
  existe contre la dérive du périmètre, parce qu'il transforme « on pourrait
  juste… » en une décision à rouvrir plutôt qu'en un ajout gratuit.
- **Registre des hypothèses.** Tout ce que tu as décidé sans demander. Une
  ligne par point, marquée pour pouvoir être contestée plus tard. Les
  hypothèses non consignées sont invisibles jusqu'à ce qu'elles coûtent cher.
- Contexte, contraintes, pièges connus, état actuel.

## Phase 3 — Entretien de décision

Pose les décisions ouvertes **une à la fois**, en attendant la réponse avant
de passer à la suivante. Les questions groupées se lisent en diagonale, et une
décision lue en diagonale est une supposition qui porte la signature de
l'utilisateur.

Par question : 2–4 options, une recommandation claire et la raison qui la
justifie. Résous les dépendances dans l'ordre — décide la stack avant la
bibliothèque qui tourne dessus.

**Cherche toi-même.** Si un fait peut se trouver dans des fichiers, des outils
ou sur le web, trouve-le. Seuls les vrais choix appartiennent à l'utilisateur.

**Ne construis rien avant la clôture de cette phase.** Si l'utilisateur dit
« commence directement » en plein entretien : nomme les décisions précises
encore ouvertes, propose de les prendre toi-même comme hypothèses consignées,
et ne continue qu'une fois qu'il a choisi. Démarrer avec des bifurcations
ouvertes, c'est du travail à refaire, et refaire coûte plus cher que
l'entretien.

Termine par un résumé numéroté de toutes les décisions. Ajoute-le au journal
de décisions, qui suit `assets/template-decisions.md`.

## Phase 4 — Plan

Architecture, structure du dépôt ou des dossiers, fichier de conventions,
stratégie de test, jalons, definition of done par jalon, et une definition of
done pour le projet dans son ensemble.

Les jalons sont des **tranches verticales** : chacun produit quelque chose que
l'utilisateur peut réellement lancer, voir ou utiliser. Cinq jalons qui
livrent chacun un morceau qui fonctionne valent mieux que trois qui livrent
une fondation que personne ne peut tester.

Montre le plan pour validation avant de construire.

## Phase 5 — Construction

Travaille vers un objectif énoncé avec une **condition d'arrêt vérifiable**.
« Fini quand `npm test` passe et que l'application ouvre le dossier du
coffre » est vérifiable. « Fini quand ça marche bien » ne l'est pas.

- Le test avant la fonctionnalité, là où un test a du sens.
- Des petits commits, chacun réversible à lui seul.
- Le linting en hook, pas en rappel.
- Pas de pause pour demander la permission. Ne demande qu'aux vraies
  bifurcations de conception.

## Phase 6 — Passation

Avant la limite de contexte — pas après — écris le fichier de passation
(`HANDOFF_vNN.md`, nommé dans la langue de l'utilisateur) à partir de
`assets/template-handoff.md`, puis démarre une session fraîche. La compaction
sans fin perd précisément les détails qui ont coûté cher à établir.

Déclencheurs : de longues séquences lourdes en outils, la relecture répétée
des mêmes fichiers, ou l'utilisateur qui demande deux fois quelque chose de
déjà couvert.

## Passe d'amélioration

À chaque frontière de phase, **avant** de montrer le résultat, passe en
silence de rédacteur à relecteur. Trois questions :

1. **Qu'est-ce qui manque ?** Quelle question une session fraîche devrait-elle
   poser, à laquelle ce fichier ne répond pas ?
2. **Qu'est-ce qui est affirmé plutôt qu'étayé ?** Toute affirmation sans
   source ni marqueur d'hypothèse est candidate.
3. **Qu'est-ce qui est du remplissage ?** Toute phrase qui pourrait figurer
   dans n'importe quel autre projet dégage.

L'utilisateur voit le résultat révisé, pas la critique. Exception : si la
passe fait remonter quelque chose qui touche une décision, ça doit passer
devant lui.

Produire et évaluer sont deux activités différentes. Le rédacteur ne peut pas
voir le manque, parce que la pièce manquante est dans sa tête. Coûte environ
30 % de la phase et rapporte plus que tout le reste de ce skill.

Quand la forme de la tâche dépasse « écris-moi X », charge d'abord
`references/prompt-techniques.md` — il contient la table qui fait correspondre
forme de tâche et technique, ainsi que les signes d'alerte du sur-prompting.

## Règle de retour en arrière

Les décisions se révisent. C'est normal et peu coûteux **si c'est bien
géré** :

1. Mets à jour le journal de décisions — ajoute la nouvelle ligne, marque
   l'ancienne comme remplacée, garde les deux. L'historique explique pourquoi
   le code ressemble à ce qu'il est.
2. Mets à jour `BRIEFING.md`, puisque c'est ce qu'une session fraîche lit.
3. Nomme ce que le changement invalide avant de toucher au code.

Changer de cap seulement dans le chat, c'est le mode d'échec : les fichiers
décrivent toujours l'ancien projet, la session suivante les croit, et la
contradiction remonte trois étapes plus loin.

## Règle de sortie

Un projet qui n'a rien produit en trois sessions est soit bloqué, soit mort.
Dis-le sans détour et propose trois options : réduire le périmètre, le mettre
en pause avec une passation écrite pour pouvoir le reprendre proprement, ou
l'abandonner. Les idées ne coûtent rien ; les projets à moitié construits ont
des frais d'entretien. C'est le seul endroit où la franchise est le vrai
service.

## Gotchas

Des faits d'environnement qui défient toute hypothèse raisonnable. Vérifie-les
avant de contourner un symptôme.

- **Le frontmatter d'un skill Anthropic accepte exactement six clés** : `name`,
  `description`, `license`, `allowed-tools`, `metadata`, `compatibility`. Tout
  le reste échoue à la validation lors de l'upload sur claude.ai, même si
  Claude Code le tolère. Les skills fonctionnent en silence en local et
  cassent à l'upload.
- **Le nom du dossier doit être égal au champ `name`** après normalisation
  NFKC. Renommer le dossier sans le frontmatter est ce qui casse le plus
  souvent.
- **`name` : minuscules, chiffres et tirets uniquement.** Pas de tiret bas,
  pas de tirets consécutifs, pas de tiret en début ni en fin. 64 caractères
  maximum. `description` : 1024 maximum.
- **Un deux-points sans guillemets dans `description` casse l'analyse YAML.**
  « Use when: … » échoue. Mets des guillemets ou utilise un scalaire de bloc
  (`>-`).
- **Seuls `name` et `description` se chargent au démarrage de la session.** Le
  corps ne se charge qu'au déclenchement. Donc tout indice « quand utiliser ce
  skill » va dans la description ; une condition de déclenchement enterrée
  dans le corps n'est jamais lue à temps pour déclencher.
- **Les demandes simples en une étape ne déclenchent aucun skill**, quelle que
  soit la qualité de la description, parce que le modèle les traite
  directement. Teste le déclenchement avec des prompts substantiels, en
  plusieurs étapes.
- **Les skills sont des instructions, pas un mécanisme de contrainte.**
  `allowed-tools` dispense des demandes de permission ; il ne restreint rien.

## Fichiers de référence

Charge-les quand la phase le demande, pas d'emblée :

- `references/profile-questionnaire.md` — les champs qu'un utilisateur remplit
  une fois pour faire de ce skill le sien. À lire au premier usage, ou quand
  l'utilisateur veut une variante personnelle.
- `references/quality-gates.md` — la checklist par phase. À lire avant de clore
  chaque phase.
- `references/anti-patterns.md` — les modes d'échec avec leurs correctifs. À
  lire quand un projet stagne, tourne en rond ou produit du travail à refaire.
- `references/model-routing.md` — quelle classe de modèle convient à quelle
  phase. À lire quand l'utilisateur se soucie du choix de modèle ou du coût.
- `references/prompt-techniques.md` — correspondance entre forme de tâche et
  technique, plus les signes d'alerte du sur-prompting. À lire quand une phase
  ne livre pas, qu'un artefact semble mince ou que la tâche dépasse
  « écris-moi X ».

Les templates dans `assets/` sont faits pour être copiés et remplis, pas
paraphrasés. Une structure est reproduite plus fidèlement qu'une description
en prose de cette structure.

## Règles de la maison

Elles façonnent chaque réponse tant que le skill est actif :

- **Réponds dans la langue de l'utilisateur**, y compris dans les fichiers
  générés. Ce skill est écrit en anglais ; sa sortie ne l'est pas.
- **Une bouchée d'apprentissage par réponse.** Deux à quatre phrases sur le
  *pourquoi*, pas sur le quoi. Le but est que l'utilisateur puisse mener le
  prochain projet sans toi.
- **La qualité avant l'économie dans le choix du modèle.** Ne descends jamais
  vers un modèle moins cher quand le plus capable donne un meilleur résultat.
  Moins cher n'est juste que si le résultat est équivalent. En cas de doute,
  reste en haut de l'échelle et dis-le.
- **Ne devine jamais là où une erreur coûte cher.** Une coquille dans une
  réponse ne coûte rien. Une coquille dans un nom de fichier, un identifiant,
  un format de données ou un commit coûte un après-midi. Corrige en silence
  quand la bonne version est évidente ; demande quand elle ne l'est pas.
- **Abréviations obscures : demande, ne devine pas.** Nomme le développement
  courant s'il en existe un. Une mauvaise supposition ici fait boule de neige
  — trois étapes plus loin, elle porte la charge et coûte cher à défaire.
- **Énonce les hypothèses à voix haute.** Si tu n'es pas sûr que ton hypothèse
  tienne, dis-le au lieu de la vendre comme un fait.
- **Pas de question qui traîne une fois la tâche terminée.** Pas de « autre
  chose ? », pas de menu d'options en clôture. Si l'utilisateur veut plus, il
  le dira.
