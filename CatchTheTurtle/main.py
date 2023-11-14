import turtle
import random

screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Python Turtle Graphics")
FONT =('Arial',30,'normal')
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
score = 0

turtle_list = []
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("black")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score : 0",move=False,align="center",font=FONT)

def setup_countdown_turtle():
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setpos(100, y)  # Sürenin pozisyonunu sağ üste ayarla
    countdown_turtle.write(arg="Time: 10", move=False, align="center", font=FONT)

grid_size =10
def make_turtle(x,y):
    t = turtle.Turtle()

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("black")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-10,0,10,20]


def handle_click(x, y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtles():
    hide_turtles()
    random.choice(turtle_list).showturtle()
    screen.ontimer(show_turtles,500)




def countdown(time):
    countdown_turtle.hideturtle()
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.write(arg="Time : {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda : countdown(time - 1),1000)
    else:
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over !", move=False, align="center", font=FONT)



turtle.tracer(0)

setup_score_turtle()
setup_countdown_turtle()
setup_turtles()
hide_turtles()
show_turtles()
countdown(10)

turtle.tracer(1)



turtle.mainloop()