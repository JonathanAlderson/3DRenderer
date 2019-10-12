import tkinter,math,time


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
    for i in range(0,len(currentlyRenderedPoints),8):
        for j in range(len(currentlyRenderedPoints[i:i+8])):
            for k in range(len(currentlyRenderedPoints[i:i+8])):
                 mycanvas.create_line(currentlyRenderedPoints[j+i][0],currentlyRenderedPoints[j+i][1],currentlyRenderedPoints[k+i][0],currentlyRenderedPoints[k+i][1])
      
                

def createVertexPerspective(coordinate):
    global ex,ey,ez

    localCameraBX = (cameraBX)
    localCameraBY = (cameraBY)
    localCameraBZ = (cameraBZ)

    matrixA = [ 1                      , 0                      , 0                      ,
                0                      , math.cos(localCameraBX), math.sin(localCameraBX),
                0                      ,-math.sin(localCameraBX), math.cos(localCameraBX)]
    
    matrixB = [ math.cos(localCameraBY), 0                      ,-math.sin(localCameraBY),
                0                      , 1                      , 0                      ,
                math.sin(localCameraBY), 0                      , math.cos(localCameraBY)]
    
    matrixC = [ math.cos(localCameraBZ), math.sin(localCameraBZ), 0                      ,
               -math.sin(localCameraBZ), math.cos(localCameraBZ), 0                      ,
                0                      , 0                      , 1                      ]

    
    matrixD = [coordinate[0]-cameraX,coordinate[1]-cameraY,coordinate[2]-cameraZ]

    d = smallMatMul (matMul ( matMul(matrixA,matrixB) , matrixC ) , matrixD)


    try:
        x = ((ez / d[2])*d[0])-ex
    except:
        x = 0
        #print("Error")
    try:
        y = ((ez / d[2])*d[1])-ey
    except:
        y = 0
        #print("Error")

    x += midX
    y += midY
    mycanvas.create_rectangle(x,y,x,y)
    if( y > 0 and x > 0 and y < windowHeight and x < windowWidth):
        currentlyRenderedPoints.append([x,y])
    else:
        try:
            currentlyRenderedPoints.append(currentlyRenderedPoints[-1])
        except:
            pass


def createCube(allPoints,center,size):

    allPoints.append([center[0]+size,center[1]+size,center[2]+size])
    allPoints.append([center[0]+size,center[1]+size,center[2]-size])
    allPoints.append([center[0]+size,center[1]-size,center[2]+size])
    allPoints.append([center[0]+size,center[1]-size,center[2]-size])
    allPoints.append([center[0]-size,center[1]+size,center[2]+size])
    allPoints.append([center[0]-size,center[1]+size,center[2]-size])
    allPoints.append([center[0]-size,center[1]-size,center[2]+size])
    allPoints.append([center[0]-size,center[1]-size,center[2]-size])
    return allPoints
    


#allPoints = [[ 10, 10, 10],[ 10, 10,-10],[ 10,-10, 10],[ 10,-10,-10],[-10,10,10],[-10, 10, -10],[-10,-10, 10],[-10,-10,-10]] # These coordinates make a cube
allPoints = []

createCube(allPoints,[0,0,0],10)
createCube(allPoints,[0,0,20],10)
createCube(allPoints,[0,20,0],10)
createCube(allPoints,[40,0,0],10)
createCube(allPoints,[60,0,0],10)
createCube(allPoints,[80,0,0],10)
createCube(allPoints,[80,0,20],10)
createCube(allPoints,[80,0,40],10)
createCube(allPoints,[60,0,40],10)
createCube(allPoints,[40,0,40],10)



currentlyRenderedPoints = []



def update():
    global currentlyRenderedPoints,cameraY,cameraX,cameraZ,cameraBX,cameraBY,cameraBZ,timer,ex,ey,ez
    mycanvas.delete('all')
    currentlyRenderedPoints = []
    for point in allPoints:

        createVertexPerspective(point)

    createLines()

    #cameraBX += 1

    keyUpdate()
    frameRate = time.time()-timer
    mywindow.after(1,update)
    
    mywindow.title(("3D Rendering Frame Rate ",round(1/(frameRate))))
    timer = time.time()


    
    
    
##### CANVAS VARIABLES
maxSize = 100
windowScale = 1
monitorWidth = 1366
monitorHeight = 768
windowWidth = monitorWidth * windowScale
windowHeight = monitorHeight * windowScale
midX = int(windowWidth / 2)
midY = int(windowHeight / 2)
mywindow = tkinter.Tk()
mycanvas = tkinter.Canvas(width=windowWidth,height=windowHeight)
mycanvas.pack()

timer = time.time()

#######################


##### CAMERA VARIABLES
cameraX = 0
cameraY = 30
cameraZ = 80

ex = 100
ey = 100
ez = 200


# The bearing that the camera is looking at
cameraBX = 0
cameraBY = 0
cameraBZ = 0

speed = 1
roationSpeed = 0.1
######################




###### KEYBIND VARIABLES

def keyUpdate():
    global cameraX,cameraY,cameraZ,cameraBY,cameraBX,cameraBZ
    
    if wButton:
        cameraZ -= math.cos(cameraBY) * speed
        cameraX -= math.sin(cameraBY) * speed
    if sButton:
        cameraZ += math.cos(cameraBY) * speed
        cameraX += math.sin(cameraBY) * speed
    if aButton:
        cameraZ += math.cos(cameraBY+1.57079) * speed
        cameraX += math.sin(cameraBY+1.57079) * speed
    if dButton:
        cameraZ -= math.cos(cameraBY+1.57079) * speed
        cameraX -= math.sin(cameraBY+1.57079) * speed
    if qButton:
        cameraY += speed
    if eButton:
        cameraY -= speed
        
    if pButton:
        cameraBX += roationSpeed
    if colonButton:
        cameraBX -= roationSpeed
    if lButton:
        cameraBY -= roationSpeed
    if quoteButton:
        cameraBY += roationSpeed


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
