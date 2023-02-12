from psychopy import core, event

#################################
# Helper method to wait for a Space key press
# And keep the window open until feedback
#################################

def waitForSpace(win):
    core.wait(1/120)
    c = event.getKeys()
    while 'space' not in c and 'escape' not in c:
        core.wait(1/120)
        c = event.getKeys()
    if 'escape' in c:
        win.close()
        core.quit()
    return

