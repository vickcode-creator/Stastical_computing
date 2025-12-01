
import numpy as np

def estimate_pi(n=1000000):
    pts = np.random.rand(n,2)
    inside = (pts**2).sum(axis=1) <= 1.0
    return inside.mean() * 4.0

if __name__ == "__main__":
    for n in [1000, 10000, 100000, 1000000]:
        pi_est = estimate_pi(n)
        print(f"n={n:,}: pi ~ {pi_est}")
