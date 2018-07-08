'''
word cloud. This program reads a text file, finds the frequency of each of the
words excluding the articles and other unnecessary words like pronouns. It then
creates a word cloud of the words by diplaying the words graphically in a set
window according to the frequency of the words.
'''
from random import*
from graphics import*
def keyVal(tupList):
    return tupList[1]
def fileWords(file):
##    file = input('Give me a file you want to try? ') 
    text = open(file, 'r', encoding = 'utf-8')
    textStr = text.read().lower()
    char = '!@#$%^&*()~`{}-[];:<>,./?"'
    for letters in textStr:
        if letters in char:
            textStr = textStr.replace(letters, '')

    stop = open('stop.txt', 'r', encoding = 'utf-8')
    stopWords = stop.read().lower().split('\n')
    print(stopWords)
##    stopWords.append('\n')
  

##    print(stopWords)
##    textStr = textStr.split()
##    print(textStr[0:10])
##    for words in textStr:
##        if words in stopWords:
##            textStr.remove(words)
    textStr = textStr.split()
    print(textStr[0:200]) 
    for words in textStr:
        for word in stopWords:
            if word == words: 
                textStr.remove(words)
##    print(textStr[0:200]) 
      #creating the dictionary
    
    wordFreq = {}
    for words in textStr:
        wordFreq[words] = wordFreq.get(words, 0) + 1

    wordList = list(wordFreq.items())
    wordList.sort()
    wordList.sort(key = keyVal, reverse = True)
    
    text.close()
    
    return wordList, len(textStr) 
    

def main():

    win = GraphWin('wordCloud', 600, 600)
    filename = Text(Point(20, 50), 'filename')
    filename.draw(win)
    fileEnt = Entry(Point(300, 50), 20)
    fileEnt.setText('stairway.txt') 
    fileEnt.draw(win)
    sortedWords, total = fileWords(fileEnt.getText())

    for vals in sortedWords[1:20]:
        cloud(win, vals[0], vals[1]/total)
        print(vals[0], vals[1]/len(sortedWords)*1000)
    
def cloud(win, word, frequency):
    text = Text(Point(randrange(100,500), randrange(200,400)), word)
    text.setSize(round(frequency*1000))
    text.draw(win)
    return 
    
main()
    
