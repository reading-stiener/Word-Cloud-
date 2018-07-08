#name: Abhijeet Pradhan
#com 110
#assignment 4

'''
word cloud. This program reads a text file, finds the frequency of each of the
words excluding the excess characters and stopwords like pronouns and srticles.
It then creates a word cloud of the words by diplaying the words graphically in
a set window according to the frequency of the words.
In this program I have used a top approach where the main function depends on
helper function which depends on other helper functions.
'''

from random import*
from graphics import*
from time import*

def main():

    #creates a graphics window 
    win = GraphWin('wordCloud', 600, 600)

    #displays the introduction at the start of the program. refer to intro function for more details 
    intro(win, 'Welcome!', Rectangle(Point(200, 200), Point(400, 400)), 25)
    message = 'This program generates a word\n cloud out of an inputted text file.\n An initial text file is already in\n place for you. You can try other\n files of your choice by entering\n another text file name in the\n filename field.'
    intro(win, message, Rectangle(Point(100, 100), Point(500, 500)), 20, move = False)

    #setting up the input entry field 
    filename = Text(Point(150, 50), 'filename')
    filename.draw(win)     
    
    fileEnt = Entry(Point(300, 50), 20)
    fileEnt.setText('stairway.txt') 
    fileEnt.draw(win)

    #setting up the buttons for drawing the word cloud, clearing the word cloud and quitting the program 
    quitIt = drawButton(win, Point(350, 450), Point(450, 500), 'QUIT')
    clear = drawButton(win, Point(150, 450), Point(250, 500), 'ERASE')
    draw = drawButton(win, Point(150, 520), Point(250, 570), 'DRAW')

    #setting up variables for the programs to start 
    pt = win.getMouse()
    textList = []
    
    #the loop runs indefinitely while the quit button is not clicked 
    while isClickedB(quitIt, pt) == False:

        #if draw button clicked, then prints out the wordcloud in the window
        if isClickedB(draw, pt): 
            sortedWords, total = fileWords(fileEnt.getText())
            maxFreq = sortedWords[0][1]/total
            bufferList = []

            #the loop below prints the 30 most common words in the text. it uses the cloud funvtion to do so. refer to cloud
            #function below for more details 
            for vals in sortedWords[0:30]:
                texT = cloud(win, vals[0], sizeVal(vals[1]/total, maxFreq), bufferList)
                print(vals[0], sizeVal(vals[1]/total, maxFreq))
                print(len(bufferList))
                textList.append(texT)

        #if erase button was clicked, erases the wordcloud that has been drawn
        if isClickedB(clear, pt):
            destroyer(textList)
        
        pt = win.getMouse()
    win.close()

#the helper function for sorting the dictionary made using the filewords function below     
def keyVal(tupList):
    return tupList[1]

def fileWords(file):
    #open the text file being used 
    text = open(file, 'r', encoding = 'utf-8')
    textStr = text.read().lower()

    #excess characters to remove 
    char = '!@#$%^&*()~`{}-[];:<>,./?"'

    #the loop for removing the excess characters 
    for letters in textStr:
        if letters in char:
            textStr = textStr.replace(letters, '')

    #opening the stopwords file 
    stop = open('stop.txt', 'r', encoding = 'utf-8')
    stopWords = stop.read().lower().split('\n')

    #making the text string without excess charcters into a list 
    textStr = textStr.split()
    wordFreq = {}

    #adds the words in textStr into the worFreq dictionary if it is not among the stopwords 
    for words in textStr:
        if words not in stopWords: 
            wordFreq[words] = wordFreq.get(words, 0) + 1

    #making the wordFreq dictionary into wordList with tuples of key value pairs as elements and sorting them 
    wordList = list(wordFreq.items())
    wordList.sort()
    wordList.sort(key = keyVal, reverse = True)

    text.close()
    stop.close()
    
    return wordList, len(textStr)

#this function generates the the text object of the required words into the window
#it takes in the parameters word, ita size to create buffer zones and a bufferList
#for keeping track of the bufferzones that that have already been created for the
#words already in the cloud 
def cloud(win, word, size, bufferList):
    
    pt = Point(randrange(100, 500), randrange(200, 400))
    #this function checks if the random point generated for the new word will not touch
    #the buffer zones that have already been made 
    while touches(bufferList, pt, len(word), size):
        pt = Point(randrange(100, 500), randrange(200,400))
    text = Text(pt, word)
    text.setSize(size)
     
    text.setTextColor(color_rgb(randrange(0,255), randrange(0,255), randrange(0,255)))
    text.draw(win)
    #the function below creates a new buffer for the word that has just been printed in the
    #wordCloud 
    bufferMaker(win, bufferList, pt, size, len(word))
    return text
#the helper function below is used to generate sizes for the words according to the
#the word frquencies. It is set up in a way so that the maximum size is always 40
def sizeVal(frequency, maxFreq):
    MAX = 40
    size = round(frequency/maxFreq * MAX)
    return size

#the helper function below is used in the cloud() function to generate an invisible \
#buffer around a new texr object that has just been printed in the wordd cloud 
def bufferMaker(win, bufferList, cenPt, size, length):
    #setting up the variables 
    width = round(size*length*.35)
    height = round(size*.60)
    x = cenPt.getX()
    y = cenPt.getY()
    bufferRect = Rectangle(Point(x-width, y-height), Point(x+width, y+height))
##    bufferRect.draw(win)
    bufferList.append(bufferRect)
  
    
#this helper function is used to check if a point set up for a word will not overlap
    #any of the buffers alresdy in place 
def touches(bufferList, pt, length, size):
    for rects in bufferList:
        #a helper function. see below for details 
        if isClicked(rects, pt, length, size):
            return True
    return False

#this function tests individual buffers in the bufferList with the newtest point
#for validity 
def isClicked(buffer, point, length, size):
    #setting up points from the rectangle and the test point for the word 
    p1 = buffer.getP1()
    p2 = buffer.getP2()

    
    x = point.getX()
    y = point.getY()

    #settin up important variables for the range of the new word 
    width = round(size*length*.35)
    height = round(size*.60)
    x1 = int(x - width)
    x2 = int(x + width)
    y1 = int(y - height)
    y2 = int(y + height)

    #the logic for testing if the buffer is valid. It uses a double for loop approach
    #checking if any of the pixels inside the range of the new word falls inside any
    #buffer. if true, it returns True, else False 
    for X in range(x1, x2):
        for Y in range(y1, y2):
            if X >= p1.getX() and X <= p2.getX() and Y >= p1.getY() and Y <= p2.getY():
                return True 
    return False

#this function helps in creating animated intros 
def intro(win, text, box, size, move = True):
    center = box.getCenter()
    msg = Text(Point(center.getX(), center.getY()), text)
    msg.setSize(size)
    box.setWidth(2)
    box.draw(win)
    
    msg.draw(win)

    if move == True:
        for i in range(100):
            box.move(0,-5)
            msg.move(0,-5)
            sleep(0.002)
    message = Text(Point(300, 550), 'Click to continue')
    message.draw(win)
    win.getMouse()
    message.undraw()
    box.undraw()
    msg.undraw()
#this function checks if the button for drawing or erasing or quitting are clicked
def isClickedB(button, point):

    p1 = button.getP1()
    p2 = button.getP2()
    x = point.getX()
    y = point.getY()
    
    #the logic for the check
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
#this helper function is used for getting rid of the words printes in thw wordCloud
#if the user clicks the erase button
def destroyer(textList):
    for objects in textList:
        objects.undraw()
    
main()
 
