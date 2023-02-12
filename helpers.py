from psychopy import core, event

#################################
# Helper method to wait for a Space key press
# And keep the window open until feedback
#################################

def waitForSpace():
    core.wait(1/120)
    c = event.getKeys()
    while 'space' not in c:
        core.wait(1/120)
        c = event.getKeys()
    return

