from turtle import Turtle, Screen

timmy_turtle = Turtle()

# 거북이 모양 노출 가능
timmy_turtle.shape("turtle")
timmy_turtle.color("red") # 색상 변경


# 거북이가 특정 동작을 하게 하기
timmy_turtle.forward(100)



screen = Screen()
screen.exitonclick()