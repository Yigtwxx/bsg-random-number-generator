# Collatz Tabanlı Rastgele Sayı Üreteci (Collatz RNG)

## 1) Amaç
Bu çalışmanın amacı, matematikte iyi bilinen **Collatz (3n + 1) problemi**nin kaotik davranışını kullanarak
bir **pseudo-random number generator (PRNG)** tasarlamak ve bu üretecin temel istatistiksel davranışlarını
incelemektir. Algoritma, başlangıç tohumu (seed) ile başlar ve Collatz dönüşümleri üzerinden iç durumu
güncelleyerek rastgele sayı üretir.

## 2) Girdi / Çıktı
### Girdiler
- **seed (opsiyonel):** Başlangıç tohumu. Verilmediği durumda sistem zamanı (milisaniye) kullanılır.
- **a, b:** Üretilmek istenen rastgele sayının alt ve üst sınırları.

### Çıktılar
- **next_int():** Collatz adımından sonra oluşan ham iç durum değeri.
- **randint(a, b):** [a, b] aralığında üretilen rastgele tam sayı.
- **random():** [0, 1) aralığında normalize edilmiş rastgele ondalık sayı.

## 3) Sözde Kod (Pseudocode)

ALGORİTMA CollatzRNG  
GİRDİ: seed (opsiyonel)  
ÇIKTI: Rastgele sayı dizisi  

BAŞLAT:  
- Eğer seed yoksa: seed ← sistem zamanı  
- state ← seed  
- steps_taken ← 0  

FONKSİYON STEP():  
- Eğer state ≤ 1 ise:  
  - state ← (state + seed + steps_taken + SABİT) × 1664525  
- Eğer state çift ise:  
  - state ← state / 2  
- Aksi halde:  
  - state ← 3 × state + 1  
- steps_taken ← steps_taken + 1  
- state’i döndür  

FONKSİYON RANDINT(a, b):  
- range_size ← b − a + 1  
- STEP() fonksiyonunu 3 kez çağır  
- val ← son state  
- a + (val mod range_size) değerini döndür  

SON

## 4) Çalışma Mantığı (4 Ana Sütun)

Bu algoritmanın çalışma prensibi dört temel yapı üzerine kuruludur:

### 1. Başlangıç / Tohumlama
Algoritma bir **seed** değeri ile başlar. Seed, kullanıcı tarafından verilmezse sistem saatine bağlı olarak
üretilir. Bu durum her çalıştırmada farklı bir başlangıç durumu sağlar.

### 2. Ana Motor (Collatz Dönüşümü)
İç durum her adımda Collatz kuralına göre güncellenir:
- Çift sayılar 2’ye bölünür.
- Tek sayılar için 3n + 1 işlemi uygulanır.
Bu dönüşüm deterministik olmasına rağmen karmaşık ve öngörülmesi zor bir davranış sergiler.

### 3. Tuzak Önleme (Kick Mekanizması)
Collatz dizisinin 4 → 2 → 1 döngüsüne sıkışmasını önlemek için,
durum 1 veya daha küçük olduğunda **seed, adım sayacı ve sabit bir sayı** ile karıştırılarak
yeni bir kaotik yörüngeye sıçrama yapılır.

### 4. Karıştırma / Korelasyon Azaltma
Tek bir Collatz adımı ardışık değerler arasında yüksek korelasyon oluşturabileceği için,
`randint()` fonksiyonu içinde **art arda üç adım** uygulanarak dağılımın daha dengeli olması sağlanır.

## 5) Parametreler ve Seçimler
- **seed:** Üretecin deterministik veya zamana bağlı çalışmasını belirler.
- **steps_taken:** Tuzak önleme ve çeşitlilik sağlamak için kullanılır.
- **Sabit çarpan (1664525):** Lineer karıştırma etkisi sağlayarak durum uzayını genişletir.

## 6) Karmaşıklık Analizi
- **Zaman Karmaşıklığı:** O(1) (Her rastgele sayı üretimi sabit sayıda işlem içerir)
- **Bellek Karmaşıklığı:** O(1) (Sabit sayıda değişken kullanılır)

## 7) Test ve Analiz (Demo Programı)

Algoritmanın davranışını incelemek için `demo.py` dosyası kullanılmıştır.

### Test Kurulumu
- Örneklem boyutu: 1000
- Aralık: [0, 99]

### İstatistiksel Özet
- Ortalama (Mean): ≈ 49.5 (beklenen değere yakındır)
- Medyan (Median): Orta değere yakın
- Standart Sapma: Dengeli bir yayılım göstermektedir

Histogram çıktısı, üretilen sayıların aralık boyunca yaklaşık olarak dengeli dağıldığını göstermektedir.

## 8) Kullanım

```python
from collatz_rng import CollatzRNG

rng = CollatzRNG(seed=12345)

print(rng.randint(0, 100))
print(rng.random())
````

Demo çalıştırmak için:

```bash
python demo.py
```

## 9) Sınırlamalar ve Güvenlik Notu

* Bu algoritma **kriptografik olarak güvenli değildir**.
* Amaç; matematiksel kaos ve deterministik kurallardan rastgelelik üretimini göstermektir.
* Kriptografik uygulamalarda kullanılmamalıdır.

## 10) Sonuç

Bu çalışmada Collatz problemi tabanlı bir rastgele sayı üreteci geliştirilmiş,
basit istatistiksel testlerle davranışı incelenmiştir.
Algoritma eğitimsel ve deneysel amaçlar için uygun olup,
kaotik sistemlerin rastgelelik üretimindeki rolünü göstermektedir.



<img width="640" height="800" alt="image" src="https://github.com/user-attachments/assets/e5c58ec1-336a-43cc-a843-ce89f7a07a0a" />
