from turtle import Screen, Turtle
screen = Screen()

cordinate = [(0,0), (-20,0), (-40,0),(-60,0),(-80,0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


        self.extend()

    def create_snake(self):

        for position in cordinate:
            self.add(position)
    def add(self,position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
    def relocate(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add(self.segments[-1].position())
    def move(self):

        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
            screen.listen()
        return self.head.forward(20)


    def left(self):

        if self.head.heading() != RIGHT:

            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):

        if self.head.heading() != DOWN:

            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


