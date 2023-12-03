import time
string = "Python is a high level programming language"
word_count = len(string.split())
border = "-" * 40

def createbox():
    print(border)
    print()
    print("Enter below written phrase as fast as possible and with accuracy")
    print()

while 1:
    t0=time.time()
    createbox()
    print(string,"\n")
    inputText = str(input())
    t1 =time.time()
    lengthofInput = len(inputText.split())
    accuracy = len(set(inputText.split()) & set(string.split()))
    accuracy = (accuracy/word_count)
    timeTaken = (t1-t0)

    wordsperminute=(lengthofInput/timeTaken)*60
    #showing results
    print("\nTotal words \t :",lengthofInput)
    print("Time used \t :",round(timeTaken,2),"secs")
    print("Your accuracy \t :",round(accuracy,3)*100,"%")
    print("Speed is \t :",round(wordsperminute,2),"wpm")
    print("Wanna try again ",end="")
    
    if input():
        continue
    else:
        print("Thanx")
        time.sleep(1.5)
        break