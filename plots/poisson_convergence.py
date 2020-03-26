import numpy as np
from pathlib import Path
import matplotlib
matplotlib.use("pgf")
import matplotlib.pyplot as plt

plt.rcParams["figure.constrained_layout.use"] = True

if __name__ == "__main__":
    Ns = np.load(Path(__file__).resolve().parent.parent /"computation" / "poisson_convergence_Ns.npy")
    Es = np.load(Path(__file__).resolve().parent.parent /"computation" / "poisson_convergence_errors.npy")

    plt.loglog([1.0 / N for N in Ns], Es, "-kx")
    plt.xlabel("Mesh size $h$")
    plt.ylabel("$L_2$ error norm")
    plt.savefig(Path(__file__).parent / "poisson_convergence.pdf")
