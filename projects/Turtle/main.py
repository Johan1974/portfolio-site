from turtle import Turtle, Screen
import random



# Draw a Square
square = Turtle()
square.color('green')
square.shape('turtle')
square.speed(0)


screen = Screen()
# Set up screen to not auto-update
# screen.tracer(0)

# Calculate half width and height of the Turtle screen
half_width = screen.window_width() / 2
half_height = screen.window_height() / 2

# Draw a square
square.penup()
square.setpos(-half_width + 10, half_height - 110)
square.pendown()
for _ in range(4):
    square.forward(100)
    square.left(90)
    
# draw a dotted line  
dotline = Turtle()
dotline.color('red')
dotline.shape('arrow')
dotline.penup()
dotline.setpos(-half_width + 10, half_height - 120)
dotline.pendown()
dotline.speed(0)

for _ in range(10):
    dotline.pendown()
    dotline.forward(10)
    dotline.penup()
    dotline.forward(10)


# draw different shapes  
shape = Turtle()
shape.color('blue')
shape.shape('arrow')
shape.speed(0)
shape.penup()
shape.setpos(-half_width + 100, half_height - 420)
shape.pendown()
shape.speed(0)

for i in range(3,10):
    angle = 360 / i
    for _ in range(i):
        shape.forward(100)
        shape.left(angle)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


# randomwalk  
randomwalk = Turtle()
# randomwalk.color('blue')
screen.colormode(255)
# randomwalk.pencolor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
randomwalk.shape('arrow')
randomwalk.pensize(10)
randomwalk.speed(0)
# randomwalk.penup()
# randomwalk.setpos(-half_width + 100, half_height - 420)
# randomwalk.pendown()
randomwalk.setpos(0, half_height - 110)

directions = [0, 90, 180 ,270]
colors = ['red','green','yellow','blue']

for _ in range(100):
    randomwalk.forward(30)
    randomwalk.setheading(random.choice(directions))
    randomwalk.color(random_color())
    # randomwalk.color(random.choice(colors))


# randomwalk  
circles = Turtle()
# randomwalk.color('blue')
screen.colormode(255)
# randomwalk.pencolor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
circles.shape('arrow')
# circles.pensize(10)
circles.speed(0)
circles.circle(120,360)
circles.speed(0)

for _ in range(360):
    circles.circle(120,360)
    circles.left(1)
    circles.color(random_color())

screen.exitonclick()
