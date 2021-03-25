"""
KinkySpiral - Python Turtle
By A.D. Tejpal - 25-Mar-2021

This is a Python-Turtle program demonstrating drawing of spirals
made up of kinky spokes.

The user has the option to try out variations in density of spokes as
well as their kink angle.

Fresh rounds of graded color animation keep taking place at short
intervals.
"""
import turtle as tt
import turtle_udf as tf
import sys
import time

# Create instances of  Turtle() and Screen() classes
tu1 = tt.Turtle()  # For Spiral
tu2 = tt.Turtle()  # For Overall Heading & Labels
tu3 = tt.Turtle()  # For Particulars Of Current Music Track
tu4 = tt.Turtle()  # For Current Volume Level
ts = tt.Screen()

# Following statement is needed for permitting RGB style color values
# Using Turtle() object (like tu1) instead of tt below, would attract error.
tt.colormode(255)

# Globals
isPlayOn = True
grpSize = 180
spiralSize = 90
bendAngle = 35
colorIndexSpiral = 0
colorIndexScreen = 0
lbWidth = 114
isExitMode = False

lbAreaList = []  # Holds label coordinates (for checking mouse click)
colorListSpiral = [(0, 0, 255), (173, 216, 230),
                   (0, 0, 128), (165, 42, 42, 255), (139, 69, 19),
                   (255, 215, 0), (0, 255, 0), (176, 176, 176),
                   (240, 240, 255), (255, 52, 179), (205, 102, 0),
                   (255, 105, 180), (155, 48, 255), (255, 0, 0),
                   (255, 255, 0)]
colorCountSpiral = len(colorListSpiral)

colorListScreen = [(240, 240, 244), (208, 208, 221), (174, 174, 198),
                   (234, 235, 236), (210, 213, 215), (188, 192, 194),
                   (175, 180, 182), (235, 237, 233), (216, 220, 211),
                   (198, 203, 190), (175, 183, 164), (233, 232, 236),
                   (205, 203, 211), (180, 176, 189), (160, 155, 172),
                   (234, 234, 234)]
colorCountScreen = len(colorListScreen)

"""
# Maximize turtle window with suitable title
tf.TurtleInitialSettings(tt, "Georgia's Spirals - Python-Turtle")
"""

# Simulate turtle window to full screen
tf.TurtleInitialSettings(tt, "", isFullScreen=True)

# Set turtle screen color (first one in color list)
ts.bgcolor(colorListScreen[0])

# Set animation speed
# 0 for instantaneous, otherwise 1 (min) to 10 (max)
tu1.speed(0)
tu2.speed(0)
tu3.speed(0)
tu4.speed(0)
tu1.pensize(2)  # For Spirals

# Hide Turtles
# For un-hiding the turtles, use showturtle command like tu1.st()
tu1.ht()
tu2.ht()
tu3.ht()
tu4.ht()

# Make Labels:
lbList = [["RESUME", "green"], ["STOP", "red"],
          ["KINKIER", "black"], ["FLATTER", "black"],
          ["MORE", "black"], ["LESS", "black"], ["EXIT", "red"]]

# txtPosition=1 results in positioning the text at top left corner.
pos = tf.PositionText(tt, txtPosition=1, vMargin=105)

for s in lbList:
    tf.GoToPos(tu2, pos)
    lbAreaList.append(tf.MakeLabel(tu2, txtString=s[0], 
                 txtAlign="center", fontColor=s[1],
                 fontName="Times New Roman",
                 fontSize=14, fontWt="bold",
                  labelWd=lbWidth, labelHt=30,
                  borderThickness=4, borderColor="blue", topMargin=11))

    pos = (pos[0], pos[1] - 50)

# Main Heading - Below The Last Label
pos = (pos[0] + 75, pos[1] - 65)
tf.GoToPos(tu2, pos)
tf.ShowText(tu2, "Spokes",
            txtAlign="center", fontColor="blue",
            fontSize=28, fontWt="bold")

