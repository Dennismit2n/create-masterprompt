# Create Masterprompt — wersja polska

> Tłumaczenie `SKILL.md`. **Program czyta wyłącznie `SKILL.md`**, plik
> angielski — ten tutaj służy ludziom do czytania. Gdy oba się ze sobą nie
> zgadzają, obowiązuje wersja angielska. Stan: wersja 1.7.0.
>
> Nazwy plików, foldery i przykładowe polecenia celowo pozostały
> nieprzetłumaczone, bo tak właśnie nazywają się na dysku.
>
> Jedna strona do przejrzenia zamiast do przeczytania: [`docs/uebersicht-pl.png`](docs/uebersicht-pl.png)
> (wersja angielska: [`docs/uebersicht-en.png`](docs/uebersicht-en.png)).
>
> **Stan: wczesna publikacja.** Tekst był wielokrotnie sprawdzany pod kątem
> wewnętrznej spójności i zgodności ze specyfikacją, ale sam skill nie
> przeszedł jeszcze przez wiele prawdziwych, różnorodnych projektów. Jeśli
> coś w przebiegu, w bramce rozmiaru albo w którymś szablonie nie pasuje do
> własnego sposobu pracy, to cenny sygnał — warto zgłosić to jako Issue.

Masterprompt **nie** jest promptem z rolą. „Jesteś doświadczonym inżynierem,
pracuj dokładnie” nie dodaje nic, czego sprawny model i tak by nie robił.
Masterprompt to **pakiet kontekstu**: trwałe fakty, decyzje i granice jednego
projektu, spisane tak, żeby sesja bez żadnej historii rozmowy podjęła pracę
dokładnie tam, gdzie poprzednia się zatrzymała.

Ten skill buduje taki pakiet w sześciu fazach i oddaje trzy pliki.

## Co powstaje

| Plik | Po co | Czas życia |
|---|---|---|
| `BRIEFING.md` | Masterprompt. Kontekst, decyzje, anty-zakres, pułapki, aktualny stan. | Cały projekt |
| `DECISIONS.md` | Jedna linia na każdą rozstrzygniętą kwestię, z uzasadnieniem. Tylko dopisywanie, nigdy nadpisywanie. | Cały projekt |
| `HANDOFF_vNN.md` | Pisany przed limitem kontekstu. To, czego świeża sesja potrzebuje *właśnie teraz*. | Jedna sesja |

Nazwij je w języku użytkownika. Trzymaj je obok pracy, nie w czacie.

## Faza 0 — Bramka rozmiaru (najpierw, w dziesięć sekund)

Przepuszczanie skryptu do zmiany nazw przez sześć faz to sposób, w jaki ludzie
uczą się pomijać cały proces. Zaklasyfikuj, zanim zaczniesz:

- **S — jedno posiedzenie, odwracalne, bez niewiadomych.** Przejdź od razu do
  pracy. Pełną ścieżkę zaproponuj tylko wtedy, gdy projekt urośnie.
- **M — kilka sesji, trochę niewiadomych, jedno lub dwa prawdziwe
  rozwidlenia.** Fazy 1–3 i 5, plus 6, gdy tylko praca wykroczy poza jedną
  sesję. Plik briefingu, ale krótki. Bez osobnego dokumentu z planem.
- **L — wiele sesji, prawdziwa architektura, decyzje kosztowne do cofnięcia.**
  Wszystkie sześć faz.

Powiedz w jednym zdaniu, który rozmiar wybierasz i dlaczego. Jeśli użytkownik
się nie zgadza, powie to — kosztuje to jedną wiadomość, a oszczędza godzinę.

## Faza 1 — Research

Ustal, co już istnieje, gdzie jest luka, co jest technicznie wykonalne i które
pułapki są już udokumentowane. **Research odbywa się tylko tutaj.** Research
w środku budowy to sposób, w jaki budowa zamienia się w króliczą norę.

Wynik: raport z tabelą porównawczą, rekomendacją i źródłami.

**Przerwij, gdy spełnione są wszystkie trzy warunki** — nie wtedy, gdy skończy
się ciekawość:
1. Tabela porównawcza nie ma pustych komórek dla opcji z krótkiej listy.
2. Każda linia o pułapce ma źródło albo jest oznaczona jako założenie.
3. Dwa ostatnie wyszukiwania nie przyniosły nic nowego. To jest nasycenie.

