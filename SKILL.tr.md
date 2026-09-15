# Create Masterprompt — Türkçe sürüm

> `SKILL.md` dosyasının çevirisi. **Program yalnızca `SKILL.md` dosyasını
> okur**, yani İngilizce olanı — bu dosya insanların okuması içindir. İkisi
> çelişirse İngilizce olan geçerlidir. Sürüm 1.7.0 itibarıyla günceldir.
>
> Dosya adları, klasörler ve örnek komutlar bilerek çevrilmedi; diskte bu
> adlarla duruyorlar.
>
> Baştan sona okumak yerine tek bakışta görmek için bir sayfa: [`docs/uebersicht-tr.png`](docs/uebersicht-tr.png)
> (İngilizce sürüm: [`docs/uebersicht-en.png`](docs/uebersicht-en.png)).
>
> **Durum: erken yayın.** Metin, iç tutarlılık ve spesifikasyona uygunluk
> açısından birkaç kez denetlendi; ancak skill'in kendisi henüz çok sayıda
> gerçek ve birbirinden farklı projede çalışmadı. Akışta, boyut kapısında ya da
> bir şablonda kendi çalışma biçimine uymayan bir şey varsa, bu yararlı bir
> sinyaldir — Issue olarak bildir.

Masterprompt bir rol promptu **değildir**. “Sen kıdemli bir mühendissin, titiz
çalış” cümlesi, yetkin bir modelin zaten yapmadığı hiçbir şey eklemez.
Masterprompt bir **bağlam paketidir**: bir projenin kalıcı gerçekleri,
kararları ve sınırları; geçmişi sıfır olan bir oturumun tam olarak öncekinin
bıraktığı yerden devam edebileceği biçimde yazılmış.

Bu skill o paketi altı aşamada kurar ve geriye üç dosya verir.

## Ne üretirsin

| Dosya | Amaç | Ömrü |
|---|---|---|
| `BRIEFING.md` | Masterprompt. Bağlam, kararlar, anti-scope, tuzaklar, güncel durum. | Projenin tamamı |
| `DECISIONS.md` | Karara bağlanan her soru için tek satır, gerekçesiyle. Yalnızca sonuna eklenir. | Projenin tamamı |
| `HANDOFF_vNN.md` | Bağlam sınırından önce yazılır. Taze bir oturumun *tam şu anda* neye ihtiyacı olduğu. | Tek oturum |

Bunları kullanıcının dilinde adlandır. İşin yanında tut, sohbetin içinde
değil.

## Aşama 0 — Boyut kapısı (önce bunu yap, on saniyede)

Bir yeniden adlandırma betiğine altı aşama uygulamak, insanların süreci tümden
atlamayı öğrendiği yoldur. Başlamadan önce sınıflandır:

- **S — tek oturum, geri alınabilir, bilinmeyen yok.** Doğrudan işe geç. Tam
  akışı yalnızca iş büyürse öner.
- **M — birkaç oturum, bazı bilinmeyenler, bir iki gerçek yol ayrımı.** Aşama
  1–3 ve 5; iş tek oturumu aşar aşmaz 6 da. Briefing dosyası var, ama kısa.
  Ayrı bir plan belgesi yok.
- **L — çok oturumlu, gerçek mimari, geri alması pahalı kararlar.** Altı
  aşamanın tamamı.

Hangi boyutu seçtiğini ve nedenini tek cümleyle söyle. Kullanıcı aynı fikirde
değilse söyler — bu bir mesaja mal olur, bir saat kazandırır.

## Aşama 1 — Araştırma

Neyin zaten var olduğunu, boşluğun nerede olduğunu, teknik olarak neyin
yapılabilir olduğunu ve hangi tuzakların zaten belgelenmiş olduğunu bul.
**Araştırma yalnızca burada yapılır.** İnşanın ortasında araştırma, bir inşanın
dipsiz kuyuya dönüşme yoludur.

Çıktı: karşılaştırma tablosu, bir öneri ve kaynaklar içeren bir rapor.

**Üçü birden doğru olduğunda dur** — merakın tükendiğinde değil:
1. Kısa listedeki seçenekler için karşılaştırma tablosunda boş hücre kalmadı.
2. Her tuzak satırının bir kaynağı var ya da varsayım olarak işaretlenmiş.
3. Son iki arama yeni bir şey getirmedi. Doygunluk budur.

