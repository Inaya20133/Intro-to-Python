import turtle

julia=turtle.Turtle()

julia.fillcolor('pink')
julia.pencolor('black')

##julia.begin_fill()
##julia.circle(100)
##julia.end_fill()



julia.write(' (0,0)' )
julia.pendown()
julia.goto(-300,0)
julia.write('(-300, 0)')
julia.goto(300,0)
julia.penup()
julia.write("(300,0)")
julia.goto(0,-300)
julia.pendown()
julia.write("(0,-300)")
julia.goto(0,300)
julia.write("(0,300)")            


julia.shape("turtle")
julia.color("red")

julia.penup()
julia.goto(200,200)

julia.stamp()

julia.color('blue')
julia.goto(250,-250)
julia.write(250,-250)
julia.stamp()

julia.color("green")
julia.goto(0,-100)
julia.write(0,-100)
julia.stamp()

julia.color('pink')
julia.goto(-50,200)
julia.write(-50,200)
julia.stamp()

julia.color('purple')
julia.goto(-200,100)
julia.write(-200,100)
julia.stamp()

julia.color('orange')
julia.goto(-200,-100)
julia.write(-200,100)
julia.stamp()

julia.color('brown')
julia.goto(-300,300)
julia.write(-300.300)
julia.stamp()

julia.color('yellow')
julia.goto(0,300)
julia.write(0,300)
julia.stamp()

julia.color('magenta')
julia.goto(300,0)
julia.write(300,0)
julia.stamp()








