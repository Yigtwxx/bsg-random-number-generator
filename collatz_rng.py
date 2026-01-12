import time

class CollatzRNG:
    """
    Collatz sanısına (3n + 1) dayanan sahte rastgele sayı üreticisi (PRNG).
    """
    def __init__(self, seed=None):
        # Eğer bir tohum (seed) değeri verilmezse, o anki zamanı milisaniye cinsinden kullanırız.
        if seed is None:
            seed = int(time.time() * 1000)
        self.seed = seed
        self.state = seed
        # 4-2-1 döngüsüne sık girilirse çeşitliliği sağlamak için kullanılan bir sayaç.
        self.steps_taken = 0

    def _next_collatz(self, n):
        """Referans/kullanım için standart Collatz adımı."""
        # Eğer sayı çift ise 2'ye böl.
        if n % 2 == 0:
            return n // 2
        else:
            # Eğer sayı tek ise 3 ile çarp ve 1 ekle.
            return 3 * n + 1

    def _step(self):
        """
        Dahili durumu (state) Collatz mantığını kullanarak ilerletir.
        Eğer 4-2-1 döngüsüne girersek (durum 1'e ulaşırsa) bir 'tekme' (kick) mekanizması içerir.
        """
        if self.state <= 1:
            # Tuzaktan kaçınma: Eğer 1'e ulaşırsak, yeni kaotik bir yörüngeye atlamak için
            # bitleri tohum (seed) ve adım sayacı ile karıştırırız.
            # 0xDEADBEEF: Rastgeleliği artırmak için kullanılan yaygın bir "sihirli sayı".
            # 1664525: Doğrusal Eşlik Üreteçlerinde (LCG) yaygın kullanılan bir çarpan.
            self.state = (self.state + self.seed + self.steps_taken + 0xDEADBEEF) * 1664525
        
        # Collatz kuralını uygula: Çift ise yarısı, tek ise 3k+1.
        if self.state % 2 == 0:
            self.state = self.state // 2
        else:
            self.state = 3 * self.state + 1
        
        self.steps_taken += 1
        return self.state

    def next_int(self):
        """Mevcut durum tam sayısını ham olarak döndürür."""
        return self._step()

    def randint(self, a, b):
        """
        a <= N <= b olacak şekilde rastgele bir N tam sayısı döndürür.
        Tüm yapı üzerinde modül (mod) işlemi yapmak yerine, daha iyi dağılım özellikleri için
        durumun alt bitlerini kullanmayı hedefler (burada basitçe mod kullanılsa da, adım sayısı ile karıştırma yapılır).
        """
        range_size = b - a + 1
        if range_size <= 0:
            raise ValueError("Boş aralık (Empty range)")
        
        # Tekli Collatz adımları ilişkili olduğundan (örn. n -> 3n+1 her zaman büyür, n -> n/2 her zaman küçülür),
        # daha iyi "karıştırma" sağlamak için durumu birden fazla kez ilerletiyoruz.
        # Anlık korelasyonu (ilişkiyi) kaybetmek için her sayı üretiminde 3 adım atıyoruz.
        self._step()
        self._step()
        val = self._step()
        
        # Sonucu istenilen aralığa (a ve b arasına) sığdırmak için modül işlemi ve ofset ekleme.
        return a + (val % range_size)

    def random(self):
        """
        [0.0, 1.0) aralığında bir sonraki rastgele kayan noktalı sayıyı (float) döndürür.
        """
        # Büyük bir tam sayı üret ve bunu normalleştir (0 ile 1 arasına sıkıştır).
        val = self.randint(0, 10**9)
        return val / (10**9 + 1.0)

if __name__ == "__main__":
    # Hızlı kendi kendine test (Self-test) bloğu
    rng = CollatzRNG(seed=12345)
    print("İlk 10 sayı [0, 100]:")
    for _ in range(10):
        # 0 ile 100 arasında rastgele tam sayılar üret ve yan yana yazdır.
        print(rng.randint(0, 100), end=" ")
    print("\n")
