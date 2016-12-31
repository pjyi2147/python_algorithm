
import turtle

def tree(branchLen, pensize, t):
    t.pensize(pensize)
    angle = 30
    if branchLen > 5 and pensize > 2:
        t.color('green')
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-15, pensize-2, t)
        t.left(angle*2)
        tree(branchLen-15, pensize-2, t)
        t.right(angle)
        t.pensize(pensize)

        if branchLen > 20:
            t.color('brown')
        
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(100, 15, t)
    myWin.exitonclick()

main()
