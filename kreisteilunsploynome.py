
import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import prime, primerange


# Die ersten 20 Primzahlen als Indizes der Kreisteilungspolynome
INDIZES = [int(prime(i)) for i in range(1, 21)]


def omega(q, ell):
    """
    Anzahl der Nullstellen von Phi_ell(X) modulo q.
    ell und q sind Primzahlen.
    """
    if q == ell:
        return 1
    if q % ell == 1:
        return ell - 1
    return 0


def konstanten_berechnen(cutoff=100_000):
    """
    Berechnet die BH-Teilprodukte C_ell(Q)
    für die ersten 20 Kreisteilungspolynome.

    cutoff: Größte berücksichtigte Primzahl.
    """
    qs = np.array(
        list(primerange(2, cutoff + 1)),
        dtype=np.int64
    )

    log_produkte = np.zeros(len(INDIZES))
    verlauf = np.empty((len(INDIZES), len(qs)))

    for j, q_np in enumerate(qs):
        q = int(q_np)

        for i, ell in enumerate(INDIZES):
            w = omega(q, ell)

            # Logarithmus des Eulerfaktors
            log_faktor = (
                math.log1p(-w / q)
                - math.log1p(-1 / q)
            )

            log_produkte[i] += log_faktor
            verlauf[i, j] = math.exp(log_produkte[i])

    return qs, verlauf


def malen(cutoff=100_000):
    qs, verlauf = konstanten_berechnen(cutoff)

    fig, ax = plt.subplots(figsize=(14, 8))

    farben = plt.get_cmap("tab20").colors

    for i, ell in enumerate(INDIZES):
        ax.semilogx(
            qs,
            verlauf[i],
            label=rf"$\Phi_{{{ell}}}$",
            color=farben[i],
            linewidth=1.5
        )

    ax.axhline(
        y=1,
        color="black",
        linestyle="--",
        alpha=0.5,
        label="$C=1$"
    )

    ax.set_title(
        "Bateman-Horn-Konstanten der ersten "
        "20 Kreisteilungspolynome"
    )
    ax.set_xlabel(r"Primzahlgrenze $Q$")
    ax.set_ylabel(r"Teilprodukt $C_\ell(Q)$")

    ax.grid(True, which="both", alpha=0.2)
    ax.legend(
        loc="upper left",
        bbox_to_anchor=(1.02, 1),
        ncol=2,
        fontsize=9
    )

    fig.tight_layout()
    plt.show()

    print("\nLetzte berechnete Teilprodukte:")
    print("-" * 35)

    for i, ell in enumerate(INDIZES):
        print(
            f"Phi_{ell:2d}: "
            f"C_{ell}({qs[-1]}) = "
            f"{verlauf[i, -1]:.10f}"
        )

    return fig, ax, qs, verlauf


if __name__ == "__main__":
    malen(cutoff=100_000)
