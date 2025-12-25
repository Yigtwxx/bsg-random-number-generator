# Collatz RNG

A pseudo-random number generator (PRNG) powered by the chaotic orbits of the **Collatz Conjecture** (3n+1 problem).

## Theory
The Collatz function is defined as:
$$ f(n) = \begin{cases} n/2 & \text{if } n \equiv 0 \pmod{2} \\ 3n+1 & \text{if } n \equiv 1 \pmod{2} \end{cases} $$

The generator uses the trajectory of integer sequences under this map to generate entropy. 
To avoid the trivial $4 \to 2 \to 1$ loop, the generator employs a "kick" mechanism (linear congruential step) when the state collapses to 1, ensuring continuous chaotic behavior.

## Usage

### Basic
```python
from collatz_rng import CollatzRNG

# Initialize with default seed (time-based)
rng = CollatzRNG()

# Generate random integer [0, 100]
print(rng.randint(0, 100))

# Generate float [0.0, 1.0)
print(rng.random())
```

### Deterministic Seeding
```python
rng = CollatzRNG(seed=12345)
print(rng.randint(0, 10)) # Repeatable result
```

## files
- `collatz_rng.py`: Main class implementation.
- `demo.py`: Script to generate numbers and visualize distribution.
