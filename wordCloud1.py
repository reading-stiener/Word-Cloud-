'''
word cloud. This program reads a text file, finds the frequency of each of the
words excluding the articles and other unnecessary words like pronouns. It then
creates a word cloud of the words by diplaying the words graphically in a set
window according to the frequency of the words.
'''
from random import*
from graphics import*

def main():

    win = GraphWin('wordCloud', 600, 600)
    filename = Text(Point(150, 50), 'filename')
    filename.draw(win)
    
    fileEnt = Entry(Point(300, 50), 20)
    fileEnt.setText('jekyll.txt') 
    fileEnt.draw(win)

    sortedWords, total = fileWords(fileEnt.getText())
    maxFreq = sortedWords[0][1]/total

    bufferList = []
   
    for vals in sortedWords[0:20]:
        cloud(win, vals[0], sizeVal(vals[1]/total, maxFreq), bufferList)
        print(vals[0], sizeVal(vals[1]/total, maxFreq))

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

    while touches(bufferList, pt):
        pt = Point(randrange(100, 500), randrange(200,400))

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
  
    
    
def touches(bufferList, pt):
    for rects in bufferList:
        if isClicked(rects, pt) == True:
            return True
    return False

def isClicked(buffer, point):
    p1 = buffer.getP1()
    p2 = buffer.getP2()
    
    x = point.getX()
    y = point.getY()

    if x > p1.getX() and x < p2.getX() and y > p1.getY() and y < p2.getY():
        return True
    return False 
    
    
main()
 