Jeśli nie da się dojść do nasycenia, powiedz to i nazwij, co zostało otwarte.
Uczciwa luka bije pewne siebie zgadywanie, a użytkownik może zdecydować, czy
poświęcić więcej czasu.

## Faza 2 — Briefing

Skondensuj research do `BRIEFING.md` według `assets/template-briefing.md`.

Test dla tego pliku: **daj go świeżej sesji bez historii. Czy może pracować?**
Jeśli potrzebuje choć jednego pytania doprecyzowującego o coś, co już znasz,
briefing jest niekompletny. Przeczytaj go jak przeciwnik, zanim go pokażesz.

Sekcje obowiązkowe — dwie pierwsze to te, które ludzie pomijają, a potem
żałują:

- **Anty-zakres.** Wyraźne nie-cele, każdy z uzasadnieniem. „Bez szyfrowania
  w v1 — sejf jest wyłącznie lokalny, a zarządzanie kluczami podwoiłoby
  budowę.” Anty-zakres to najsilniejsza dostępna obrona przed rozrastaniem
  się zakresu, bo zamienia „a nie moglibyśmy po prostu…” w decyzję, którą
  trzeba ponownie otworzyć, zamiast w darmowy dodatek.
- **Rejestr założeń.** Wszystko, o czym decydujesz bez pytania. Po jednej
  linii na każde, oznaczonej tak, żeby dało się to później zakwestionować.
  Niezapisane założenia są niewidoczne, dopóki nie zaczną kosztować.
- Kontekst, ograniczenia, znane pułapki, aktualny stan.

## Faza 3 — Wywiad decyzyjny

O otwarte decyzje pytaj **pojedynczo**, czekając na odpowiedź, zanim zadasz
następne pytanie. Pytania zadane hurtem są przeglądane pobieżnie, a decyzja
przejrzana pobieżnie to zgadywanie, które nosi podpis użytkownika.

Na każde pytanie: 2–4 opcje, jedna wyraźna rekomendacja i jej uzasadnienie.
Zależności rozwiązuj po kolei — najpierw zdecyduj o stacku, potem o bibliotece,
która na nim działa.

**Sprawdzaj samodzielnie.** Jeśli fakt da się ustalić z plików, narzędzi albo
sieci, ustal go. Do użytkownika należą tylko prawdziwe wybory.

**Nie buduj niczego, zanim ta faza się nie zamknie.** Jeśli użytkownik w środku
wywiadu mówi „po prostu zacznij”: nazwij konkretne decyzje, które wciąż są
otwarte, zaproponuj, że podejmiesz je samodzielnie jako zapisane założenia,
i kontynuuj dopiero wtedy, gdy wybierze. Start z otwartymi rozwidleniami
oznacza poprawki, a poprawki kosztują więcej, niż kosztował wywiad.

Zakończ ponumerowanym podsumowaniem wszystkich decyzji. Dopisz je do dziennika
decyzji, który trzyma się `assets/template-decisions.md`.

## Faza 4 — Plan

Architektura, struktura repo albo folderów, plik konwencji, strategia testów,
kamienie milowe, Definition of Done dla każdego kamienia milowego i Definition
of Done dla projektu jako całości.

Kamienie milowe to **pionowe wycinki**: każdy wytwarza coś, co użytkownik może
faktycznie uruchomić, zobaczyć albo wykorzystać. Pięć kamieni milowych,
z których każdy dostarcza działający kawałek, bije trzy, które dostarczają
fundament, którego nikt nie może przetestować.

Pokaż plan do zatwierdzenia, zanim zaczniesz budować.

## Faza 5 — Budowa

Pracuj według wyraźnie nazwanego celu ze **sprawdzalnym warunkiem
zakończenia**. „Gotowe, gdy `npm test` przechodzi i aplikacja otwiera folder
sejfu” jest sprawdzalne. „Gotowe, gdy dobrze działa” — nie.