pos = (pos[0], pos[1] - 40)
tf.GoToPos(tu2, pos)
tf.ShowText(tu2, "Spirals",
            txtAlign="center", fontColor="blue",
            fontSize=28, fontWt="bold")

#==========Function Code Block-Start=======
def ShowStatus():
    """
    Displays the Spiral Size & Group Size
    """
    global grpSize, bendAngle

    tu3.clear()
    
    # Update Group Size
    pos = tf.PositionText(tt, txtPosition=1, vMargin=37)
    tf.GoToPos(tu3, pos)
    tf.ShowText(tu3, "Number Of Spokes: " + str(grpSize), 
                txtAlign="left", fontColor="black", fontSize=14)

    # Update Kink Ange
    pos = (pos[0], pos[1] - 25)
    tf.GoToPos(tu3, pos)
    tf.ShowText(tu3, "Kink Angle: " + str(bendAngle), 
                txtAlign="left", fontColor="black", fontSize=14)

def DrawSpokeSpiral(TurtleObject, 
                cRed=255, cGreen=0, cBlue=0):
    """
    For using RGB style for colors, the calling code should have
    prior statement like following:
    turtle.colormode(255)
    """
    global isPlayOn, spiralSize, grpSize, bendAngle
    
    tu = TurtleObject
    pX = lbWidth / 2

    # Store original values
    cr = cRed
    cg = cGreen
    cb = cBlue
    r = spiralSize
    
    clrStep = 8  # Progressive darkening / brightening
    stepAngle = 360/grpSize

    # Six sectors - for alternate darkening / brightening
    s1 = int(grpSize * (1/6))
    s2 = int(grpSize * (2/6))
    s3 = int(grpSize * (3/6))
    s4 = int(grpSize * (4/6))
    s5 = int(grpSize * (5/6))
    s6 = grpSize

    for n in range(grpSize):
        if not isPlayOn:
            break

        tu.pencolor(cRed, cGreen, cBlue)        
        
        tu.penup()
        tu.setposition(pX, 0)  # for proper centering (allowing for label width)
        tu.pendown()
        tu.forward(r)

        for m in range(4):
            if m%2 > 0:
                tu.left(bendAngle)
            else:
                tu.right(bendAngle)
            tu.forward(0.5 * r)

        tu.right(stepAngle)
        
        if (n in range(s1)
            or n in range(s2, s3)
            or n in range(s4, s5)):
            # Progressive darkening of color in each cycle
            if cRed > (clrStep + 5):
                cRed = cRed - clrStep
            if cGreen > (clrStep + 5):
                cGreen = cGreen - clrStep
            if cBlue > (clrStep + 5):
                cBlue = cBlue - clrStep
        else:
            # Progressive increase of color in each cycle
            if cRed < (cr - clrStep + 1):
                cRed = cRed + clrStep
            if cGreen < (cg - clrStep + 1):
                cGreen = cGreen + clrStep
            if cBlue < (cb - clrStep + 1):
                cBlue = cBlue + clrStep

# Draw Spiral
def DrawSpiral():
    global colorIndexSpiral, colorListSpiral, colorCountSpiral
    global colorIndexScreen, colorListScreen, colorCountScreen
    global musicIndex, musicCount, mVol
    global musicListFullPaths, musicListFileNames
    global isPlayOn, isExitMode, spiralSize, grpSize, spiralType
    """
    Apparently, global declaration is not needed for object variables.
    """    
    while True:
        if isExitMode:
            break
        
        if not isPlayOn:
            # Discontinue & display Stop notice
            tu3.clear()        
            pos = tf.PositionText(tt, txtPosition=1, vMargin=35)
            tf.GoToPos(tu3, pos)
            tf.ShowText(tu3,
                        "Play Stopped: Click RESUME To Start Afresh" , 
                        txtAlign="left", fontColor="red", fontSize=14)
            break
        
        # Display Status:
        ShowStatus()
        
        # Set screen color as per color list
        clr = colorListScreen[colorIndexScreen]
        ts.bgcolor(clr)
        
        # Set spiral color as per color list
        clr = colorListSpiral[colorIndexSpiral]
        rr = clr[0]
        gg = clr[1]
        bb = clr[2]

        DrawSpokeSpiral(tu1,
                    cRed=rr, cGreen=gg, cBlue=bb)

        colorIndexSpiral = colorIndexSpiral + 1
        if colorIndexSpiral > (colorCountSpiral - 1):
            colorIndexSpiral = 0

        colorIndexScreen = colorIndexScreen + 1
        if colorIndexScreen > (colorCountScreen - 1):
            colorIndexScreen = 0

        time.sleep(2)

