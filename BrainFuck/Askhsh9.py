#Topotheto tis routines mou stin arxi gia na mporo na tis kaleso aneta se olo mou to programma
#=============================================================================================

#Routina metatropis apo keimeno se BrainFuck
def String2BrainFuck (strRegular):
    strWorking = ""
    strResult = ""
    iCurrent = 0
    iLen = len(strRegular) - 1
    while iCurrent <= iLen:
        ASCII_NUMBER = ord(strRegular[iCurrent])
        for times in range(0,ASCII_NUMBER):
            strWorking = strWorking + "+"
        strWorking = strWorking + "."
        if iCurrent < iLen:
            strWorking = strWorking + ">"
        strResult = strResult + strWorking
        strWorking = ""
        iCurrent = iCurrent + 1
    return strResult

#Eftiaksa se routina ton kodika gia na paro mono sigkekrimenous char apo to string
#mipos kai to xrisimopoiiso ksana kapou
def Get_Valid_Chars(strCode):
    BF_COMMANDS = ['>', '<', '+', '-', '.', ',', '[', ']']
    return ''.join(filter(lambda x: x in BF_COMMANDS, strCode))

#Routina metatropis apo BrainFuck se keimeno
def BrainFuck2String (strBrainFuck):
    strBrainFuck = Get_Valid_Chars(strBrainFuck)

    BRAIN = []
    BRAIN_MAX = 30000
    BRAIN_POINTER = 0
    BRAIN_FILL = []
    LOOP = False
    LOOP_RETURN = 0
    for BRAIN_FILL in range (0,BRAIN_MAX,1):
        BRAIN.append(0)
    
    strWorking = ""
    strResult = ""
    iCurrent = 0
    iLen = len(strBrainFuck) - 1
    while iCurrent <= iLen:
        if strBrainFuck[iCurrent] == ">":
                BRAIN_POINTER = BRAIN_POINTER + 1
        elif strBrainFuck[iCurrent] == "<":
                BRAIN_POINTER = BRAIN_POINTER - 1
        elif strBrainFuck[iCurrent] == "+":
            BRAIN[BRAIN_POINTER] = (BRAIN[BRAIN_POINTER] + 1) % 256
        elif strBrainFuck[iCurrent] == "-":
            BRAIN[BRAIN_POINTER] = (BRAIN[BRAIN_POINTER] - 1) % 256
        elif strBrainFuck[iCurrent] == ".":
            strResult = strResult + chr(BRAIN[BRAIN_POINTER])
        elif strBrainFuck[iCurrent] == ",":
            while True:
                sInput = input("Enter a single character: ")
                if len(sInput) == 1:
                    BRAIN[BRAIN_POINTER] = ord(sInput)
                    break
        elif strBrainFuck[iCurrent] == "[":
            if LOOP == False:
                LOOP_RETURN = iCurrent
                LOOP = True
        elif strBrainFuck[iCurrent] == "]":
            if BRAIN[BRAIN_POINTER] != 0:
                iCurrent = LOOP_RETURN
            elif BRAIN[BRAIN_POINTER] <= 0:
                LOOP = False
        else:
            print ("Error Value at valid chars!")
        iCurrent = iCurrent + 1
    
    return strResult

#Apo edo ksekinaei o kodikas gia to user interface
#=================================================

#Onoma programatos (gia efe :P)
print ("===========================")
print ("=                         =")
print ("=   BrainFuck Converter   =")
print ("=                         =")
print ("===========================")

KeepRunning = True

while KeepRunning:
    #Afinoume ton xristi na epileksei leitourgeia
    #Tiponoume tis epiloges, tha mporousame na ta baloume se mia metabliti
    #alla mias kai exoume kapoio problima mias kai grafoume gia BrainFuck ...
    print ("\nConverter Modes")
    print ("===============")
    print ("[1]. Convert a regular string to BrainFuck code.")
    print ("[2]. Convert a BrainFuck code to regular string.")
    print ("[3]. Exit")

    #Rotame to xristi na epileksei mia epilogi
    iMode = int(input ("Choose a mode: "))

    if iMode == 1:      #Metatropi keimenou se BrainFuck
        #s2b
        UserInput = raw_input("Write your text, that you want to convert to BrainFuck: ")
        sUI = String2BrainFuck(UserInput)
        print (sUI)
    elif iMode == 2:    #Metatropi BrainFuck se keimeno
        #b2s
        UserText = raw_input("Write your text, that you want to convert to BrainFuck: ")
        sUI = BrainFuck2String(UserText)
        print (sUI)
    elif iMode == 3:    #Den antekse allo kai eipe na figei
        #exit
        print ("Thank you for using BrainFuck Converter.")
        print ("Have a nice day.")
        KeepRunning = False
    else:               #Tairiazei me tin BrainFuck mias kai den mporei na epileksei sosta
        print ("Please choose a correct choise!")
