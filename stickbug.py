import turtle as trtl
import time
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
spider.penup()
spider.goto(-20,50)
spider.pendown()
spider.pensize(10)
spider.pencolor("red")
spider.circle(0.01)
spider.penup()
spider.goto(20,50)
spider.pendown()
spider.circle(0.1)
spider.penup()


legs = 6
leglength = 70

legdist = 380 / 6
spider.pensize(5)
spider.goto(0,-1)
spider.pendown()
spider.pencolor("black")
n = 0
while(n < legs):
    spider.goto(0,0)
    spider.setheading(legdist*n)
    spider.forward(leglength)
    n = n + 1
time.sleep(3)
wn = trtl.screen()
wn.mainloop()
