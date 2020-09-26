responses=["Welcome to smart Helper","My name is Techie","Thanks","Sorry, this is beyond my ability",
            "I'm fine, what about you?","Any arithmetic operation you want to do?","Write some operational statement"]

def extract_num_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)

def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1

def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def end():
    print(responses[2])
    input("Press any key to exit")
    exit()

def myname():
    print(responses[1])

def sorry():
    print(responses[3])

def how():
    print(responses[4])

def fine():
    print(responses[5])

def yes():
    print(responses[6])

operation={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,
            "MINUS":sub,"SUBTRACT":sub,"SUBTRACTION":sub,"DIFFERENCE":sub,
            "PRODUCT":multiply,"MULTIPLICATION":multiply,"MULTIPLY":multiply,
            "DIVISION":division,"DIVIDE":division,"LCM":lcm,"HCF":hcf}

commands={"NAME":myname,"END":end,"END":end,"HOW":how,"FINE":fine,"GOOD":fine,"YES":yes,"Y":yes}
