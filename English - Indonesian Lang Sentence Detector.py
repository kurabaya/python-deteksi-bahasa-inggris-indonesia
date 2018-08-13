" English or Bahasa Indonesia Sentence Detector Program - Faizal SF "

#Refering and splitting source database
sourceEnglish = open('english.txt', 'r').read()
sourceIndonesia = open('indonesia.txt', 'r').read()
splitDbseEnglish = sourceEnglish.split('\n')
replaceDbseIndonesia = sourceIndonesia.replace(" ","").replace("(k)", "").replace("(n)", "").replace("(v)", "").replace("(i)", "").replace("(num)", "").replace("\n", " ").replace("(pron)", "").replace("(l)", "")
splitDbseIndonesia = replaceDbseIndonesia.split(" ")

#Function to filter the input
def filterSentence(Input) :
    global resultIndonesia
    global resultEnglish
    splitSentence = Input.lower().split(' ')
    index = 0
    resultIndonesia = 0
    resultEnglish = 0
    while index < len(splitSentence) :
        if splitSentence[index] in splitDbseIndonesia and splitSentence[index] in splitDbseEnglish :
            resultIndonesia = resultIndonesia + 1
            resultEnglish = resultEnglish + 1
        elif splitSentence[index] in splitDbseIndonesia or splitSentence[index] in splitDbseEnglish :
            if splitSentence[index] in splitDbseIndonesia :
                resultIndonesia = resultIndonesia + 1
            elif splitSentence[index] in splitDbseEnglish :
                resultEnglish = resultEnglish + 1        
        index = index + 1
    return resultIndonesia
    return resultEnglish
        
#Input the sentences
global repeat
repeat = 0
while repeat == 0 :
    nama = input("Enter the sentence : \n")
    sentence = nama.lower()
    filterSentence(nama)

    #Process and analyze the filtered input
    if resultIndonesia/((resultIndonesia+resultEnglish)+0.000001) > 0.8 and resultEnglish/((resultIndonesia+resultEnglish)+0.000001) < 0.2:
        print('Written in Bahasa Indonesia')
    elif resultEnglish/((resultIndonesia+resultEnglish)+0.000001) > 0.8 and resultIndonesia/((resultIndonesia+resultEnglish)+0.000001) < 0.2:
        print('Written in English')
    elif resultIndonesia/((resultIndonesia+resultEnglish)+0.000001) > 0.5 and resultEnglish/((resultIndonesia+resultEnglish)+0.000001) < 0.5 :
        print('Probably written in Bahasa Indonesia')
    elif resultEnglish/((resultIndonesia+resultEnglish)+0.000001) > 0.5 and resultIndonesia/((resultIndonesia+resultEnglish)+0.000001) < 0.5 :
        print('Probably written in English')
    elif resultEnglish != 0 and resultIndonesia !=0 and resultEnglish == resultIndonesia :
        print('Written in Bahasa Indonesia and English')
    elif resultEnglish == 0 and resultIndonesia == 0:
        print('Not written in Bahasa Indonesia nor English')

    #This should be deleted - used only for analyzing the bugs
    #print(resultEnglish)
    #print(resultIndonesia)

    #Prompt asking to repeat the program
    prompt = input('Do you want to enter another sentence? (Y/N) ')
    print('\n')
    if prompt.lower() == 'y' :
        repeat = 0
    elif prompt.lower() == 'n' :
        repeat = 1
    else :
        print('You entered a wrong character. Program will be stopped.')
        repeat = 1
