import time

class CollatzRNG:
    """
    Pseudo-random number generator (PRNG) based on the Collatz conjecture (3n + 1).
    """
    def __init__(self, seed=None):
        # If no seed value is provided, use the current time in milliseconds.
        if seed is None:
            seed = int(time.time() * 1000)
        self.seed = seed
        self.state = seed
        # A counter used to ensure diversity if we frequently enter the 4-2-1 cycle.
        self.steps_taken = 0

    def _next_collatz(self, n):
        """Standard Collatz step for reference/usage."""
        # If the number is even, divide by 2.
        if n % 2 == 0:
            return n // 2
        else:
            # If the number is odd, multiply by 3 and add 1.
            return 3 * n + 1

    def _step(self):
        """
        Advances the internal state using Collatz logic.
        Includes a 'kick' mechanism if we enter the 4-2-1 cycle (state reaches 1).
        """
        if self.state <= 1:
            # Trap avoidance: If we reach 1, we mix the bits with seed and step counter
            # to jump to a new chaotic orbit.
            # 0xDEADBEEF: A common "magic number" used to increase randomness.
            # 1664525: A multiplier commonly used in Linear Congruential Generators (LCG).
            self.state = (self.state + self.seed + self.steps_taken + 0xDEADBEEF) * 1664525
        
        # Apply Collatz rule: If even, halve it; if odd, 3k+1.
        if self.state % 2 == 0:
            self.state = self.state // 2
        else:
            self.state = 3 * self.state + 1
        
        self.steps_taken += 1
        return self.state

    def next_int(self):
        """Returns the current state integer as raw."""
        return self._step()

    def randint(self, a, b):
        """
        Returns a random integer N such that a <= N <= b.
        Aims to use the lower bits of the state for better distribution properties
        instead of taking the modulo over the entire structure (though we simply 
        use mod here, mixing is done with step count).
        """
        range_size = b - a + 1
        if range_size <= 0:
            raise ValueError("Empty range")
        
        # Since single Collatz steps are correlated (e.g., n -> 3n+1 always grows, n -> n/2 always shrinks),
        # we advance the state multiple times to provide better "mixing".
        # We take 3 steps per number generation to lose instant correlation.
        self._step()
        self._step()
        val = self._step()
        
        # Apply modulo operation and offset to fit the result within the desired range (between a and b).
        return a + (val % range_size)

    def random(self):
        """
        Returns the next random floating-point number in the range [0.0, 1.0).
        """
        # Generate a large integer and normalize it (squeeze it between 0 and 1).
        val = self.randint(0, 10**9)
        return val / (10**9 + 1.0)

if __name__ == "__main__":
    # Quick self-test block
    rng = CollatzRNG(seed=12345)
    print("First 10 numbers [0, 100]:")
    for _ in range(10):
        # Generate random integers between 0 and 100 and print them side by side.
        print(rng.randint(0, 100), end=" ")
    print("\n")
