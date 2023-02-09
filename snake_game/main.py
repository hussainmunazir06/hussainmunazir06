import turtle
import random
import time
import snake
import food
import scoreboard

# all_turtles = []
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
# x_axis = 0
# for turtles in range(3):
#     tom = turtle.Turtle(shape="square")
#     tom.color("white")
#     tom.penup()
#     tom.goto((x_axis, 0))
#     all_turtles.append(tom)
#     x_axis -= 20

snake = snake.Snake()
food = food.Food()

score = scoreboard.ScoreBoard()
game_is_on = True
screen.setup(width=600, height=600)

while game_is_on:
    screen.update()
    time.sleep(0.2)
    
    screen.onkey(key="Up", fun=snake.forward_move)
    screen.onkey(key="Left", fun=snake.left_move)
    screen.onkey(key="Right", fun=snake.right_move)
    screen.onkey(key="Down", fun=snake.down_move)
    
    snake.move()
    if snake.all_turtles[0].distance(food) < 15:
        food.refresh()
        snake.add_tail()
        score.add_score()
        # score += 1
    if snake.all_turtles[0].xcor() > 310 or snake.all_turtles[0].xcor() < -310 or snake.all_turtles[0].ycor() > 310 or snake.all_turtles[0].ycor() < -310:
        game_is_on = False
        score.game_over()

    for turtles in snake.all_turtles[2:]:
        # if turtles == snake.all_turtles[0] or turtles == snake.all_turtles[1]:
        #     pass
        # elif snake.all_turtles[0].distance(turtles) < 10:
        #     game_is_on = False
        #     score.game_over()

        if snake.all_turtles[0].distance(turtles) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()