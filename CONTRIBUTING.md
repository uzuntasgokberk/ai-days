# Katkı

Teşekkürler. Bu repo tek kişi tarafından yürütülüyor; süreç kısa ve sabit.

## Önce issue, pull request davetle

- **Issue aç:** yanlış bir tarih, sayı, isim ya da kaynak için [Düzeltme](.github/ISSUE_TEMPLATE/duzeltme.md);
  bir sonraki bölüme girmesini istediğin bir gelişme için [Gündem önerisi](.github/ISSUE_TEMPLATE/gundem-onerisi.md);
  geri kalan her şey için [Soru](.github/ISSUE_TEMPLATE/soru.md).
- **Pull request'ler davetle.** Düzeltme issue'da kabul edilirse senden bir pull request istenir; davetsiz pull request
  issue'ya yönlendirilerek kapatılır.
- **Kişisel veri ya da yanlışlıkla paylaşılmış bir bilgi** asla issue'ya yazılmaz: [SECURITY.md](SECURITY.md).

## Bir kart nasıl doğrulanır

- Tarih, duyuru tarihidir (ABD saati).
- @uzuntasgokberk paylaşımları dışındaki her kart, resmi sayfa ve en az iki haber kaynağıyla doğrulanır; kaynaklar
  kartın altında yazar.
- Resmi kaynakla teyit edilmemiş bir bilgi kartta "henüz doğrulanmadı" diye işaretlenir.
- Gündem önerisi en az bir resmi kaynak ve bir haber kaynağıyla gelir; öneri, kartın kaynak kuralını karşılarsa girer.

## Değişiklik nasıl yapılır

- Her bölüm kendi klasöründe: `bolumler/<iki haneli no>-<dönem>/`, içinde `README.md`, PDF ve `onizleme.png`.
  Yayınlanmış bir bölümün klasör ve dosya adı değişmez; dışarıdan verilen linkler onlara bağlı.
- PDF düzeltmesi yeni PDF olarak aynı adla gelir; düzeltme, bölüm README'sinin sonundaki notta tarihiyle yazılır.
- Markdown dosyaları 500 satırın altında kalır.
- Commit'ler Conventional Commits biçiminde (`feat(bolum-08): ...`, `fix(bolum-07): ...`, `docs: ...`).
- Katkılar repo lisansıyla, CC BY 4.0 ve [NOTICE](NOTICE)'taki atıf koşuluyla paylaşılır.

## Kontrolleri yerelde çalıştır

```sh
python3 scripts/kontrol.py
```

Her bölüm klasöründe README, tek PDF ve önizleme olduğunu, PDF'lerin 50 MB'ı geçmediğini, PDF'lerde yerel dosya yolu
gömülü olmadığını ve Markdown'daki göreli linklerin var olan dosyalara gittiğini kontrol eder. CI aynı betiği çalıştırır.
