import os; os.system("clear"); loopkeeper = 1; 
while loopkeeper == 1:
    begtikomandoseilute = input(">"); os.system(begtikomandoseilute)
    if begtikomandoseilute == "kill":
        loopkeeper = 0
