# import turtle as t

# screen = t.Screen()
# screen.bgcolor('green')

# road = t.Turtle()
# road.hideturtle()
# road.speed(0)

# def create_rectangle(color,x,y,height,width):
#     road.penup()
#     road.goto(x,y)
#     road.pendown()
#     road.color(color)
#     road.begin_fill()
#     for _ in range(2):
#         road.forward(width)
#         road.right(90)
#         road.forward(height)
#         road.right(90)
      
#     road.end_fill()  

# def create_white_strips():
#     dash = t.Turtle()
#     dash.hideturtle()
#     dash.speed(0)
#     dash.color("white")
#     dash.width(5)
#     dash.penup()
#     dash.goto(0,-600)
#     dash.left(90)
#     for _ in range(30):
#         dash.pendown()
        
#         dash.forward(20)
#         dash.penup()
#         dash.forward(20)
    

# create_rectangle("black",-100,300,600,200)
# create_white_strips()
# t.done()
    
import turtle as t

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('green')

road = t.Turtle()
road.hideturtle()
road.speed(0)

def create_rectangle(color, x, y, height, width):
    road.penup()
    road.goto(x, y)
    road.pendown()
    road.color(color)
    road.begin_fill()
    for _ in range(2):
        road.forward(width)
        road.right(90)
        road.forward(height)
        road.right(90)
    road.end_fill()

def create_white_strips():
    dash = t.Turtle()
    dash.hideturtle()
    dash.speed(0)
    dash.color("white")
    dash.width(5)
    dash.penup()
    dash.goto(0, 300)
    dash.setheading(-90)
    # dash.left(90)
    for _ in range(30):
        dash.pendown()
        dash.forward(30)
        dash.penup()
        dash.forward(30)

def create_car():
    car = t.Turtle()
    car.hideturtle()
    car.speed(1)
    
    car.penup()
    car.goto(-50,-100)
    car.pendown()
    car.color("blue")
    car.begin_fill()
    for _ in range(2):
        car.forward(100)
        car.right(90)
        car.forward(100)
        car.right(90)
    car.end_fill()
    


# Adjusted road size to fill the screen
create_rectangle("black", -150, 300, 600, 300)
create_white_strips()
create_car()
t.done()