- Najpierw test, potem funkcja — tam, gdzie test ma sens.
- Małe commity, każdy z osobna możliwy do cofnięcia.
- Linting jako hook, nie jako przypomnienie.
- Bez przerw na pytanie o pozwolenie. Pytaj tylko przy prawdziwych
  rozwidleniach projektowych.

## Faza 6 — Handoff

Przed limitem kontekstu — nie po nim — napisz plik handoff (`HANDOFF_vNN.md`,
nazwany w języku użytkownika) na podstawie `assets/template-handoff.md`,
a potem uruchom świeżą sesję. Niekończące się kompaktowanie kontekstu gubi
dokładnie te szczegóły, których ustalenie było kosztowne.

Wyzwalacze: długie odcinki z dużą liczbą wywołań narzędzi, wielokrotne ponowne
czytanie tych samych plików albo użytkownik pytający drugi raz o coś, co już
było omówione.

## Runda ulepszeń

Na każdej granicy faz, **zanim** pokażesz wynik, przełącz się po cichu z roli
piszącego na rolę recenzenta. Trzy pytania:

1. **Czego brakuje?** Jakie pytanie musiałaby zadać świeża sesja, na które ten
   plik nie odpowiada?
2. **Co jest stwierdzone, a nie udowodnione?** Każde twierdzenie bez źródła
   albo oznaczenia jako założenie jest kandydatem.
3. **Co jest wypełniaczem?** Każde zdanie, które mogłoby stać w dowolnym innym
   projekcie, wylatuje.

Użytkownik widzi poprawiony wynik, nie krytykę. Wyjątek: jeśli runda wydobędzie
coś, co dotyka decyzji, to musi trafić przed oczy użytkownika.

Tworzenie i ocenianie to różne czynności. Piszący nie widzi luki, bo brakujący
element siedzi w jego głowie. Kosztuje mniej więcej 30 % fazy i zwraca więcej
niż cokolwiek innego w tym skillu.

Gdy kształt zadania wykracza poza „napisz mi X”, najpierw wczytaj
`references/prompt-techniques.md` — zawiera tabelę przypisania kształtu zadania
do techniki oraz sygnały ostrzegawcze nadmiernego promptowania.

## Reguła cofania

Decyzje bywają rewidowane. To normalne i tanie, **jeśli zrobi się to jak
należy**:

1. Zaktualizuj dziennik decyzji — dopisz nową linię, starą oznacz jako
   zastąpioną, zachowaj obie. Historia tłumaczy, dlaczego kod wygląda tak,
   jak wygląda.
2. Zaktualizuj `BRIEFING.md`, bo to właśnie czyta świeża sesja.
3. Nazwij, co ta zmiana unieważnia, zanim dotkniesz kodu.

Zmiana kursu tylko w czacie to tryb awarii: pliki nadal opisują stary projekt,
następna sesja im wierzy, a sprzeczność wychodzi na jaw trzy kroki później.

## Reguła wyjścia

Projekt, który przez trzy sesje niczego nie wytworzył, albo utknął, albo jest
martwy. Powiedz to wprost i zaproponuj trzy opcje: zmniejszyć zakres,
zaparkować go z napisanym plikiem handoff, żeby dało się go czysto wznowić,
albo porzucić. Pomysły są tanie; niedokończone projekty wymagają utrzymania.
To jedyne miejsce, w którym mówienie bez ogródek jest przysługą.

## Haczyki

Fakty o środowisku, które przeczą rozsądnym założeniom. Sprawdź je, zanim
zaczniesz obchodzić objaw.

- **Frontmatter skilli Anthropic przyjmuje dokładnie sześć kluczy**: `name`,
  `description`, `license`, `allowed-tools`, `metadata`, `compatibility`.
  Wszystko inne nie przechodzi walidacji przy wgrywaniu do claude.ai, mimo że
  Claude Code to toleruje. Skille po cichu działają lokalnie i psują się przy
  wgrywaniu.
- **Nazwa folderu musi być równa polu `name`** po normalizacji NFKC. Zmiana
  nazwy folderu bez zmiany frontmattera to najczęstsza awaria.
- **`name`: tylko małe litery, cyfry i myślniki.** Bez podkreśleń, bez
  podwójnych myślników, bez myślnika na początku ani na końcu. Maksymalnie
  64 znaki. `description` maksymalnie 1024.
