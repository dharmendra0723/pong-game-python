import turtle

class Bounce:
	"""docstring for Bounce"""
	def __init__(self, name):
		# Create the Window
		self.screen = turtle.Screen()
		self.screen.title(name)
		self.screen.bgcolor('black')
		self.screen.setup(width=800, height=600)
		self.screen.tracer(0)

		# Create the Paddle and setup position
		self.paddle = turtle.Turtle()
		self.paddle.speed(0)
		self.paddle.shape('square')
		self.paddle.color('white')
		self.paddle.shapesize(stretch_wid=1, stretch_len=5)
		self.paddle.penup()
		self.paddle.goto(0, -280)

		# Add Ball
		self.ball = turtle.Turtle()
		self.ball.speed(0)
		self.ball.penup()
		self.ball.shape('circle')
		self.ball.color('white')
		self.ball.goto(0, 290)
		# Movement of Ball
		self.ball.dx = 0.5
		self.ball.dy = 0.5

		#Add Key Listener
		self.screen.listen()
		self.screen.onkeypress(self.paddle_left,"Left")
		self.screen.onkeypress(self.paddle_right,"Right")

	def paddle_left(self):
		x = self.paddle.xcor()
		x += -25
		if x < -360:
			x = -360
		self.paddle.setx(x)
	def paddle_right(self):
		x = self.paddle.xcor()
		x += 25
		if x > 350:
			x = 350
		self.paddle.setx(x)

	def start(self):

		

		while True:

			self.screen.update()
			self.ball.setx(self.ball.xcor()+self.ball.dx)
			self.ball.sety(self.ball.ycor()+self.ball.dy)

			# Ball Boundry Check
			if self.ball.ycor()>290:
				self.ball.sety(290)
				self.ball.dy*=-1
			if self.ball.ycor()<-290:
				self.ball.setx(0)
				self.ball.sety(250)

			if self.ball.xcor()>390:
				self.ball.setx(390)
				self.ball.dx*=-1
			if self.ball.xcor()<-390:
				self.ball.setx(-390)
				self.ball.dx*=-1

			# Paddle Ball Collision
			if (self.ball.ycor()<-260 and (self.ball.xcor()<self.paddle.xcor()+40 and self.ball.xcor()>self.paddle.xcor()-40)):
				self.ball.sety(-260)
				self.ball.dy*=-1




def main():
	b = Bounce('Pong Game')
	b.start()


if __name__ == '__main__':
	main()
