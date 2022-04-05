from turtle import Screen
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Yuran Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")




#Animating our snake, adding Moves to the sanke
game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  #Detect Collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
  
  #Detect Collison with the wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False
    scoreboard.game_over()

  #Detect Collison with the tail
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()
  









screen.exitonclick()