Doygunluğa ulaşamıyorsan bunu söyle ve neyin açık kaldığını adlandır. Dürüst bir
boşluk, kendinden emin bir tahmini yener; daha fazla zaman harcayıp
harcamamaya da kullanıcı karar verebilir.

## Aşama 2 — Briefing

Araştırmayı, `assets/template-briefing.md` şablonunu kullanarak `BRIEFING.md`
dosyasına sıkıştır.

Bu dosyanın sınavı: **geçmişi olmayan taze bir oturuma ver. Çalışabiliyor mu?**
Senin zaten bildiğin bir şey hakkında tek bir açıklayıcı soruya bile ihtiyaç
duyuyorsa briefing eksiktir. Göstermeden önce kusur arar gibi baştan oku.

Zorunlu bölümler — ilk ikisi, insanların atlayıp sonra pişman olduğu
bölümlerdir:

- **Anti-scope.** Açıkça belirtilmiş hedef-dışı maddeler, her birinin
  gerekçesiyle. “v1'de şifreleme yok — kasa yalnızca yerel, anahtar yönetimi ise
  inşayı ikiye katlardı.” Anti-scope, kapsam kaymasına karşı eldeki en güçlü
  savunmadır; çünkü “şunu da ekleyiversek…” cümlesini bedava bir ekleme
  olmaktan çıkarıp yeniden açılması gereken bir karara dönüştürür.
- **Varsayım kaydı.** Sormadan karar verdiğin her şey. Her biri tek satır,
  sonradan sorgulanabilsin diye işaretli. Kayda geçmemiş varsayımlar,
  pahalıya patlayana kadar görünmezdir.
- Bağlam, kısıtlar, bilinen tuzaklar, güncel durum.

## Aşama 3 — Karar görüşmesi

Açık kararları **teker teker** sor; bir sonrakine geçmeden yanıtı bekle. Toplu
sorular üstünkörü okunur; üstünkörü okunmuş bir karar ise kullanıcının imzasını
taşıyan bir tahmindir.

Soru başına: 2–4 seçenek, tek bir net öneri ve gerekçesi. Bağımlılıkları
sırayla çöz — önce teknoloji yığınını, sonra üzerinde çalışacak kütüphaneyi
kararlaştır.

**Bulunabilecek olanı kendin bul.** Bir gerçek dosyalardan, araçlardan ya da
web'den öğrenilebiliyorsa öğren. Kullanıcıya yalnızca gerçek seçimler düşer.

**Bu aşama kapanmadan hiçbir şey inşa etme.** Kullanıcı görüşmenin ortasında
“hadi başla” derse: hâlâ açık olan kararları tek tek adlandır, bunları kayıtlı
varsayım olarak kendin almayı öner ve yalnızca kullanıcı seçtikten sonra devam
et. Açık yol ayrımlarıyla başlamak yeniden yapma demektir; yeniden yapma ise
görüşmeden daha pahalıya mal olur.

Tüm kararların numaralı bir özetiyle kapat. Bunu, `assets/template-decisions.md`
şablonunu izleyen karar günlüğüne ekle.

## Aşama 4 — Plan

Mimari, repo ya da klasör yapısı, kurallar dosyası, test stratejisi, kilometre
taşları, her kilometre taşı için bir bitti tanımı (Definition of Done) ve
projenin bütünü için bir bitti tanımı.

Kilometre taşları **dikey dilimlerdir**: her biri, kullanıcının gerçekten
çalıştırabileceği, görebileceği ya da kullanabileceği bir şey üretir. Her biri
çalışan küçük bir parça teslim eden beş kilometre taşı, kimsenin test
edemeyeceği bir temel teslim eden üçünü yener.

İnşaya başlamadan önce planı onaya sun.

## Aşama 5 — İnşa

Açıkça belirtilmiş bir hedefe karşı, **denetlenebilir bir durma koşuluyla**
çalış. “`npm test` geçtiğinde ve uygulama kasa klasörünü açtığında bitti”
denetlenebilir. “İyi çalıştığında bitti” değildir.

