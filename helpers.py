from psychopy import core, event


def waitForSpace():
    core.wait(1/120)
    c = event.getKeys()
    while 'space' not in c:
        core.wait(1/120)
        c = event.getKeys()
    return

