from turtle import Turtle, Screen
import time, random


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SPEED = 0.1
MOVE_PIXEL = 20
game_on = True
skip_move = False
    

class Snake:
    def __init__(self):
        self.segment_list = []
        self.segment()
        self.head = self.segment_list[0]


    def segment(self):

        for i in range(3):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            
            if i > 0:
                x_coor = int(self.segment_list[i-1].position()[0]) - 20
                segment.goto(x_coor, 0)

            self.segment_list.append(segment)


    def extend(self):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()

        self.segment_list.append(segment)

    
    def move(self):
        global skip_move
        
        if skip_move == True:
            skip_move = False
        else:
            for i in range(len(self.segment_list)-1, 0, -1):
                x_coor = self.segment_list[i-1].position()[0]
                y_coor = self.segment_list[i-1].position()[1]
                self.segment_list[i].goto(x_coor, y_coor)
            self.head.forward(MOVE_PIXEL)
        
            screen.update()

            time.sleep(SPEED)


    def up(self):
        global skip_move
        if self.head.heading() != DOWN:   
            self.head.setheading(UP)
        for i in range(len(self.segment_list)-1, 0, -1):
            x_coor = self.segment_list[i-1].position()[0]
            y_coor = self.segment_list[i-1].position()[1]
            self.segment_list[i].goto(x_coor, y_coor)
        self.head.forward(MOVE_PIXEL)
        screen.update()
        time.sleep(SPEED)
        skip_move = True
        


    def down(self):
        global skip_move
        if self.head.heading() != UP:   
            self.head.setheading(DOWN)
        for i in range(len(self.segment_list)-1, 0, -1):
            x_coor = self.segment_list[i-1].position()[0]
            y_coor = self.segment_list[i-1].position()[1]
            self.segment_list[i].goto(x_coor, y_coor)
        self.head.forward(MOVE_PIXEL)
        screen.update()
        time.sleep(SPEED)
        skip_move = True
        


    def left(self):
        global skip_move
        if self.head.heading() != RIGHT:   
            self.head.setheading(LEFT)
        for i in range(len(self.segment_list)-1, 0, -1):
            x_coor = self.segment_list[i-1].position()[0]
            y_coor = self.segment_list[i-1].position()[1]
            self.segment_list[i].goto(x_coor, y_coor)
        self.head.forward(MOVE_PIXEL)
        screen.update()
        time.sleep(SPEED)
        skip_move = True
        


    def right(self):
        global skip_move
        if self.head.heading() != LEFT:   
            self.head.setheading(RIGHT)
        for i in range(len(self.segment_list)-1, 0, -1):
            x_coor = self.segment_list[i-1].position()[0]
            y_coor = self.segment_list[i-1].position()[1]
            self.segment_list[i].goto(x_coor, y_coor)
        self.head.forward(MOVE_PIXEL)
        screen.update()
        time.sleep(SPEED)
        skip_move = True
        


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.refresh()

    def refresh(self):
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        x_coor = random.randint(-280, 280)
        y_coor = random.randint(-280, 250)
        self.goto(x_coor, y_coor)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = -1
        
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        
        self.refresh()

    
    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", align="center", font=("Consolas", 10, "normal"))
        

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color("gray")
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Consolas", 30, "normal"))
        global game_on
        game_on = False


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

while game_on:

    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    screen.listen()
        
    snake.move()

    if snake.head.distance(food) < 20:
        snake.extend()
        food.refresh()
        scoreboard.refresh()

    for i in snake.head.position():
        if i > 300 or i < -300:
            scoreboard.game_over()
    
    for segment in snake.segment_list[1::]:
        if snake.head.distance(segment) < 10 :
            scoreboard.game_over()

screen.mainloop()