from collatz_rng import CollatzRNG
import time
import statistics

# ANSI Renk Kodları (Terminalde renkli çıktı almak için)
class Colors:
    HEADER = '\033[95m'  # Başlık rengi (Mor)
    BLUE = '\033[94m'    # Mavi
    CYAN = '\033[96m'    # Camgöbeği (Cyan)
    GREEN = '\033[92m'   # Yeşil
    WARNING = '\033[93m' # Uyarı rengi (Sarı)
    FAIL = '\033[91m'    # Hata rengi (Kırmızı)
    ENDC = '\033[0m'     # Renk sıfırlama (Normal)
    BOLD = '\033[1m'     # Kalın yazı
    UNDERLINE = '\033[4m'# Altı çizili

def print_header(title):
    """Verilen başlığı şık bir çerçeve içinde yazdırır."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD} {title.center(58)} {Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}\n")

def print_histogram(data, buckets=10, width=40):
    """
    Verilen veri listesi için bir histogram (dağılım grafiği) çizer.
    buckets: Kaç adet aralık (sütun) olacağı.
    width: Çubukların maksimum karakter genişliği.
    """
    if not data:
        return
    
    print(f"{Colors.CYAN}{Colors.BOLD}>> Dağılım Analizi (Aralık 0-99){Colors.ENDC}")
    
    counts = [0] * buckets
    range_limit = 100
    bucket_size = range_limit // buckets
    
    # Verileri uygun kutulara (buckets) yerleştir
    for x in data:
        idx = min(x // bucket_size, buckets - 1)
        counts[idx] += 1
        
    max_count = max(counts)
    # Ölçekleme faktörü: En uzun çubuğun 'width' kadar olmasını sağlar
    scale = width / max_count if max_count > 0 else 1
    
    print(f"{Colors.BOLD}{'Aralık':<12} | {'Adet':<8} | {'Frekans Grafiği'}{Colors.ENDC}")
    print(f"{'-'*13}|{'-'*10}|{'-'*45}")
    
    for i in range(buckets):
        start = i * bucket_size
        end = (i + 1) * bucket_size - 1
        count = counts[i]
        
        # Çubuk rengini sayıya göre belirle (Görsellik amaçlı: Pozitifse yeşil, 0 ise kırmızı)
        bar_color = Colors.GREEN if count > 0 else Colors.FAIL
        bar = f"{bar_color}{'█' * int(count * scale)}{Colors.ENDC}"
        
        # Yüzdeyi hesapla
        percent = (count / len(data)) * 100
        
        print(f"{start:02d}-{end:02d}        | {count:<4} ({percent:4.1f}%) | {bar}")
    print(f"{'-'*70}\n")

def main():
    print_header("Collatz Sanısı RNG Demosu")

    print(f"{Colors.BLUE}[*] Jeneratör Başlatılıyor...{Colors.ENDC}")
    rng = CollatzRNG() 
    print(f"{Colors.GREEN}[+] Jeneratör Hazır!{Colors.ENDC}")
    print(f"    Tohum (Seed): {Colors.WARNING}{rng.seed}{Colors.ENDC}")
    
    sample_size = 1000
    print(f"\n{Colors.BLUE}[*] {sample_size} rastgele sayı üretiliyor (0-99)...{Colors.ENDC}")
    
    start_time = time.time()
    # 0 ile 99 arasında 1000 adet rastgele sayı üret
    data = [rng.randint(0, 99) for _ in range(sample_size)]
    duration = time.time() - start_time
    
    print(f"{Colors.GREEN}[+] Üretim Tamamlandı: {duration:.4f} saniye.{Colors.ENDC}\n")

    # İstatistikler
    mean = statistics.mean(data)       # Ortalama
    median = statistics.median(data)   # Ortanca
    mode = statistics.mode(data)       # Tepe Değer (En sık tekrar eden)
    stdev = statistics.stdev(data)     # Standart Sapma
    
    print(f"{Colors.CYAN}{Colors.BOLD}>> İstatistiksel Özet{Colors.ENDC}")
    print(f"    Örnek Veri: {Colors.WARNING}{data[:10]}...{Colors.ENDC}")
    print(f"    Ortalama: {mean:.2f} (Beklenen ~49.5)")
    print(f"    Ortanca:  {median:.2f}")
    print(f"    Mod:      {mode}")
    print(f"    Std Sapma:{stdev:.2f}\n")
    
    # Histogramı çizdir
    print_histogram(data)
    
    print(f"{Colors.HEADER}Kaosu modellediğiniz için teşekkürler!{Colors.ENDC}\n")

if __name__ == "__main__":
    main()
