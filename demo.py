from collatz_rng import CollatzRNG
import time

def print_histogram(data, buckets=10, width=50):
    if not data:
        return
    min_val = 0 # Expecting generation range stats
    max_val = max(data)
    
    # We are generating numbers in range [0, 99] for this demo
    # so we can hardcode buckets for clarity or calculate them.
    # Let's calculate simple frequency.
    
    # Create simple frequency map for 10 ranges: 0-9, 10-19...
    counts = [0] * buckets
    range_limit = 100
    bucket_size = range_limit // buckets
    
    for x in data:
        idx = min(x // bucket_size, buckets - 1)
        counts[idx] += 1
        
    total = len(data)
    print(f"\nDistribution of {total} numbers (Range 0-99):")
    print(f"{'Range':<12} | {'Count':<6} | {'Graph'}")
    print("-" * 70)
    
    max_count = max(counts)
    scale = width / max_count if max_count > 0 else 1
    
    for i in range(buckets):
        start = i * bucket_size
        end = (i + 1) * bucket_size - 1
        count = counts[i]
        bar = "#" * int(count * scale)
        print(f"{start:02d}-{end:02d}        | {count:<6} | {bar}")

def main():
    print("Initializing Collatz RNG...")
    # Seed with current time
    rng = CollatzRNG() 
    
    print(f"Seed used: {rng.seed}")
    print("Generating 1000 random numbers between 0 and 99...")
    
    data = []
    for _ in range(1000):
        data.append(rng.randint(0, 99))
        
    print(f"First 10 values: {data[:10]}")
    
    print_histogram(data)
    
    print("\nDone.")

if __name__ == "__main__":
    main()
