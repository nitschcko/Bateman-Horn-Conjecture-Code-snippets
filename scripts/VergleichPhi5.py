from sympy import isprime
import matplotlib.pyplot as plt
from mpmath import li
datei = open('primzahlen.txt', "r")
prime = []
for i in datei:
    prime.append(int(i))

def omega(n):
    if n % 5 == 1:
        return 4
    if n == 5:
        return 1
    return 0

def poly(x):
    return x**4+x**3+x**2+x+1


def zeichne_vergleich(x_max):
    x, tatsaechlich, bateman_horn, schranke = berechne_kurven(x_max)
    fig, (gesamt, detail) = plt.subplots(
        1, 2, sharex=True, figsize=(11, 4.6), constrained_layout=True
    )
    fig.suptitle(r"Primwerte von $n^4+n^3+n^2+n+1$", fontsize=18)
    gesamt.set_title("Gesamtansicht", loc="left", fontsize=12)
    detail.set_title("Zählung und Bateman–Horn im Detail", loc="left", fontsize=12)
    gesamt.set_ylabel(r"Anzahl der Primwerte für $2 \leq n < x$")
    gesamt.plot(x, schranke, color="#AF5127", lw=1.8, label="Schranke")

    for ax in (gesamt, detail):
        ax.step(x, tatsaechlich, where="post", color="#20364D", lw=2,
                label="Tatsächliche Anzahl")
        ax.plot(x, bateman_horn, color="#087B72", ls="--", lw=1.8,
                label="Bateman–Horn")
        ax.set_xlabel(r"Obere Grenze $x$")
        ax.set_ylim(bottom=0)
        ax.margins(x=0.01)
        ax.grid(axis="y", color="#D9DFE3", lw=0.7)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    gesamt.legend(loc="upper left", frameon=False)
    return fig

def berechne_kurven(x_max):
    if x_max < 2:
        raise ValueError("Die obere Grenze muss mindestens 2 sein.")

    x_werte = range(2, x_max + 1)
    tatsaechlich, bateman_horn, schranke = [], [], []
    anzahl = 0
    produkt = 1.0
    for x in x_werte:
        if isprime(x):
            # (1 - 1/p)**(-1) * (1 - omega(p)/p) = (p - omega(p))/(p - 1)
            produkt *= (x - omega(x)) / (x - 1)
        grundwert = produkt * float(li(x))
        bateman_horn.append(grundwert / 4)
        schranke.append(2 * grundwert)

        # range(2, x) schließt x aus. Bei Grenze x kommt also n = x - 1 hinzu.
        if x > 2 and isprime(poly(x - 1)):
            anzahl += 1
        tatsaechlich.append(anzahl)

    return x_werte, tatsaechlich, bateman_horn, schranke

if __name__ == "__main__":
    zeichne_vergleich(10000)
    plt.show()