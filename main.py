from psychopy import visual, core, event
import helpers
import runConfigDialog
import pyautogui
from instructionsScreen import show_instructions
import LoggerSetup

log = LoggerSetup.set_up_logger()
configDialogBank = runConfigDialog.user_input_play()

params = {
    'subjectID': configDialogBank[0],
    'practiceTrials': configDialogBank[1],  # Number if Practice Trials, taken from Config Dialog
    'numOfScreensTask1': configDialogBank[2],  # Number of Screens in the 1st task, either 49 (7*7) or 36 (6*6)
    'numOfScreensTask2': configDialogBank[3],  # Number of Screens in the 2nd task, either 49 (7*7) or 36 (6*6)
    'startingDistance': configDialogBank[4],  # Decide whether the starting distance is random, or fixed on 50
    'fullScreen': configDialogBank[5],
    'keyboardMode': configDialogBank[6],
    'joystickSensitivity': configDialogBank[7],
    'screenSize': pyautogui.size() if configDialogBank[5] is True else (1024, 768),  # Get Screen Resolution to match Full Screen
    # 'portAddress': int("0xE050", 16)
}

# Initialize Screen
win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
img = visual.ImageStim(win=win, image="./img/ITI_fixation.jpg", units="pix", opacity=1,
                       size=(params['screenSize'][0], params['screenSize'][1]))
img.draw()
win.update()
helpers.wait_for_space(win)

print(helpers.display_vas(win, params, "How excited are you??", ["טעמ", "הברה"]))

show_instructions(win, img, params)

# Initialize DataFrame

# Initialize Sensors

# Run VAS

# Show Instructions

# Practice run

# Task 1

# Mid-VAS

# Task 2

# Final VAS

# Recap