- Testin anlamlı olduğu yerde önce test, sonra özellik.
- Küçük commit'ler, her biri tek başına geri alınabilir.
- Linting bir hook olarak, hatırlatma olarak değil.
- İzin istemek için durmak yok. Yalnızca gerçek tasarım yol ayrımlarında sor.

## Aşama 6 — Devir teslim

Bağlam sınırından önce — sonra değil — devir teslim dosyasını (`HANDOFF_vNN.md`,
kullanıcının dilinde adlandırılmış) `assets/template-handoff.md` şablonundan
yaz, ardından taze bir oturum başlat. Sonu gelmeyen sıkıştırma, tam da elde
edilmesi pahalı olan ayrıntıları kaybettirir.

Tetikleyiciler: uzun, araç ağırlıklı dönemler; aynı dosyaların tekrar tekrar
okunması; ya da kullanıcının zaten ele alınmış bir şeyi ikinci kez sorması.

## İyileştirme turu

Her aşama sınırında, sonucu göstermeden **önce**, sessizce yazar rolünden
gözden geçiren rolüne geç. Üç soru:

1. **Ne eksik?** Taze bir oturumun sormak zorunda kalacağı ve bu dosyanın
   yanıtlamadığı soru hangisi?
2. **Ne kanıtlanmak yerine yalnızca iddia edilmiş?** Kaynağı ya da varsayım
   işareti olmayan her iddia adaydır.
3. **Ne dolgu?** Başka herhangi bir projede de yer alabilecek her cümle gider.

Kullanıcı eleştiriyi değil, gözden geçirilmiş sonucu görür. İstisna: tur bir
karara dokunan bir şey ortaya çıkarırsa, o kullanıcının önüne konur.

Üretmek ve değerlendirmek farklı etkinliklerdir. Yazar boşluğu göremez, çünkü
eksik parça onun kafasındadır. Aşamanın kabaca %30'una mal olur ve bu skill'deki
her şeyden daha fazlasını geri getirir.

Görevin biçimi “bana X yaz”ın ötesine geçiyorsa önce
`references/prompt-techniques.md` dosyasını yükle — görev biçiminden tekniğe
yönlendirme tablosu ve aşırı promptlamanın uyarı işaretleri orada.

## Geri sarma kuralı

Kararlar gözden geçirilir. Bu normaldir ve **doğru ele alınırsa** ucuzdur:

1. Karar günlüğünü güncelle — yeni satırı ekle, eskisini geçersiz kılınmış
   olarak işaretle, ikisini de tut. Kodun neden öyle göründüğünü geçmiş
   açıklar.
2. `BRIEFING.md` dosyasını güncelle; taze bir oturumun okuduğu şey odur.
3. Koda dokunmadan önce değişikliğin neyi geçersiz kıldığını adlandır.

Rotayı yalnızca sohbette değiştirmek asıl hata biçimidir: dosyalar hâlâ eski
projeyi anlatır, bir sonraki oturum onlara inanır ve çelişki üç adım sonra su
yüzüne çıkar.

## Çıkış kuralı

Üç oturumda hiçbir şey üretmemiş bir proje ya takılmıştır ya da ölmüştür. Bunu
açıkça söyle ve üç seçenek sun: kapsamı küçült, temiz biçimde yeniden ele
alınabilsin diye yazılı bir devir teslimle askıya al ya da bırak. Fikirler
ucuzdur; yarım kalmış projelerin bakım maliyeti vardır. Burası, açık sözlü
olmanın kullanıcıya yapılan asıl hizmet olduğu tek yerdir.

## Gotchas

Makul varsayımlara ters düşen ortam gerçekleri. Bir belirtinin etrafından
dolaşmadan önce bunlara bak.

- **Anthropic skill frontmatter'ı tam olarak altı anahtar kabul eder**: `name`,
  `description`, `license`, `allowed-tools`, `metadata`, `compatibility`.
  Bunların dışındaki her şey, Claude Code hoş görse bile claude.ai'ye yüklemede
  doğrulamadan geçmez. Skill'ler yerelde sessizce çalışır, yüklemede bozulur.
- **Klasör adı `name` alanıyla aynı olmalıdır** — NFKC normalleştirmesinden
  sonra. Frontmatter'a dokunmadan klasörü yeniden adlandırmak en yaygın bozulma
  nedenidir.
