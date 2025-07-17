
"""
There are about 20+ functions in the random module depending on the Python version, but the core ones listed above are most frequently used.
Here's a list of the most commonly used random functions:
- random.randint(a, b): Returns a random integer N such that a <= N <= b.
| Function                         | Description                                                                  |
| -------------------------------- | ---------------------------------------------------------------------------- |
| `random()`                       | Returns a random float between **0.0 and 1.0**                               |
| `uniform(a, b)`                  | Returns a random float between **a and b**                                   |
| `randint(a, b)`                  | Returns a random **integer between a and b**, inclusive                      |
| `randrange(start, stop[, step])` | Returns a randomly selected element from `range(start, stop, step)`          |
| `choice(seq)`                    | Returns a random element from a non-empty sequence                           |
| `choices(seq, k=n)`              | Returns a **list** of `k` random elements from a sequence (with replacement) |
| `sample(seq, k)`                 | Returns a **list** of `k` random elements **without replacement**            |
| `shuffle(seq)`                   | Shuffles a **mutable sequence** (like a list) **in-place**                   |
| `seed(a=None)`                   | Initializes the random number generator (for reproducibility)                |
| `getstate()`                     | Returns the current state of the random generator                            |
| `setstate(state)`                | Restores the generator to a previous state                                   |
| `betavariate(alpha, beta)`       | Beta distribution                                                            |
| `expovariate(lambd)`             | Exponential distribution                                                     |
| `gammavariate(alpha, beta)`      | Gamma distribution                                                           |
| `gauss(mu, sigma)`               | Gaussian (normal) distribution                                               |
| `lognormvariate(mu, sigma)`      | Log-normal distribution                                                      |
| `normalvariate(mu, sigma)`       | Normal distribution                                                          |
| `triangular(low, high, mode)`    | Triangular distribution                                                      |
| `vonmisesvariate(mu, kappa)`     | Von Mises distribution                                                       |
| `weibullvariate(alpha, beta)`    | Weibull distribution                                                         |
___________________________________________________________________________________________________________________

For example like:
"""


import random

print(random.random())         # Random float between 0 and 1
print(random.randint(1, 10))   # Random int between 1 and 10
print(random.choice(['a', 'b', 'c']))  # Random element from list
print(random.uniform(1, 10))  # Random float between 1 and 10
print(random.randrange(1, 10, 2))  # Random even int between 1
print(random.sample(['a', 'b', 'c'], 2))  # Random 2
print(random.shuffle(['a', 'b', 'c']))  # Randomly shuffle list
print(random.getstate())  # Get current state of random number generator
print(random.setstate(random.getstate()))  # Restore previous state of random number generator
