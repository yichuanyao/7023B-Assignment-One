import math
import turtle
import random


def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)


def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.right(120)


def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)


def draw_centered_square(t, cx, cy, half_side, rotation_deg):
    rad = math.radians(rotation_deg)
    corners = [
        (-half_side, -half_side),
        (half_side, -half_side),
        (half_side, half_side),
        (-half_side, half_side),
    ]
    points = []
    for px, py in corners:
        rx = px * math.cos(rad) - py * math.sin(rad)
        ry = px * math.sin(rad) + py * math.cos(rad)
        points.append((cx + rx, cy + ry))

    t.penup()
    t.goto(points[0])
    t.pendown()
    for pt in points[1:]:
        t.goto(pt)
    t.goto(points[0])


def draw_khatam(t, cx, cy, half_side, colour_a, colour_b):
    t.pencolor(colour_a)
    draw_centered_square(t, cx, cy, half_side, 0)
    t.pencolor(colour_b)
    draw_centered_square(t, cx, cy, half_side, 45)


def draw_islamic_geometric_pattern(t, cx, cy, radius, colours):
    t.pensize(2)

    t.penup()
    t.goto(cx, cy - radius)
    t.setheading(0)
    t.pendown()
    t.pencolor(colours[0])
    t.circle(radius)

    layers = 9
    for i in range(layers):
        half = radius * (0.95 - i * 0.09)
        c1 = colours[i % len(colours)]
        c2 = colours[(i + 3) % len(colours)]
        draw_khatam(t, cx, cy, half, c1, c2)

    for i in range(16):
        t.pencolor(colours[(i + 1) % len(colours)])
        half = radius * (0.55 + 0.02 * (i % 5))
        draw_centered_square(t, cx, cy, half, i * 11.25)

    for i in range(8):
        ang = math.radians(i * 45 + 22.5)
        sx = cx + radius * 1.15 * math.cos(ang)
        sy = cy + radius * 1.15 * math.sin(ang)
        c1 = colours[i % len(colours)]
        c2 = colours[(i + 4) % len(colours)]
        draw_khatam(t, sx, sy, radius * 0.22, c1, c2)

    draw_khatam(t, cx, cy, radius * 0.18, colours[2], colours[6])


def turtle_drawing():
    screen = turtle.Screen()
    screen.setup(width=1000, height=750)
    screen.bgcolor("black")
    screen.title("Assignment One - Turtle Drawing (Yao Yichuan)")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    colours = [
        "red", "orange", "yellow", "lime", "cyan",
        "deepskyblue", "magenta", "violet", "gold", "white",
    ]

    islamic_colours = [
        "#00E5FF", "#FFD700", "#4169E1", "#FF1744",
        "#00E676", "#FF9100", "#E040FB", "#FFF59D",
        "#18FFFF", "#FF6E40",
    ]

    t.penup()
    t.goto(260, 160)
    t.setheading(0)
    t.pendown()
    length = 10
    for i in range(24):
        t.pencolor(colours[i % len(colours)])
        t.pensize(1 + i // 10)
        draw_square(t, length)
        t.right(10)
        length += 3

    t.penup()
    t.goto(-300, 220)
    t.setheading(0)
    t.pendown()
    length = 10
    for i in range(20):
        t.pencolor(colours[(i + 3) % len(colours)])
        t.pensize(2)
        draw_triangle(t, length)
        t.left(12)
        length += 4

    t.penup()
    t.goto(300, -220)
    t.setheading(0)
    t.pendown()
    length = 25
    for i in range(14):
        t.pencolor(colours[(i + 5) % len(colours)])
        t.pensize(2)
        draw_star(t, length)
        t.right(20)
        length += 3

    edge_spots = [
        (-40, 320), (80, 330), (200, 300),
        (360, 80), (370, -40),
        (120, -330),
    ]
    for i, (sx, sy) in enumerate(edge_spots):
        t.penup()
        t.goto(sx, sy)
        t.setheading(i * 25)
        t.pendown()
        t.pencolor(random.choice(colours))
        t.pensize(2)
        if i % 3 == 0:
            draw_star(t, 20)
        elif i % 3 == 1:
            draw_square(t, 16)
        else:
            draw_triangle(t, 18)

    draw_islamic_geometric_pattern(t, cx=-210, cy=-130, radius=95, colours=islamic_colours)

    print("Turtle drawing complete. Close the window to continue.")
    screen.exitonclick()


def qa_bot():
    print("=" * 50)
    print("Welcome to the Assignment One QA Bot!")
    print("Ask me something about: HKU, robot, jetson, ai, human")
    print("Type 'quit' or 'exit' to leave.")
    print("=" * 50)

    while True:
        question = input("\nYour question: ").strip()

        if question == "":
            print("Please type a question.")
            continue

        text = question.lower()

        if text in ("quit", "exit", "q"):
            print("Goodbye! Thanks for chatting.")
            break
        elif "hku" in text:
            print(
                "HKU (The University of Hong Kong) is a leading research university "
                "in Asia, known for innovation, diversity, and academic excellence."
            )
        elif "robot" in text:
            print(
                "A robot is a programmable machine that can sense its environment "
                "and perform tasks automatically, often with sensors and actuators."
            )
        elif "jetson" in text:
            print(
                "NVIDIA Jetson is a family of embedded AI computing boards used for "
                "edge AI, robotics, computer vision, and autonomous systems."
            )
        elif "ai" in text:
            print(
                "AI (Artificial Intelligence) enables computers to learn from data, "
                "reason, and solve problems that normally require human intelligence."
            )
        elif "human" in text:
            print(
                "Humans create, teach, and guide AI and robots. Collaboration between "
                "humans and machines can improve safety, productivity, and creativity."
            )
        else:
            print(
                "Sorry, I don't understand that yet. "
                "Try asking about HKU, robot, jetson, ai, or human."
            )


def simple_calculator():
    print("=" * 50)
    print("Simple Calculator")
    print("Operators: +  -  *  /")
    print("=" * 50)

    try:
        first = float(input("Enter the first number: ").strip())
        second = float(input("Enter the second number: ").strip())
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    operator = input("Choose an operator (+, -, *, /): ").strip()

    if operator == "+":
        result = first + second
        print(f"Result: {first} + {second} = {result}")
    elif operator == "-":
        result = first - second
        print(f"Result: {first} - {second} = {result}")
    elif operator == "*":
        result = first * second
        print(f"Result: {first} * {second} = {result}")
    elif operator == "/":
        if second == 0:
            print("Error: cannot divide by zero.")
        else:
            result = first / second
            print(f"Result: {first} / {second} = {result}")
    else:
        print("Invalid operator. Please use one of: +, -, *, /")


def main():
    print("=" * 50)
    print("Assignment One - Yao Yichuan")
    print("1. Turtle Drawing")
    print("2. QA Bot")
    print("3. Simple Calculator (optional)")
    print("=" * 50)

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        turtle_drawing()
    elif choice == "2":
        qa_bot()
    elif choice == "3":
        simple_calculator()
    else:
        print("Invalid choice. Please run again and enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
