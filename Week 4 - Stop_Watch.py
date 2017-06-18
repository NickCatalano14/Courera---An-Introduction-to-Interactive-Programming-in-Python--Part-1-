# template for "Stopwatch: The Game"

import simplegui


# define global variables

stop = True
conv_seconds = 100
counter = 0
num_stops = 0
num_wins = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = (t) % 10
    seconds = int(t/10) % 10
    minutes = int(t / 600) % 600
    tens = int(t / 100) % 6
    string = str(minutes) + ":" + str(tens) + str(seconds) + "." + str(tenths)
    return string
    
    
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def Start():
    global counter, stop
    counter += 1
    stop = False
    timer.start()
    
def Stop():
    global stop, counter, num_wins, num_stops
    
    stop = True
    timer.stop()
    
    if counter % 10 == 0 and counter != 0:
        num_wins += 1
        num_stops += 1
    else:
        num_stops += 1

def Reset():
    global counter, num_stops, num_wins
    timer.stop()
    counter = 0
    num_stops = 0
    num_wins = 0
    stop = True

# define event handler for timer with 0.1 sec interval
def run():
    global counter
    counter += 1
   
# define draw handler
def draw(canvas):
    text = format(counter)
    canvas.draw_text( text, (75, 100), 50, "white")
    canvas.draw_text(str(num_wins) + '/' + str(num_stops), (250, 25), 30, "white")
   
    
# create frame
frame = simplegui.create_frame("Stopwatch game", 300, 200)

# register event handlers
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(conv_seconds, run)

# start frame
frame.start()
Reset()



# Please remember to review the grading rubric
