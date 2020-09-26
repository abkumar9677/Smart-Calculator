import sys
sys.path.append('/Smart_Calculator/')
import Smart_Calculator
from Smart_Calculator.mathy import *

print(responses[0])
print(responses[1])
while True:
    print()
    text=input("Talk to your HELPER:")
    for word in text.split(' '):
        if word.upper() in operation.keys():
            try:
                l=extract_num_from_text(text)
                r=operation[word.upper()](l[0],l[1])
                print(r)

            except:
                print("Something is wrong, please try again")
            
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()