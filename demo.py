from collatz_rng import CollatzRNG
import time
import statistics

# ANSI Colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(title):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD} {title.center(58)} {Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}\n")

def print_histogram(data, buckets=10, width=40):
    if not data:
        return
    
    print(f"{Colors.CYAN}{Colors.BOLD}>> Distribution Analysis (Range 0-99){Colors.ENDC}")
    
    counts = [0] * buckets
    range_limit = 100
    bucket_size = range_limit // buckets
    
    for x in data:
        idx = min(x // bucket_size, buckets - 1)
        counts[idx] += 1
        
    max_count = max(counts)
    scale = width / max_count if max_count > 0 else 1
    
    print(f"{Colors.BOLD}{'Range':<12} | {'Count':<8} | {'Frequency Graph'}{Colors.ENDC}")
    print(f"{'-'*13}|{'-'*10}|{'-'*45}")
    
    for i in range(buckets):
        start = i * bucket_size
        end = (i + 1) * bucket_size - 1
        count = counts[i]
        
        # Determine bar color based on count (just for fun)
        bar_color = Colors.GREEN if count > 0 else Colors.FAIL
        bar = f"{bar_color}{'█' * int(count * scale)}{Colors.ENDC}"
        
        # Add percentage
        percent = (count / len(data)) * 100
        
        print(f"{start:02d}-{end:02d}        | {count:<4} ({percent:4.1f}%) | {bar}")
    print(f"{'-'*70}\n")

def main():
    print_header("Collatz Conjecture RNG Demo")

    print(f"{Colors.BLUE}[*] Initializing Generator...{Colors.ENDC}")
    rng = CollatzRNG() 
    print(f"{Colors.GREEN}[+] Generator Ready!{Colors.ENDC}")
    print(f"    Seed: {Colors.WARNING}{rng.seed}{Colors.ENDC}")
    
    sample_size = 1000
    print(f"\n{Colors.BLUE}[*] Generating {sample_size} random numbers (0-99)...{Colors.ENDC}")
    
    start_time = time.time()
    data = [rng.randint(0, 99) for _ in range(sample_size)]
    duration = time.time() - start_time
    
    print(f"{Colors.GREEN}[+] Generation Complete in {duration:.4f} seconds.{Colors.ENDC}\n")

    # Statistics
    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    stdev = statistics.stdev(data)
    
    print(f"{Colors.CYAN}{Colors.BOLD}>> Statistical Summary{Colors.ENDC}")
    print(f"    Answer Sample: {Colors.WARNING}{data[:10]}...{Colors.ENDC}")
    print(f"    Mean:   {mean:.2f} (Expected ~49.5)")
    print(f"    Median: {median:.2f}")
    print(f"    Mode:   {mode}")
    print(f"    Stdev:  {stdev:.2f}\n")
    
    print_histogram(data)
    
    print(f"{Colors.HEADER}Thank you for determining chaos!{Colors.ENDC}\n")

if __name__ == "__main__":
    main()
