#wieża hanoi 

def makeStic():
    board = "|| A || || B || || C ||"
    return board

def makeCircle(howMuch):
    sticA = []
    for i in range(howMuch):
        sticA.append(i+1)
    return sticA 

def fillSticks(sticA,sticB,sticC):
    wholeBoard = []
    hold = 0
    sticAlist = []
    sticBlist = []
    sticClist = []

    for i in range(len(sticA)):
        if sticA[i]: 
            hold = str(sticA[i])
            sticAprnt = "|| ",hold," ||"        
            sticAlist.append(sticAprnt)
            wholeBoard.append(sticAprnt)

    for i in sticB:
        if sticB[i]: 
            hold = str(sticB[i])
            sticBprnt = "|| ",hold," ||"    
            sticBlist.append(sticBprnt)
            wholeBoard.append(sticBprnt)

    for i in sticC:
        if sticC[i]: 
            hold = str(sticC[i])
            sticCprnt = "|| ",hold," ||\n"
            sticClist.append(sticCprnt)
            wholeBoard.append(sticCprnt)

    return wholeBoard

circles = int(input("Podaj ile krążków ma być na pierwszym patyku\n"))

makeStic()
circs = makeCircle(howMuch=circles)
#print(circs)

for i in fillSticks(sticA=circs,sticB=[],sticC=[]):
    print(i,"\n")