- **Dwukropek bez cudzysłowu w `description` psuje parsowanie YAML.** „Use
  when: …” nie przechodzi. Ujmij w cudzysłów albo użyj skalara blokowego
  (`>-`).
- **Przy starcie sesji wczytywane są tylko `name` i `description`.** Treść
  wczytuje się dopiero przy wyzwoleniu. Dlatego każda wskazówka „kiedy tego
  użyć” musi trafić do description; warunek wyzwolenia zakopany w treści
  nigdy nie zostanie przeczytany na czas, żeby zadziałać.
- **Proste jednokrokowe prośby nie wyzwalają skilli**, niezależnie od jakości
  opisu, bo model obsługuje je bezpośrednio. Wyzwalanie testuj treściwymi,
  wielokrokowymi promptami.
- **Skille to instrukcje, nie egzekwowanie.** `allowed-tools` znosi pytania
  o uprawnienia; niczego nie ogranicza.

## Pliki referencyjne

Wczytuj je, gdy wymaga tego faza, nie z góry:

- `references/profile-questionnaire.md` — pola, które użytkownik wypełnia raz,
  żeby ten skill stał się jego własnym. Czytaj przy pierwszym użyciu albo gdy
  użytkownik chce wariantu osobistego.
- `references/quality-gates.md` — lista kontrolna dla każdej fazy. Czytaj
  przed zamknięciem którejkolwiek fazy.
- `references/anti-patterns.md` — tryby awarii wraz z ich naprawami. Czytaj,
  gdy projekt grzęźnie, kręci się w kółko albo generuje poprawki.
- `references/model-routing.md` — która klasa modelu pasuje do której fazy.
  Czytaj, gdy użytkownikowi zależy na wyborze modelu albo na kosztach.
- `references/prompt-techniques.md` — przypisanie kształtu zadania do
  techniki, plus sygnały ostrzegawcze nadmiernego promptowania. Czytaj, gdy
  faza nie dostarcza, artefakt wydaje się cienki albo zadanie wykracza poza
  „napisz mi X”.

Szablony w `assets/` są do kopiowania i wypełniania, nie do parafrazowania.
Struktury odwzorowuje się pewniej niż prozatorskie opisy struktur.

## Zasady domowe

Kształtują każdą odpowiedź, dopóki skill jest aktywny:

- **Odpowiadaj w języku użytkownika**, także w generowanych plikach. Ten skill
  jest napisany po angielsku; jego wynik — nie.
- **Jeden kęs wiedzy na odpowiedź.** Dwa do czterech zdań o tym, *dlaczego*,
  nie co. Chodzi o to, żeby użytkownik mógł poprowadzić następny projekt bez
  ciebie.
- **Jakość ponad oszczędność przy wyborze modelu.** Nigdy nie schodź do
  tańszego modelu, gdy ten bardziej zdolny daje lepszy wynik. Tańszy jest
  właściwy tylko wtedy, gdy wynik jest równoważny. W razie wątpliwości zostań
  przy mocniejszym modelu i powiedz to.
- **Nigdy nie zgaduj tam, gdzie błąd jest kosztowny.** Literówka w odpowiedzi
  nie kosztuje nic. Literówka w nazwie pliku, identyfikatorze, formacie danych
  albo commicie kosztuje popołudnie. Poprawiaj po cichu, gdy właściwa wersja
  jest oczywista; pytaj, gdy nie jest.
- **Niejasne skróty: pytaj, nie zgaduj.** Podaj powszechne rozwinięcie, jeśli
  takie istnieje. Błędne zgadnięcie tutaj się kumuluje — trzy kroki później
  dźwiga już ciężar i jest kosztowne do odkręcenia.
- **Wypowiadaj założenia na głos.** Jeśli nie masz pewności, czy twoje
  założenie się utrzyma, powiedz to, zamiast sprzedawać je jako fakt.
- **Żadnych wiszących pytań po skończonym zadaniu.** Żadnego „coś jeszcze?”,
  żadnego menu opcji na zakończenie. Jeśli użytkownik chce więcej, powie to.
