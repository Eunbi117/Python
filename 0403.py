import turtle as t
import random
score = 0
playing = False
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)
talk = t.Turtle()
talk.shape("arrow")
talk.color("black")
talk.speed(0)
talk.ht()
talk.up()
talk.goto(0, 0)
def turn_right():
    t.setheading(0)
def turn_up():
    t.setheading(90)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)
def start():
    import time
    global playing
    global starttime
    if playing == False:
        starttime=time.time()
        playing = True
        t.clear()
        play()
        
def play():
      import time
      global score
      global playing
      global starttime
      t.forward(11)

      if random.randint(1, 7) == 1 :
            ang = te.towards(t.pos())
            te.setheading(ang)

      if t.distance(te) < 12 :
            time = str(time.time()-starttime)
            text = "Score : " + time[:time.find('.')+2]+"'s"
            message("Game Over", text)
            playing = False
            score = 0
            
#------------------------위치-------------
            y = t.ycor()
            x = t.xcor()

            if y>230:
                  t.sety(-230)
            if y<-230:
                  t.sety(-230)
            if x>230:
                  t.setx(230)
            if x<-230:
                  t.setx(-230)
            if playing:
                  talk.goto(180,180)
                  time = time.time()-starttime
                  speed = time + 5
            if speed > 12:
                  speed = 12
                  te.forward(speed)
                  talk.clear()
                  time = str(time)
                  time = (time)[:time.find('.')+2]
                  talk.write(time+"'s", False, "center", ("", 40))

                  t.ontimer(play, 1)
            elif not playing:
                  import time
                  time.sleep(2)
                  finish()

def message(m1, m2):
      t.clear()
      t.goto(0, 100)
      t.write(m1, False, "center", ("", 20))
      t.goto(0, -100)
      t.write(m2, False, "center", ("", 15))
      t.home()

def finish():
      t.bye()
    
t.title("Turtle Run")
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]")
