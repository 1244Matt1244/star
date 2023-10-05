import turtle

pen = turtle.Turtle()

def cube():
    for i in range(200):
        pen.right(1)
        pen.forward(1) 

def cube():
    pen.fillcolor('yellow')
    pen.begin_fill()
    pen.left(140)
    pen.forward(140)
    cube()
    pen.left(120)
    cube()
    pen.forward(120)
    pen.end_fill()

if __name__ == '__main__':
    cube()
    turtle.done()