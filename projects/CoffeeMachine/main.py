from turtle import Turtle, Screen

timmy = Turtle()
print(Turtle)

timmy.shape('turtle')
timmy.color('green')
timmy.forward(100)

my_screen = Screen()
print(f'{my_screen.canvheight} * {my_screen.canvwidth}')
my_screen.exitonclick()