- **`name`: yalnızca küçük harf, rakam ve tire.** Alt çizgi yok, ardışık tire
  yok, başta ya da sonda tire yok. En fazla 64 karakter. `description` en fazla
  1024.
- **`description` içinde tırnaksız bir iki nokta YAML ayrıştırmasını bozar.**
  “Use when: …” başarısız olur. Tırnak içine al ya da blok skaler (`>-`) kullan.
- **Oturum başlangıcında yalnızca `name` + `description` yüklenir.** Gövde,
  tetiklenince yüklenir. Bu yüzden her “bunu ne zaman kullanmalı” ipucu
  description'a aittir; gövdeye gömülü bir tetikleme koşulu, tetiklemeye
  yetişecek zamanda asla okunmaz.
- **Basit tek adımlı istekler skill tetiklemez**, description ne kadar iyi
  olursa olsun, çünkü model bunları doğrudan halleder. Tetiklemeyi içerikli,
  çok adımlı prompt'larla test et.
- **Skill'ler talimattır, zorlama değil.** `allowed-tools` izin sorularını
  kaldırır; hiçbir şeyi kısıtlamaz.

## Referans dosyaları

Bunları aşama gerektirdiğinde yükle, baştan değil:

- `references/profile-questionnaire.md` — kullanıcının bu skill'i kendine ait
  kılmak için bir kez doldurduğu alanlar. İlk kullanımda ya da kullanıcı
  kişisel bir sürüm istediğinde oku.
- `references/quality-gates.md` — aşama başına kontrol listesi. Herhangi bir
  aşamayı kapatmadan önce oku.
- `references/anti-patterns.md` — hata biçimleri ve çözümleri. Bir proje
  tıkandığında, döngüye girdiğinde ya da yeniden yapma ürettiğinde oku.
- `references/model-routing.md` — hangi model sınıfının hangi aşamaya uyduğu.
  Kullanıcı model seçimini ya da maliyeti önemsediğinde oku.
- `references/prompt-techniques.md` — görev biçiminden tekniğe yönlendirme,
  artı aşırı promptlama uyarı işaretleri. Bir aşama sonuç vermediğinde, bir
  çıktı zayıf göründüğünde ya da görev “bana X yaz”ın ötesine geçtiğinde oku.

`assets/` altındaki şablonlar kopyalanıp doldurulmak içindir, kendi
sözcüklerinle yeniden yazılmak için değil. Yapılar, yapıların düzyazı
tarifinden daha güvenilir biçimde tutturulur.

## Ev kuralları

Skill etkin olduğu sürece bunlar her yanıtı biçimlendirir:

- **Kullanıcının dilinde yanıt ver**, üretilen dosyalar dahil. Bu skill
  İngilizce yazılmıştır; çıktısı değil.
- **Yanıt başına bir öğrenme lokması.** Ne üzerine değil, *neden* üzerine iki
  ila dört cümle. Amaç, kullanıcının bir sonraki projeyi sensiz yürütebilmesi.
- **Model seçiminde tasarruf değil, kalite.** Daha yetkin model daha iyi sonuç
  veriyorsa asla daha ucuz modele inme. Daha ucuzu yalnızca sonuç eşdeğer
  olduğunda doğrudur. Emin değilsen üstte kal ve bunu söyle.
- **Hatanın pahalı olduğu yerde asla tahmin etme.** Bir yanıttaki yazım hatası
  hiçbir şeye mal olmaz. Bir dosya adındaki, tanımlayıcıdaki, veri biçimindeki
  ya da commit'teki yazım hatası bir öğleden sonraya mal olur. Doğrusu
  apaçıksa sessizce düzelt; değilse sor.
- **Belirsiz kısaltmalar: sor, tahmin etme.** Yaygın bir açılımı varsa onu
  söyle. Buradaki yanlış bir tahmin katlanarak büyür — üç adım sonra yük
  taşır hâle gelir ve geri çözmesi pahalıdır.
- **Varsayımları açıkça dile getir.** Varsayımının geçerli olduğundan emin
  değilsen, onu gerçekmiş gibi satmak yerine bunu söyle.
- **Görev bittiğinde arkada soru bırakma.** “Başka bir şey?” yok, kapanışta
  seçenek menüsü yok. Kullanıcı daha fazlasını isterse söyler.
