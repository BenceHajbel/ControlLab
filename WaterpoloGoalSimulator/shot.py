import math
g = 9.81  # acceleration due to gravity (m/s^2)
import matplotlib.pyplot as plt


def import__shot_data():
    shot_distance = float(input("Enter the shot distance (m): "))
    v = float(input("Enter the shot speed (m/s): "))
    a = float(input("Enter the shot angle (degrees): "))
    a_rad = math.radians(a)  # convert angle to radians
    h = float(input("Enter the shot height (m): "))
    m = float(input("Enter the shot mass (kg): "))
    return v, a, shot_distance, h, m


def import_goal_data():
    goal_width = float(input("Enter the goal width (m): "))
    goal_height = float(input("Enter the goal height (m): "))
    return goal_width, goal_height


def calculate_range_distance(v, a):
    a_rad = math.radians(a)
    range_distance = (v ** 2) * math.sin(2 * a_rad) / g
    return range_distance


def calculate_shot_height(v, a, distance):
    a_rad = math.radians(a)
    height = (
        distance * math.tan(a_rad)
        - (g * distance ** 2)
        / (2 * v ** 2 * (math.cos(a_rad) ** 2))
    )
    return height


def calculate_shot_time(v, a, distance):
    a_rad = math.radians(a)
    time = distance / (v * math.cos(a_rad))
    return time

def generate_trajectory(v, a, h):
    x_values = []
    y_values = []

    a_rad = math.radians(a)

    x = 0

    while True:

        y = (
            h
            + x * math.tan(a_rad)
            - (g * x**2)
            / (2 * v**2 * (math.cos(a_rad)**2))
        )

        if y < 0:
            break

        x_values.append(x)
        y_values.append(y)

        x += 0.1

    return x_values, y_values

def visualize_shot(v, a, h, shot_distance, goal_height):
    x_values, y_values = generate_trajectory(v, a, h)

    plt.plot(x_values, y_values)

    plt.axvline(
        x=shot_distance,
        ymin=0,
        ymax=goal_height / max(y_values),
        label="Goal"
    )

    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.title("Water Polo Shot")
    plt.grid(True)
    plt.legend()

    plt.show()



def main():
    v, a, shot_distance, h, m = import__shot_data()
    goal_width, goal_height = import_goal_data()

    range_distance = calculate_range_distance(v, a)
    shot_height = calculate_shot_height(v, a, shot_distance)
    shot_time = calculate_shot_time(v, a, shot_distance)

    print(f"Range Distance: {range_distance:.2f} m")
    print(f"Shot Height at {shot_distance} m: {shot_height:.2f} m")
    print(f"Shot Time: {shot_time:.2f} s")

    if 0 <= shot_height <= goal_height and 0 <= range_distance <= goal_width:
        print("The shot is successful!")
    else:
        print("The shot missed the goal.")

    visualize_shot(
        v,
        a,
        h,
        shot_distance,
        goal_height
    )

if __name__ == "__main__":
    main()

