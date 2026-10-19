import numpy as np


X_0 = 0.35
N = 100
R_MIN = 3.0
R_MAX = 4.8


def func(x, r):
    return r * x * (1 - x)

def iterate(r, x_0=X_0, n=N):
    x = np.zeros(n + 1)
    x[0] = x_0
    for i in range(n):
        x[i + 1] = func(x[i], r)
        if not np.isfinite(x[i + 1]):
            return x[:i + 2]
    return x

def fixed_points(r):
    if r == 0.0:
        return [0.0]
    return [0.0, 1 - 1 / r]

def analyze_stability(r):
    points = fixed_points(r)
    results = []
    for point in points:
        derivative = r * (1 - 2 * point)
        if np.abs(derivative) < 1:
            stability = 'устойчива'
        elif np.abs(derivative) > 1:
            stability = 'неустойчива'
        else:
            stability = 'требуется дополнительный анализ'
        results.append({
            "point": point,
            "derivative": derivative,
            "stability": stability
        })
    return results

def lyapunov_exponent(r, x_0=X_0, transient=1000, n=5000):
    x = x_0
    for _ in range(transient):
        x = func(x, r)
        if not np.isfinite(x) or not 0 <= x <= 1:
            return np.nan
    values = []
    for _ in range(n):
        derivative = abs(r * (1 - 2 * x))
        if derivative == 0:
            return -np.inf
        values.append(np.log(derivative))
        x = func(x, r)
        if not np.isfinite(x) or not 0 <= x <= 1:
            return np.nan
    return np.mean(values)

def statistical_analysis(x):
    sample = x[81:]
    sample = sample[np.isfinite(sample)]
    if len(sample) == 0:
        return None
    return {
        "count": len(sample),
        "mean": np.mean(sample),
        "variance": np.var(sample),
        "std": np.std(sample),
        "min": np.min(sample),
        "max": np.max(sample)
    }
            