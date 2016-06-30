import turtle

window=turtle.Screen()
window.bgcolor("red")

def draw_square(some_turtle):
	
	count=4;
	while(count>0):
		some_turtle.forward(100)
		some_turtle.right(90)
		count=count-1
		
def draw_art():
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)

	#angie = turtle.Turtle()
	#angie.shape("arrow")
	#angie.color("blue")
	#angie.circle(100)
	
	#lokie = turtle.Turtle()
	#lokie.shape("turtle")
	#lokie.color("violet")
	#for x in range(0,4):
		#lokie.forward(100)
		#lokie.right(120)

def draw_rhombus(brad):
	oblique = True
	for x in range(0,4):
		brad.forward(60)
		if(oblique):
			brad.right(45)
			oblique=False
		else:
			brad.right(135)
			oblique=True

#draw_square()
draw_art()
	
window.exitonclick()

