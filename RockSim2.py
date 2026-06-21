import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def import_launch_data():

    planet_name = input("Planet name: ")

    g = float(input("Gravity (m/s²): "))

    dry_mass = float(input("Rocket dry mass (kg): "))

    fuel_mass = float(input("Fuel mass (kg): "))

    thrust = float(input("Engine thrust (N): "))

    burn_time = float(input("Burn time (s): "))

    angle = float(input("Launch angle (degrees): "))

    start_height = float(input("Launch height (m): "))

    return (
        planet_name,
        g,
        dry_mass,
        fuel_mass,
        thrust,
        burn_time,
        angle,
        start_height
    )


def simulate_flight(
        g,
        dry_mass,
        fuel_mass,
        thrust,
        burn_time,
        angle,
        start_height
):

    time = 0
    dt = 0.05

    angle_rad = math.radians(angle)

    current_mass = dry_mass + fuel_mass

    fuel_burn_rate = fuel_mass / burn_time

    x = 0
    y = start_height

    vx = 0
    vy = 0

    x_values = []
    y_values = []

    while y >= 0:

        # motor ég
        if time < burn_time and fuel_mass > 0:

            acceleration = thrust / current_mass

            ax = acceleration * math.cos(angle_rad)
            ay = acceleration * math.sin(angle_rad) - g

            fuel_mass -= fuel_burn_rate * dt

            if fuel_mass < 0:
                fuel_mass = 0

            current_mass = dry_mass + fuel_mass

        # motor kikapcsol
        else:

            ax = 0
            ay = -g

        vx += ax * dt
        vy += ay * dt

        x += vx * dt
        y += vy * dt

        x_values.append(x)
        y_values.append(y)

        time += dt

    return x_values, y_values, time


def animate_trajectory(x_values, y_values, planet_name):

    fig, ax = plt.subplots()

    ax.set_xlim(0, max(x_values) * 1.1)
    ax.set_ylim(0, max(y_values) * 1.1)

    ax.set_title(
        f"Rocket trajectory - {planet_name}"
    )

    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")

    ax.grid()

    rocket, = ax.plot([], [], "o")
    trail, = ax.plot([], [])

    def update(frame):

        rocket.set_data(
            [x_values[frame]],
            [y_values[frame]]
        )

        trail.set_data(
            x_values[:frame],
            y_values[:frame]
        )

        return rocket, trail

    animation = FuncAnimation(
        fig,
        update,
        frames=len(x_values),
        interval=20,
        blit=False
    )

    plt.show()


if __name__ == "__main__":

    (
        planet_name,
        g,
        dry_mass,
        fuel_mass,
        thrust,
        burn_time,
        angle,
        start_height

    ) = import_launch_data()

    x_values, y_values, flight_time = simulate_flight(
        g,
        dry_mass,
        fuel_mass,
        thrust,
        burn_time,
        angle,
        start_height
    )

    print()
    print("------ RESULTS ------")
    print(f"Flight time: {flight_time:.2f} s")
    print(f"Maximum height: {max(y_values):.2f} m")
    print(f"Impact distance: {x_values[-1]:.2f} m")

    animate_trajectory(
        x_values,
        y_values,
        planet_name
    )
