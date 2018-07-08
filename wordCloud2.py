'''
word cloud. This program reads a text file, finds the frequency of each of the
words excluding the articles and other unnecessary words like pronouns. It then
creates a word cloud of the words by diplaying the words graphically in a set
window according to the frequency of the words.
'''
from random import*
from graphics import*
from time import*

def main():

    win = GraphWin('wordCloud', 600, 600)
  

    intro(win, 'Welcome!', Rectangle(Point(200, 200), Point(400, 400)), 25)
    message = 'This program generates a word\n cloud out of an inputted text file.\n An initial text file is already in\n place for you. You can try other\n files of your choice by entering\n another text file name in the\n filename field.'
    intro(win, message, Rectangle(Point(100, 100), Point(500, 500)), 20, move = False)

    filename = Text(Point(150, 50), 'filename')
    filename.draw(win)     
    
    fileEnt = Entry(Point(300, 50), 20)
    fileEnt.setText('jekyll.txt') 
    fileEnt.draw(win)

    quitIt = drawButton(win, Point(350, 450), Point(450, 500), 'Quit')
   

   
    sortedWords, total = fileWords(fileEnt.getText())
    maxFreq = sortedWords[0][1]/total

    bufferList = []
   
    for vals in sortedWords[0:20]:
        cloud(win, vals[0], sizeVal(vals[1]/total, maxFreq), bufferList)
        print(vals[0], sizeVal(vals[1]/total, maxFreq))
        print(len(bufferList))
  
def keyVal(tupList):
    return tupList[1]

def fileWords(file):
##  file = input('Give me a file you want to try? ') 
    text = open(file, 'r', encoding = 'utf-8')
    textStr = text.read().lower()
    char = '!@#$%^&*()~`{}-[];:<>,./?"'

    for letters in textStr:
        if letters in char:
            textStr = textStr.replace(letters, '')

    stop = open('stop.txt', 'r', encoding = 'utf-8')
    stopWords = stop.read().lower().split('\n')
##    print(stopWords)
##    print('\n')

    textStr = textStr.split()
    wordFreq = {}
    for words in textStr:
        if words not in stopWords: 
            wordFreq[words] = wordFreq.get(words, 0) + 1

    wordList = list(wordFreq.items())
    wordList.sort()
    wordList.sort(key = keyVal, reverse = True)
##    print(wordList)
    text.close()
    
    return wordList, len(textStr) 
    
def cloud(win, word, size, bufferList):
    pt = Point(randrange(100, 500), randrange(200, 400))
    accu= 0
    while touches(bufferList, pt, len(word), size):
        pt = Point(randrange(100, 500), randrange(200,400))
        accu +=1
        if accu > 2000: 
            print(accu)
            break
    print('accu', accu)
    text = Text(pt, word)
    text.setSize(size)
##    text.setTextColor(color_rgb(randrange(0,255), randrange(0,255), randrange(0,255)))
    text.draw(win)
    bufferMaker(win, bufferList, pt, size, len(word)) 

def sizeVal(frequency, maxFreq):
    MAX = 40
    size = round(frequency/maxFreq * MAX)
    return size

def bufferMaker(win, bufferList, cenPt, size, length):
    width = round(size*length*.35)
    height = round(size*.60)
    x = cenPt.getX()
    y = cenPt.getY()
    bufferRect = Rectangle(Point(x-width, y-height), Point(x+width, y+height))
##    bufferRect.draw(win)
    bufferList.append(bufferRect)
  
    
    
def touches(bufferList, pt, length, size):
    for rects in bufferList:
        if isClicked(rects, pt, length, size):
            return True
    return False

def isClicked(buffer, point, length, size):
    p1 = buffer.getP1()
    p2 = buffer.getP2()
    
    x = point.getX()
    y = point.getY()

    width = round(size*length*.35)
    height = round(size*.60)
    x1 = int(x - width)
    x2 = int(x + width)
    y1 = int(y - height)
    y2 = int(y + height)

##    if x1 > p1.getX() and x1 < p2.getX() and y1 > p1.getY() and y1 < p2.getY():
##        return True
##    elif y2 > p1.getY() and y2 < p2.getY() and x2 > p1.getX() and x2 < p2.getX():
##        return True
##    elif x1 > p1.getX() and x1 < p2.getX() and y2 > p1.getY() and y2 < p2.getY():
##        return True
##    elif x2 > p1.getX() and x2 < p2.getX() and y1 > p1.getY() and y1 < p2.getY():
##        return True
##    elif x1 > p1.getX() and x2 > p1.getX() and x1 < p2.getX() and x2 < p2.getX():
##        return True
##    elif y1 > p1.getY() and y2 > p1.getY() and y1 < p2.getY() and y2 < p2.getY():
##        return True
##    elif x1 < p1.getX() and x2 > p1.getX() and x1 < p2.getX() and x2 > p2.getX():
##        return True
##    elif y1 < p1.getY() and y2 > p1.getY() and y1 < p2.getY() and y2 > p2.getY():
##        return True
    for X in range(x1, x2):
        for Y in range(y1, y2):
            if X >= p1.getX() and X <= p2.getX() and Y >= p1.getY() and Y <= p2.getY():
                return True 
    return False
def isClickedLight(buffer, point):
    p1 = buffer.getP1()
    p2 = buffer.getP2()
    
    x = point.getX()
    y = point.getY()

    if x > p1.getX() and x < p2.getX() and y > p1.getY() and y < p2.getY():
        return True
    return False
def intro(win, text, box, size, move = True):
    center = box.getCenter()
    msg = Text(Point(center.getX(), center.getY()), text)
    msg.setSize(size)
    box.draw(win)
    msg.draw(win)

    if move == True:
        for i in range(30):
            box.move(0,-20)
            msg.move(0,-20)
            sleep(0.00002)
    message = Text(Point(300, 550), 'Click to continue')
    message.draw(win)
    win.getMouse()
    message.undraw()
    box.undraw()
    msg.undraw()

def isClickedB(button, point):

    #we are going to implement this
    #your code here
    p1 = button.getP1()
    p2 = button.getP2()
    x = point.getX()
    y = point.getY()

    if x > p1.getX() and x < p2.getX() and y > p1.getY() and y < p2.getY():
        return True
    return False 

def drawButton(win, pt1, pt2, label):
    button = Rectangle(pt1, pt2)
    button.setFill("blue3")
    button.draw(win)

    #find the x and y coords of the middle of the button
    centerX = (pt1.getX() + pt2.getX())/2.0 
    centerY = (pt1.getY() + pt2.getY())/2.0

    #use these coords for the position of the label
    btnLabel = Text(Point(centerX,centerY), label)
    btnLabel.setFill("white")
    btnLabel.draw(win)

    return button   
    
    
     
    
    
main()
 
