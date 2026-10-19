
import matplotlib.pyplot as plt
import numpy as np

from methods import (
    X_0,
    N,
    iterate,
    analyze_stability,
    statistical_analysis,
    lyapunov_exponent
)

from plots import (
    plot_trajectory,
    plot_phase_duagram,
    plot_bifurcation
)


def main():
    r = 3.8

    print(f"Параметр r = {r}")
    print(f"Начальное условие x0 = {X_0}")
    print(f"Количество итераций = {N}")

    x = iterate(r)

    print("\nСтационарные точки и устойчивость:")

    for result in analyze_stability(r):
        print(
            f"x* = {result['point']:.6f}, "
            f"f'(x*) = {result['derivative']:.6f}, "
            f"{result['stability']}"
        )

    print("\nПоследние значения последовательности:")
    print(x[-10:])

    print("\nСтатистическая обработка:")
    statistics = statistical_analysis(x)

    if statistics is not None:
        for key, value in statistics.items():
            if isinstance(value, (int, np.integer)):
                print(f"{key}: {value}")
            else:
                print(f"{key}: {value:.6f}")

    print("\nПоказатель Ляпунова:")
    print(lyapunov_exponent(r))

    plot_trajectory(r, x)
    plot_phase_duagram(r, x)
    plot_bifurcation()

    plt.show()


if __name__ == "__main__":
    main()
