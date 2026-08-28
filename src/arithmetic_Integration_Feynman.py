"""
Επίλυση του Δευτέρου Νόμου του Νεύτωνα με τη μέθοδο της
αριθμητικής ολοκλήρωσης κατά Feynman προς τον προσδιορισμό της τροχιάς πλανήτου
ελκομένου υπό της βαρυτικής δύναμης γειτνιάζοντος αστέρος και
γραφική αναπαράσταση της χρονικής εξέλιξης της τροχιάς στο καρτεσιανό επίπεδο συντεταγμένων.
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
        f"{x:10.5f}"
        f"{vx:10.3f}"
        f"{ax:10.3f}"
        f"{y:10.5f}"
        f"{vy:10.3f}"
        f"{ay:10.3f}"
        f"{r:10.3f}\n"
    )

def calculate_areas(x_values, y_values, dt):
    """
    Υπολογισμός του εμβαδού των επί μέρους στοιχειωδών επιφανειών.
    """
    with open("areas_Feynman.txt", "w") as outfile:
        outfile.write(f"{'Time interval':>22}{'Area':>18}\n")

        for i in range(len(x_values) - 1):
            x1 = x_values[i]
            y1 = y_values[i]

            x2 = x_values[i + 1]
            y2 = y_values[i + 1]

            area = 0.5 * abs(x1 * y2 - x2 * y1)

            t1 = i * dt
            t2 = (i + 1) * dt

            outfile.write(
                f"{f'dt = {t1:.2f} to {t2:.2f}':<25}{area:15.8f}\n")

def main():

    """
     Αρχικοποίηση του αλγορίθμου.
    """
    total_t = 4.04
    dt = 0.01
    steps = int(total_t / dt)

    x = .5
    y = .0

    vx = .0
    vy = 1.63

    """
    Υπολογισμός της αρχικής επιτάχυνσης.
    """
    ax, ay, r = acceleration(x, y)

    """
    Προώθηση της αρχικής ταχύτητας κατά μισό βήμα, dt/2.
    """
    vx_half = vx + 0.5 * dt * ax
    vy_half = vy + 0.5 * dt * ay

    t = 0.0

    """
    Θέσεις x,y.
    """
    x_values = [x]
    y_values = [y]

    print(f"\n"
        f"t = {t:.3f}, "
        f"x = {x:.3f}, vx_half = {vx_half:.3f}, ax = {ax:.3f}, "
        f"y = {y:.3f}, vy_half = {vy_half:.3f}, ay = {ay:.3f}, "
        f"r = {r:.3f}"
    )

    with open("orbit_Feynman.txt", "w") as outfile:

        outfile.write(f"Total time forward (T) is, T = {total_t:.3f} units of time.")
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

        write_parameters(outfile, t, x, vx_half, ax, y, vy_half, ay, r)

        """
        Ο κύριος αλγόριθμος.
        """
        for _ in range(steps):

            """
            Υπολογισμός της νέας θέσης με βάση τη προωθημένη ταχύτητα.
            """
            x += dt * vx_half
            y += dt * vy_half

            x_values.append(x)
            y_values.append(y)

            """
            Υπολογισμός της νέας επιτάχυνσης.
            """
            ax, ay, r = acceleration(x, y)

            """
            Υπολογισμός της νέας ταχύτητας.
            """
            vx_half += dt * ax
            vy_half += dt * ay

            t += dt

            print(
                f"t = {t:.3f}, "
                f"x = {x:.3f}, vx_half = {vx_half:.3f}, ax = {ax:.3f}, "
                f"y = {y:.3f}, vy_half = {vy_half:.3f}, ay = {ay:.3f}, "
                f"r = {r:.3f}"
            )

            write_parameters(outfile, t, x, vx_half, ax, y, vy_half, ay, r)

        print(f"\nTotal time forward (T) is, T = {total_t:.3f} units of time.")
        print(f"Total number of steps (N) is, N = {steps}.")

    calculate_areas(x_values, y_values, dt)

    """
    Σχεδιασμός της γραφικής παράστασης.
    """

    plt.figure(figsize=(7, 7))

    plt.plot(
        x_values,
        y_values,
        "-x",
        linewidth=.5,
        markersize=.02,
        label="Orbit"
    )

    # plt.scatter(x_values, y_values, marker="x", s=1, label="Planet")

    # Plot the star at the origin
    plt.scatter(0, 0, marker="*", s=150, label="Star")

    plt.title("Elliptical Orbit (Feynman's integration)")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)
    plt.axis("equal")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()