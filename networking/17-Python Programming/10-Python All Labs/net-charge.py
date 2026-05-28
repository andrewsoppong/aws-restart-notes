#Exercise 1: Assigning variables, lists, and dictionaries

# Python3.11  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {'y':10.07,'c':
 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25} #Creat a new empty dictionary

#Exercise 2: Using count() to count the numbers of each amino acid

seqCount = ({x: float(insulin.count(x)) for x in 
['y','c','k','h','r','d','e']}) #This count the number of amino acids in insulin which are Y and return a floating number

#Exercise 3: Writing the net charge formula

pH = 0 #Creating a pH variable and initializing it to 0

while (pH <= 14):
    #The Net Charge Formulae
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), netCharge) #Print the netCharge variable with the pH, it uses string formatting for better readability
    pH +=1 #Increase the pH variable