def CallSpirals():
    tu1.home()
    tu1.fd(lbWidth/2)
    tu1.clear()
    tu3.clear()
    DrawSpiral()

# Function for use in mouse click event
def ClickAction(x, y):
    global lbAreaList, isPlayOn, isExitMode
    global colorIndexSpiral, colorIndexScreen
    global colorCountSpiral, colorCountScreen
    global spiralSize, grpSize, bendAngle

    lbResume = lbAreaList[0]
    lbStop = lbAreaList[1]
    lbKinkier = lbAreaList[2]
    lbFlatter = lbAreaList[3]
    lbMore = lbAreaList[4]
    lbLess = lbAreaList[5]
    lbExit = lbAreaList[6]
    if (x in range(lbResume[0], lbResume[2]) 
                  and y in range(lbResume[3], lbResume[1])):
        if not isPlayOn:
            isPlayOn = True
            CallSpirals()

    elif (x in range(lbStop[0], lbStop[2]) 
                  and y in range(lbStop[3], lbStop[1])):
        isPlayOn = False      

    elif (x in range(lbKinkier[0], lbKinkier[2]) 
                  and y in range(lbKinkier[3], lbKinkier[1])):
        bendAngle = bendAngle + 10
        if bendAngle > 55:
            bendAngle = 55
        else:
            CallSpirals()

    elif (x in range(lbFlatter[0], lbFlatter[2]) 
                  and y in range(lbFlatter[3], lbFlatter[1])):
        bendAngle = bendAngle - 10
        if bendAngle < 15:
            bendAngle = 15
        else:
            CallSpirals()

    elif (x in range(lbMore[0], lbMore[2]) 
                  and y in range(lbMore[3], lbMore[1])):          
        grpSize = grpSize + 10
        if grpSize > 210:
            grpSize = 210
        else:
            CallSpirals()
        
    elif (x in range(lbLess[0], lbLess[2]) 
                  and y in range(lbLess[3], lbLess[1])):
        grpSize = grpSize - 10
        if grpSize < 20:
            grpSize = 20
        else:
            CallSpirals()

    elif (x in range(lbExit[0], lbExit[2]) 
                  and y in range(lbExit[3], lbExit[1])):
        isExitMode = True
        
        if isPlayOn:
            isPlayOn = False
            tu4.clear()

            pos =(lbExit[2] + 10, lbExit[3])
            tf.GoToPos(tu4, pos)
            tf.ShowText(tu4,
                        "Please Click Exit Again" , 
                        txtAlign="left", fontColor="red", fontSize=14)

        else:
            # Prevents trace-back error messages on python shell
            time.sleep(1)
            # Close turtle window
            ts.bye()
            sys.exit()

#==========Function Code Block-End========

# Call function ClickAction() on mouse click
# (Use of tt (i.e. turtle) or tu (i.e. turtle.Turtle())
# instead of ts (turtle.Screen()) would cause error)
ts.onclick(ClickAction)  # (A)

"""
Imp:  Line (B) below, meant for drawing the spirals
has to AFTER the mouse-click event line (A) above.
If (B) is placed before (A), the mouse click event stops responding
"""
DrawSpiral()

# mainloop() tells the window to wait for the user to do something
# It serves to prevent automatic disappearance of turtle window
# (when run in other than IDLEX) immediately after execution.
tt.mainloop()

"""
The statement below also serves to prevent automatic disappearance of turtle window immediately after execution.
However, tt.mainloop() is preferred in this module as mouse click event is needed otherwise.
tt.exitonclick()

Note: Code for a function should precede the calling code
"""
