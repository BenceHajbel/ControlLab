import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def import_launch_data():

    planet_name = input("Planet name: ")

    g = float(input("Gravity (m/s²): "))

    dry_mass = float(input("Rocket dry mass (kg): "))

    fuel_mass = float(input("Fuel mass (kg): "))

    current_mass = dry_mass + fuel_mass

    thrust = float(input("Engine thrust (N): "))

    burn_time = float(input("Burn time (s): "))

    angle = float(input("Launch angle (degrees): "))

    angle_rad = math.radians(angle)

    start_height = float(input("Launch height (m): "))

    return (
        planet_name,
        g,
        dry_mass,
        fuel_mass,
        current_mass,
        thrust,
        burn_time,
        angle,
        start_height
    )


def simulate_flight(planet_name, g, dry_mass, fuel_mass, current_mass, thrust, burn_time, angle, start_height, angle_rad):
    time = 0
    dt = 0.1

    angle_rad = math.radians(angle)

    x = 0
    y = start_height

    vx = 0
    vy = 0

    x_values = []
    y_values = []

    fuel_burn_rate = fuel_mass / burn_time

    while y >= 0:
        if time < burn_time and fuel_mass > 0:
            ax = (thrust / current_mass) * math.cos(angle_rad)
            ay = (thrust / current_mass) * math.sin(angle_rad) - g
            fuel_mass -= fuel_burn_rate * dt
            current_mass = dry_mass + fuel_mass
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

    range_distance = x_values[-1]
    return x_values, y_values, range_distance


def plot_trajectory(x_values, y_values, planet_name):
    plt.plot(x_values, y_values)
    plt.title(f"Rocket Trajectory on {planet_name}")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid()
    plt.show()


def animate_trajectory(x_values, y_values):

    fig, ax = plt.subplots()

    ax.set_xlim(0, max(x_values) * 1.1)
    ax.set_ylim(0, max(y_values) * 1.1)

    ax.set_title("Rocket Animation")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.grid()

    rocket, = ax.plot([], [], "o")
    trail, = ax.plot([], [])

    def update(frame):

        rocket.set_data(
            x_values[frame],
            y_values[frame]
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
        current_mass,
        thrust,
        burn_time,
        angle,
        start_height
    ) = import_launch_data()

    angle_rad = math.radians(angle)

    x_values, y_values = simulate_flight(
        planet_name,
        g,
        dry_mass,
        fuel_mass,
        current_mass,
        thrust,
        burn_time,
        angle,
        start_height,
        angle_rad
    )

    plot_trajectory(
        x_values,
        y_values,
        planet_name
    )

    animate_trajectory(
        x_values,
        y_values
    )

''' Good Data for Testing:
Planet name: Earth
Gravity (m/s²): 9.81

Rocket dry mass (kg): 100
Fuel mass (kg): 50

Engine thrust (N): 5000
Burn time (s): 8

Launch angle (degrees): 65

Launch height (m): 0'''
