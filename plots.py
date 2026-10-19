import numpy as np
import matplotlib.pyplot as plt

from methods import func, X_0


def plot_trajectory(r, x):
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(x)), x, marker=".", markersize=4)
    plt.xlabel("Номер итерации n")
    plt.ylabel("$x_n$")
    plt.title(f"Логистическое отображение r = {r}")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('images/trajectory.png')

def plot_phase_duagram(r, x):
    plt.figure(figsize=(7, 7))
    grid = np.linspace(0, 1, 500)
    plt.plot(grid, func(grid, r), label=r'$x_{n+1}=f(x_n)$')
    plt.plot(grid, grid, '--', label='$x_{n+1}=x_n$')
    plt.scatter(x[:-1], x[1:], s=15, label='Траектория')
    plt.xlabel("$x_n$")
    plt.ylabel("$x_{n+1}$")
    plt.title(f"Фазовая диарамма r = {r}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("images/pрase_diagram.png")

def plot_bifurcation():
    parameters = np.linspace(3.0, 4.8, 1800)
    iterations = 1200
    transient = 800
    rs = []
    xs = []
    for r in parameters:
        x = X_0
        for _ in range(transient):
            x = func(x, r)
            if not np.isfinite(x) or not 0 <= x <= 1:
                break
        else:
            for _ in range(iterations):
                x = func(x, r)
                if not np.isfinite(x) or not 0 <= x <= 1:
                    break
                rs.append(r)
                xs.append(x)
    plt.figure(figsize=(11, 6))
    plt.plot(rs, xs, ".", alpha=0.5)
    plt.xlabel("Параметр r")
    plt.ylabel("Установившиеся значения $x_n$")
    plt.title("Бифуркационная диаграмма логистического отображения")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("images/bifurcation.png")