import tkinter,math


def matMul(a,b):
    """Will multiply two matricies together that are 3x3 and return the sum"""
    c = []

    # All these calculcations return the product of any two matricies A * B

    #print("Mat mul called")
    #print("A = ",a)
    #print("B = ",b)
    c.append(a[0] * b[0] + a[1] * b[3] + a[2] * b[6])
    c.append(a[0] * b[1] + a[1] * b[4] + a[2] * b[7])
    c.append(a[0] * b[2] + a[1] * b[5] + a[2] * b[8])

    c.append(a[3] * b[0] + a[4] * b[3] + a[5] * b[6])
    c.append(a[3] * b[1] + a[4] * b[4] + a[5] * b[7])
    c.append(a[3] * b[2] + a[4] * b[5] + a[5] * b[8])
    
    c.append(a[6] * b[0] + a[7] * b[3] + a[8] * b[6])
    c.append(a[6] * b[1] + a[7] * b[4] + a[8] * b[7])
    c.append(a[6] * b[2] + a[7] * b[5] + a[8] * b[8])

    return c

def smallMatMul(a,b):
    """This will multiply a 3*3 matrix by a 3*1 matrix"""
    c = []

    c.append(a[0]*b[0] +  a[1]*b[1] +  a[2]*b[2])
    c.append(a[3]*b[0] +  a[4]*b[1] +  a[5]*b[2])
    c.append(a[6]*b[0] +  a[7]*b[1] +  a[8]*b[2])

    return c



def createLines():
    createdFor = []
    for line in currentlyRenderedPoints:
        for subLine in currentlyRenderedPoints:
            if subLine != line and [line,subLine] not in  createdFor:
                mycanvas.create_line(line[0],line[1],subLine[0],subLine[1])
                createdFor.append([line,subLine])
            

def createVertexPerspective(coordinate):

    matrixA = [1,0,0,0,math.cos(math.radians(cameraBX)),math.sin(math.radians(cameraBX)),0,-math.sin(math.radians(cameraBX)),math.cos(math.radians(cameraBX))]
    matrixB = [math.cos(math.radians(cameraBY)),0,-math.sin(math.radians(cameraBY)),0,1,0,math.sin(math.radians(cameraBY)),0,math.cos(math.radians(cameraBY))]
    matrixC = [math.cos(math.radians(cameraBZ)),math.sin(math.radians(cameraBZ)),0,-math.sin(math.radians(cameraBZ)),math.cos(math.radians(cameraBZ)),0,0,0,1]
    matrixD = [coordinate[0]-cameraX,coordinate[1]-cameraY,coordinate[2]-cameraZ]

    d = smallMatMul (matMul ( matMul(matrixA,matrixB) , matrixC ) , matrixD)

    ex = 10
    ey = 10
    ez = 100

    try:
        x = ((ez / d[2])*d[0])-ex
    except:
        x = 0
    try:
        y = ((ez / d[2])*d[1])-ey
    except:
        y = 0

    x += midX
    y += midY
    mycanvas.create_rectangle(x,y,x,y)

    currentlyRenderedPoints.append([x,y])



allPoints = [[ 10, 10, 10],[ 10, 10,-10],[ 10,-10, 10],[ 10,-10,-10],[-10,10,10],[-10, 10, -10],[-10,-10, 10],[-10,-10,-10]] # These coordinates make a cube

currentlyRenderedPoints = []



def update():
    global currentlyRenderedPoints,cameraY,cameraX,cameraZ,cameraBX,cameraBY,cameraBZ
    mycanvas.delete('all')
    currentlyRenderedPoints = []
    for point in allPoints:

        createVertexPerspective(point)

    createLines()

    #cameraBX += 1

    keyUpdate()
    mywindow.after(16,update)
    
    
##### CANVAS VARIABLES
maxSize = 100
windowScale = 0.5
monitorWidth = 1366
monitorHeight = 768
windowWidth = monitorWidth * windowScale
windowHeight = monitorHeight * windowScale
midX = int(windowWidth / 2)
midY = int(windowHeight / 2)
mywindow = tkinter.Tk()
mycanvas = tkinter.Canvas(width=windowWidth,height=windowHeight)
mycanvas.pack()
#######################


##### CAMERA VARIABLES
cameraX = 0
cameraY = 0
cameraZ = 0


# The bearing that the camera is looking at
cameraBX = 0
cameraBY = 0
cameraBZ = 0

speed = 1
######################


