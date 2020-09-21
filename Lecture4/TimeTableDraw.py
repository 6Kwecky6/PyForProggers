import turtle
import math

step = 0
def drawCircle(rad, num_points, pen):
    # placing the circle down by rad to make the center of it origo
    pen.up()
    pen.goto(0,-rad)
    pen.down()
    # Drawing the circle
    pen.circle(rad)
    pen.up()

    #Moves along the circle to yield points
    for it in range(num_points):
        yield [math.sin(step*it)*rad,math.cos(step*it)*rad] #This yields each point 


def drawLine(rad,num_points,cur_point,multiplic,x_pos,y_pos,pen):
    to_pos = [math.sin(step*(cur_point*multiplic%num_points))*rad,math.cos(step*(cur_point*multiplic%num_points))*rad]
    pen.goto(x_pos,y_pos)
    pen.down()
    pen.goto(to_pos[0],to_pos[1])
    pen.up()


def main():
    pen = turtle.Turtle()
    num_points = 300
    rad = 200
    multiplic = 4
    window = turtle.Screen()
    global step # This is the length between each point on the circle
    step = (math.pi * 2) / num_points
    pen.speed(10)
    #Draws the circle
    points = drawCircle(rad,num_points, pen)

    # Draws each line
    for it in range(num_points):
        to_pos = next(points)
        drawLine(rad,num_points,it, multiplic,to_pos[0],to_pos[1],pen)


    window.exitonclick()

if __name__ == '__main__':
    main()