#use these functions to make your buffers work. 

#use this function to make new buffer for valid points only
def buffer(win, center, buflist, size, wordLength):
    #the height and the length for each rectangle surrounding the word 
    width = int(size*wordLength)
    height = int(size)

    #the x and y coordinates of the random point we are testing 
    x = center.getX()
    y = center.getY()
    #making the buffer rectangle 
    buffRectangle = Rectangle(Point(x-width, y-height), Point(x+width, y+height))
    #appending the buffer for other points 
    bufList.append(buffRectangle)

#use this function to see if a point is valid for a new word 
def touches(bufferList, point):
    for rectangles in buffList:
        if isClicked(rectangles, point) == True:
            return True
    return False

#we did this in class!
def isClicked(buffer, point):
    p1 = buffer.getP1()
    p2 = buffer.getP2()
    
    x = point.getX()
    y = point.getY()

    if x > p1.getX() and x < p2.getX() and y > p1.getY() and y < p2.getY():
        return True
    return False 
