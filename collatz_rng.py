import time

class CollatzRNG:
    """
    A pseudo-random number generator based on the Collatz conjecture (3n + 1).
    """
    def __init__(self, seed=None):
        if seed is None:
            seed = int(time.time() * 1000)
        self.seed = seed
        self.state = seed
        # A counter to ensure diversity if we hit the 4-2-1 loop frequently
        self.steps_taken = 0

    def _next_collatz(self, n):
        """Standard Collatz step provided for reference/usage."""
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1

    def _step(self):
        """
        Advances the internal state using Collatz logic.
        Includes a 'kick' mechanism if we fall into the 4-2-1 loop (state reaches 1).
        """
        if self.state <= 1:
            # Trap avoidance: If we hit 1, mix bits with seed + step counter
            # to jump to a new chaotic trajectory.
            self.state = (self.state + self.seed + self.steps_taken + 0xDEADBEEF) * 1664525
        
        if self.state % 2 == 0:
            self.state = self.state // 2
        else:
            self.state = 3 * self.state + 1
        
        self.steps_taken += 1
        return self.state

    def next_int(self):
        """Returns the raw current state integer."""
        return self._step()

    def randint(self, a, b):
        """
        Returns a random integer N such that a <= N <= b.
        Uses the lower bits of the state for better distribution properties than modulo on the whole structure.
        """
        range_size = b - a + 1
        if range_size <= 0:
            raise ValueError("Empty range")
        
        # Advance state multiple times to "mix" better, since single Collatz steps are correlated
        # (e.g. n -> 3n+1 is always growing, n -> n/2 is always shrinking)
        # We take 3 steps per number to lose some immediate correlation.
        self._step()
        self._step()
        val = self._step()
        
        return a + (val % range_size)

    def random(self):
        """
        Returns the next random floating point number in the range [0.0, 1.0).
        """
        # Generate a large integer and normalize it
        val = self.randint(0, 10**9)
        return val / (10**9 + 1.0)

if __name__ == "__main__":
    # Quick self-test
    rng = CollatzRNG(seed=12345)
    print("First 10 numbers [0, 100]:")
    for _ in range(10):
        print(rng.randint(0, 100), end=" ")
    print("\n")
