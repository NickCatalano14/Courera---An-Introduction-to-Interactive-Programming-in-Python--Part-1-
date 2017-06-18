# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 14
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True



# initialize ball_pos and ball_vel for new bal in middle of table

ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [0,1]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH/2,HEIGHT/2]
    
    if direction == True:
        ball_vel[0] = -random.randrange(120,240) / 100 
    else:
        ball_vel[0] = random.randrange(120,240) / 100 

    ball_vel[1] = -random.randrange(60, 180) / 100    
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = [0,HEIGHT/2]
    paddle2_pos = [WIDTH,HEIGHT/2]
    
    paddle1_vel = 0
    paddle2_vel = 0
    
    score1=0
    score2=0
    
    spawn_ball(0)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
        
   
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "Black")

    # update paddle's vertical position, keep paddle on the screen
    
    if (paddle1_pos[1] <= HEIGHT - HALF_PAD_HEIGHT and paddle1_vel > 0) or (paddle1_pos[1] >= HALF_PAD_HEIGHT and paddle1_vel < 0) :
        paddle1_pos[1] += paddle1_vel 
        
    elif (paddle2_pos[1] <= HEIGHT - HALF_PAD_HEIGHT and paddle2_vel > 0) or (paddle2_pos[1] >= HALF_PAD_HEIGHT and paddle2_vel < 0) :
        paddle2_pos[1] += paddle2_vel 
        
    # draw paddles
    canvas.draw_line([paddle1_pos[0],paddle1_pos[1]-HALF_PAD_HEIGHT], [paddle1_pos[0],paddle1_pos[1]+HALF_PAD_HEIGHT], 20, 'Red')
    canvas.draw_line([paddle2_pos[0],paddle2_pos[1]-HALF_PAD_HEIGHT], [paddle2_pos[0],paddle2_pos[1]+HALF_PAD_HEIGHT], 20, 'Blue')
    
    # determine whether paddle and ball collide
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1
    
    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) or ball_pos[0] >= (WIDTH - (PAD_WIDTH + BALL_RADIUS)):        
        ball_vel[0] *= -1
        
        
        if (ball_pos[0] < WIDTH/2):    
            if (ball_pos[1] <  paddle1_pos[1]-HALF_PAD_HEIGHT or ball_pos[1] >  paddle1_pos[1]+HALF_PAD_HEIGHT):
                score1 += 1
                spawn_ball(LEFT)
            else:
                ball_vel[0] += 0.2
                
  
        if (ball_pos[0] > WIDTH/2):    
            if (ball_pos[1] <  paddle2_pos[1]-HALF_PAD_HEIGHT or ball_pos[1] >  paddle2_pos[1]+HALF_PAD_HEIGHT):
                score2 += 1
                spawn_ball(RIGHT)        
            else:
                ball_vel[0] += 0.2
    
    
    # draw scores
    
    canvas.draw_text(str(score1), [250, 50], 50, "red")    
    canvas.draw_text(str(score2), [325, 50], 50, "blue")
    
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    vel = 4
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = vel  


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 150)


# start frame
new_game()
frame.start()
