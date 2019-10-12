import tkinter





def createVertex(coordinate):
    mycanvas.create_rectangle(coordinate[0]/coordinate[2],coordinate[1]/coordinate[2],coordinate[0]/coordinate[2],coordinate[1]/coordinate[2],fill="red")

def createVertexOrthographic (coordinate):
    global xyProjections
    
    scaleFactorX = coordinate[0] / coordinate[2]
    scaleFactorY = coordinate[1] / coordinate[2]
    x = scaleFactorX * coordinate[0] + cameraX  + midX
    y = scaleFactorY * coordinate[2] + cameraZ  + midY
    print("X = ",x," Y = ",y)
    mycanvas.create_rectangle(x,y,x,y,fill="red")
    

def createLines():
    for coord in xyProjections:

        for subCoord in xyProjections:

            mycanvas.create_line(coord[0],coord[1],subCoord[0],subCoord[1])


allPoints = [[0,0,1],
             [10,0,1],[-10,0,1],
             [0,10,1],[0,-10,1],
             [0,0,10],[0,0,-10],
             ]

allPoints = [     [ 10, 10, 10],[ 10, 10,-10],[ 10,-10, 10],
                  [ 10,-10,-10],[-10,10,10],[-10, 10, -10],
                  [-10,-10, 10],[-10,-10,-10]

            ]

xyProjections = []




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
######################




for point in allPoints:

    createVertexOrthographic(point)

mywindow.update()


tkinter.mainloop()
