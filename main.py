
import time
from turtle import Screen


from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
Score = ScoreBoard()
screen.listen()
screen.onkey(fun=snake.left, key='a')
screen.onkey(fun=snake.right, key='d')
screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.down, key='s')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        Score.increase()
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        Score.reset()
        snake.relocate()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            Score.reset()
            snake.relocate()



screen.exitonclick()
