# 🎲 Collatz Random Number Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Experimental-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A conceptual pseudo-random number generator (PRNG) powered by the chaotic orbits of the **Collatz Conjecture** (also known as the $3n+1$ problem). This project explores how mathematical chaos can be harvested to generate entropy.

---

## 🧐 What is the Collatz Conjecture?

The **Collatz Conjecture** is one of the most famous unsolved problems in mathematics, often summarized as:
> "Mathematics may not be ready for such problems." - Paul Erdős

The rules are deceptively simple. Take any positive integer $n$:
1. If $n$ is **even**, divide it by 2 ($n / 2$).
2. If $n$ is **odd**, multiply it by 3 and add 1 ($3n + 1$).

Repeat this process. The conjecture states that no matter what number you start with, you will eventually reach the loop **4 → 2 → 1**.

### Why use it for RNG?
Before reaching the 4-2-1 loop, the sequence of numbers (the "trajectory") often behaves chaotically, rising and falling in unpredictable patterns (sometimes called "hailstone numbers"). We extract bits of randomness from these chaotic fluctuations.

---

## 🚀 How It Works

This generator maintains an internal state based on a Collatz trajectory.
1. **Entropy Extraction**: We take the current state modulo 2 (parity) or modulo varying bases to extract random bits/integers.
2. **Avoiding the Loop**: Since all Collatz sequences eventually crash into the 4-2-1 loop, this generator implements a "Kick Mechanism". If the state reaches 1, a linear congruential step kicks the state back into a high-entropy region, ensuring a continuous stream of numbers.

---

## 💻 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Yigtwxx/bsg-random-number-generator.git
cd bsg-random-number-generator
```

### 2. Run the Demo
We have included a colorful aesthetic demo script to visualize the distribution of generated numbers.

```bash
python demo.py
```

**Output Preview:**
The demo generates 1000 numbers, calculates statistics (Mean, Median, Mode), and draws an ASCII histogram in your terminal.

### 3. Use in Your Code
You can import the `CollatzRNG` class into your own Python projects.

```python
from collatz_rng import CollatzRNG

# Initialize the generator (seeds automatically with time)
rng = CollatzRNG()

# Generate a random integer between 0 and 100
rnd_int = rng.randint(0, 100)
print(f"Random Integer: {rnd_int}")

# Generate a float between 0.0 and 1.0
rnd_float = rng.random()
print(f"Random Float: {rnd_float}")

# Use a specific seed for reproducibility
deterministic_rng = CollatzRNG(seed=987654321)
```

---

## 📂 Project Structure

*   `collatz_rng.py`: The core class implementing the PRNG logic.
*   `demo.py`: A CLI tool to showcase the generator's capabilities with stats and graphs.
*   `README.md`: This documentation.

---

<p align="center">
  <i>Determining chaos, one hailstone at a time.</i>
</p>
