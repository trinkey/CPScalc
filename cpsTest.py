import turtle, time

screen, display, clicks, t, end = turtle.Screen(), turtle.Turtle(), 0, 0, 0

screen.setup(1000,1000)
screen.bgcolor("#333333")

display.hideturtle()
display.color("#FFFFFF")
display.write("Click to start.", align = "center", font = ["Arial", 50, "normal"])

screen.tracer(0)

def addClick(x, y):
    global clicks, display, t, end, screen
    display.clear()
    if clicks == 0:
        t = time.time()
    clicks += 1
    m = "Clicks: " + str(clicks)
    display.write(m, align = "center", font = ["Arial", 50, "normal"])
    screen.update()

def end():
    global end, display, t, screen, die
    if clicks != 0:
        end = 1
        screen.onclick(None)
        time.sleep(0.1)
        display.clear()
        m = "Your CPS: " + str(round(clicks / (time.time() - t) * 10) / 10)
        display.clear()
        display.write(m, align = "center", font = ["Arial", 50, "normal"])
        display.pu()
        display.speed(0)
        display.goto(0, -100)
        display.color("#999999")
        display.write("Press space to close.", align = "center", font = ["Arial", 25, "normal"])
        screen.update()
        screen.onkey(die, "space")

def die():
    global screen
    screen.bye()

screen.onclick(addClick)
screen.onkey(end, "space")
screen.listen()
screen.mainloop()