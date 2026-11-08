from sympy import isprime
import numpy as np
import scipy.special as csc
import math
import matplotlib.pyplot as plt


def euler_totient(n):
    if n < 1:
        raise ValueError("n muss eine positive ganze Zahl sein.")
    # Mit n als oberer Grenze gilt auch euler_totient(1) == 1.
    return sum(math.gcd(i, n) == 1 for i in range(1, n + 1))


def asymptotic(m, limit):
    phi = euler_totient(m)
    if limit < 2:
        return 0.0
    return limit / (phi * math.log(limit))


def asymptoticLog(m, limit):
    """Integral von 2 bis limit ueber 1/log(t), geteilt durch phi(m)."""
    phi = euler_totient(m)
    if limit <= 2:
        return 0.0
    return (csc.expi(math.log(limit)) - csc.expi(math.log(2))) / phi


def primesarihemticProgression(a, m, limit):
    if a < 1 or m < 1 or limit < 1:
        raise ValueError("a, m und limit muessen positive ganze Zahlen sein.")
    if math.gcd(a, m) != 1:
        return "Das ist keine zulaessige Menge"

    primeValues = [a + i * m for i in range(limit) if isprime(a + i * m)]
    ende = a + (limit - 1) * m
    # Die Differenz vergleicht jeweils das Intervall [a, ende].
    asym = asymptotic(m, ende) - asymptotic(m, a - 1)
    asymlog = asymptoticLog(m, ende) - asymptoticLog(m, a - 1)
    print(
        f"Es sind {len(primeValues)} Primzahlen in den ersten {limit} "
        f"Folgegliedern. Die asymptotische Vorhersage liefert {asym:.2f}, "
        f"mit logarithmischem Integral {asymlog:.2f}."
    )
    return asym, len(primeValues)


def malen(a=1, m=4, limit=10000):
    """Vergleicht Primzahlanzahl und Naeherungen fuer die ersten limit Glieder."""
    if a < 1 or m < 1 or limit < 1:
        raise ValueError("a, m und limit muessen positive ganze Zahlen sein.")
    if math.gcd(a, m) != 1:
        raise ValueError("a und m muessen teilerfremd sein.")

    n = np.arange(1, limit + 1)
    folge = a + (n - 1) * m
    # Jedes Glied wird genau einmal auf Primalitaet geprueft.
    primzahlanzahl = np.cumsum([isprime(int(x)) for x in folge])

    # Subtraktion des Anfangswertes: Vergleich fuer [a, folge[n - 1]].
    start_asym = asymptotic(m, a - 1)
    start_log = asymptoticLog(m, a - 1)
    asym_werte = [asymptotic(m, int(x)) - start_asym for x in folge]
    log_werte = [asymptoticLog(m, int(x)) - start_log for x in folge]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.step(n, primzahlanzahl, where="post", label="Tatsächliche Primzahlanzahl")
    ax.plot(n, asym_werte, "--", label=r"Näherung mit $\frac{x}{\varphi(m)\log x}$")
    ax.plot(n, log_werte, "-.", label=r"Näherung mit $\frac{LI({a+x\cdot m})}{\varphi(m)}$")
    ax.set(
        xlabel="Anzahl der betrachteten Folgeglieder n",
        ylabel="Anzahl der Primzahlen",
        title=f"Primzahlen in der Folge {a} + i · {m}, i = 0, …, {limit - 1}",
    )
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    plt.show()
    return fig, ax


if __name__ == "__main__":
    malen()