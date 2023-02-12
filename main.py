from psychopy import visual, core, event
from psychopy import parallel
import runConfigDialog

configDialogBank = runConfigDialog.userInputPlay()

params = {
    'subjectID': configDialogBank[0],
    'practiceTrials': configDialogBank[1],
    'numOfScreensTask1': configDialogBank[2],
    'numOfScreensTask2': configDialogBank[3],
    'startingDistance': configDialogBank[4],
    'fullScreen': configDialogBank[5],
    'joystickSensitivity': configDialogBank[6],
    'screenSize': (1024, 768),
    # 'portAddress': int("0xE050", 16)
}


win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
img = visual.ImageStim(win=win, image="./img/ITI_fixation.jpg", units="pix", opacity=1, size=(params[ 'screenSize'][0], params['screenSize'][1]))
img.draw()
win.update()
core.wait(5)