###### KEYBIND VARIABLES

def keyUpdate():
    global cameraX,cameraY,cameraZ,cameraBY,cameraBX,cameraBZ
    if wButton:
        cameraZ -= speed
    if sButton:
        cameraZ += speed
    if aButton:
        cameraX += speed
    if dButton:
        cameraX -= speed
    if pButton:
        cameraBX += speed
    if colonButton:
        cameraBX -= speed
    if lButton:
        cameraBY -= speed
    if quoteButton:
        cameraBY += speed
    if qButton:
        cameraY += speed
    if eButton:
        cameraY -= speed
    print(cameraX,",",cameraY,",",cameraZ)
    

def keyW(event):
    global wButton
    wButton = True
def keyWUp(event):
    global wButton
    wButton = False
def keyA(event):
    global aButton
    aButton = True
def keyAUp(event):
    global aButton
    aButton = False
def keyS(event):
    global sButton
    sButton = True
def keySUp(event):
    global sButton
    sButton = False
def keyD(event):
    global dButton
    dButton = True
def keyDUp(event):
    global dButton
    dButton = False
def keyP(event):
    global pButton
    pButton = True
def keyPUp(event):
    global pButton
    pButton = False
def keyL(event):
    global lButton
    lButton = True
def keyLUp(event):
    global lButton
    lButton = False
def keyColon(event):
    global colonButton
    colonButton = True
def keyColonUp(event):
    global colonButton
    colonButton = False
def keyQuote(event):
    global quoteButton
    quoteButton = True
def keyQuoteUp(event):
    global quoteButton
    quoteButton = False

def keyQ(event):
    global qButton
    qButton = True
def keyQUp(event):
    global qButton
    qButton = False


def keyE(event):
    global eButton
    eButton = True
def keyEUp(event):
    global eButton
    eButton = False
    
wButton = False
aButton = False
sButton = False
dButton = False
pButton = False
lButton = False
quoteButton = False
colonButton= False
qButton = False
eButton = False


mywindow.bind_all("<KeyPress-w>",keyW)
mywindow.bind_all("<KeyPress-W>",keyW)
mywindow.bind_all("<KeyPress-a>",keyA)
mywindow.bind_all("<KeyPress-A>",keyA)
mywindow.bind_all("<KeyPress-s>",keyS)
mywindow.bind_all("<KeyPress-S>",keyS)
mywindow.bind_all("<KeyPress-d>",keyD)
mywindow.bind_all("<KeyPress-D>",keyD)



mywindow.bind_all("<KeyPress-q>",keyQ)
mywindow.bind_all("<KeyPress-Q>",keyQ)
mywindow.bind_all("<KeyPress-e>",keyE)
mywindow.bind_all("<KeyPress-E>",keyE)

mywindow.bind_all("<KeyRelease-q>",keyQUp)
mywindow.bind_all("<KeyRelease-Q>",keyQUp)
mywindow.bind_all("<KeyRelease-e>",keyEUp)
mywindow.bind_all("<KeyRelease-E>",keyEUp)

mywindow.bind_all("<KeyRelease-w>",keyWUp)
mywindow.bind_all("<KeyRelease-W>",keyWUp)
mywindow.bind_all("<KeyRelease-a>",keyAUp)
mywindow.bind_all("<KeyRelease-A>",keyAUp)
mywindow.bind_all("<KeyRelease-s>",keySUp)
mywindow.bind_all("<KeyRelease-S>",keySUp)
mywindow.bind_all("<KeyRelease-d>",keyDUp)
mywindow.bind_all("<KeyRelease-D>",keyDUp)



mywindow.bind_all("<KeyPress-p>",keyP)
mywindow.bind_all("<KeyPress-P>",keyP)
mywindow.bind_all("<KeyPress-l>",keyL)
mywindow.bind_all("<KeyPress-L>",keyL)
mywindow.bind_all("<KeyPress-;>",keyColon)
mywindow.bind_all("<KeyPress-'>",keyQuote)


mywindow.bind_all("<KeyRelease-p>",keyPUp)
mywindow.bind_all("<KeyRelease-P>",keyPUp)
mywindow.bind_all("<KeyRelease-l>",keyLUp)
mywindow.bind_all("<KeyRelease-L>",keyLUp)
mywindow.bind_all("<KeyRelease-;>",keyColonUp)
mywindow.bind_all("<KeyRelease-'>",keyQuoteUp)

update()

mywindow.update()


tkinter.mainloop()
