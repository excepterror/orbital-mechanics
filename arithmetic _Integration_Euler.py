"""
Επίλυση του Δευτέρου Νόμου του Νεύτωνα με τη μέθοδο της
αριθμητικής ολοκλήρωσης κατά Euler προς τον προσδιορισμό της τροχιάς πλανήτου
ελκομένου υπό της βαρυτικής δύναμης γειτνιάζοντος αστέρος και
γραφική αναπαράσταση της τροχιάς στο καρτεσιανό επίπεδο συντεταγμένων, συν τω χρόνω.
"""

from math import sqrt
import matplotlib.pyplot as plt


def acceleration(x: float, y: float):
    """
    Υπολογισμός της επιτάχυνσης και της απόστασης από την αρχή των αξόνων.
    """
    r = sqrt(x * x + y * y)
    inv_r3 = 1 / r**3

    ax = -x * inv_r3
    ay = -y * inv_r3

    return ax, ay, r


def write_parameters(file, t, x, vx, ax, y, vy, ay, r):
    """
    Παράμετροι του παραγόμενου αρχείου.
    """
    file.write(f"\n"
        f"{t:8.3f}"
        f"{x:10.3f}"
        f"{vx:10.3f}"
        f"{ax:10.3f}"
        f"{y:10.3f}"
        f"{vy:10.3f}"
        f"{ay:10.3f}"
        f"{r:10.3f}\n"
    )


def main():

    """
    Αρχικοποίηση αλγορίθμου.
    """
    total_t = 15
    dt = 0.01
    steps = int(total_t / dt)

    x = 0.5
    y = 0.0

    vx = 0.0
    vy = 1.63

    t = 0.0

    """
    Υπολογισμός αρχικής επιτάχυνσης.
    """
    ax, ay, r = acceleration(x, y)

    """
    Θέσεις x,y.
    """
    x_values = [x]
    y_values = [y]

    print(
        f"\n"
        f"t = {t:.3f}, "
        f"x = {x:.3f}, vx = {vx:.3f}, ax = {ax:.3f}, "
        f"y = {y:.3f}, vy = {vy:.3f}, ay = {ay:.3f}, "
        f"r = {r:.3f}"
    )

    with open("orbit_Euler.txt", "w") as outfile:

        outfile.write(f"Total time forward (T) is, T = {total_t:.1f} units of time.")
        outfile.write(f"\nTotal number of steps (N) is, N = {steps}.\n\n")

        outfile.write(
            f"{'t':>8}"
            f"{'x':>10}"
            f"{'vx':>10}"
            f"{'ax':>10}"
            f"{'y':>10}"
            f"{'vy':>10}"
            f"{'ay':>10}"
            f"{'r':>10}\n"
        )

        write_parameters(outfile, t, x, vx, ax, y, vy, ay, r)

        """
        Ο αλγόριθμος.
        """
        for _ in range(steps):

            # Compute acceleration at the current position
            ax, ay, r = acceleration(x, y)

            # Euler update of position
            x += dt * vx
            y += dt * vy

            # Euler update of velocity
            vx += dt * ax
            vy += dt * ay

            x_values.append(x)
            y_values.append(y)

            t += dt

            print(
                f"t = {t:.3f}, "
                f"x = {x:.3f}, vx = {vx:.3f}, ax = {ax:.3f}, "
                f"y = {y:.3f}, vy = {vy:.3f}, ay = {ay:.3f}, "
                f"r = {r:.3f}"
            )

            write_parameters(outfile, t, x, vx, ax, y, vy, ay, r)

        print(f"\nTotal time forward (T) is, T = {total_t:.1f} units of time.")
        print(f"Total number of steps (N) is, N = {steps}.")

    """
    Σχεδιασμός της γραφικής παράστασης.
    """

    plt.figure(figsize=(7, 7))

    plt.plot(
        x_values,
        y_values,
        "-x",
        linewidth=0.1,
        markersize=0.2,
        label="Orbit"
    )

    plt.scatter(0, 0, marker="*", s=150, label="Star")

    plt.title("Elliptical Orbit (Euler's Integration)")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)
    plt.axis("equal")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()