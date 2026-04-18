import turtle

# Ekran ayarı
ekran = turtle.Screen()
ekran.bgcolor("black")

t = turtle.Turtle()
t.color("red")
t.width(3)
t.speed(3)

# Kalp çizimi
t.begin_fill()
t.left(140)
t.forward(180)

t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)

t.forward(180)
t.end_fill()

# Yazı yazma
t.penup()
t.goto(0, 150)
t.color("white")
t.write("Seni Seviyorum...", align="center", font=("Arial", 25, "bold"))

t.hideturtle()

turtle.done()