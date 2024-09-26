import sys
import re

def problem1():
    # assuming no more than one instance per line
    # need to find all "SI###(A-Z)"
    # and only print out the stuff after SI
    for line in sys.stdin: 
        res = re.search(r'SI(\d{3}[A-Z]?)', line)
        
        if res:
            print(res[1])

def problem2():
    # assuming no more than one instance per line
    # need to find all "<b>*</b>"
    # and only print out the stuff between the b tags
    for line in sys.stdin:
        res = re.search(r'<b>(.*)</b>', line)
        
        if res:
            print(res[1])
   
def problem3():
    # need to the first "<b>*</b>"
    # and only print out the stuff between the b tags
    for line in sys.stdin:
        res = re.search(r'<b>(.*?)</b>', line)

        if res:
            print(res[1])

def problem4():
    # need to find all "(M|T|W|R|F)+(1|2|3|4|5|6|8|9|10){1,2}"
    # and only print out the stuff between the b tags
    for line in sys.stdin:
        instructor = re.findall(r'([A-Z]+)', line)
        res = re.findall(r'((M|T|W|R|F)+(1|2|3|4|5|6|8|9|10){1,2})', line)
        
        if res and instructor[0] == "VALIGN":
            res = [x[0] for x in res] # just want the string that was matched
            print(instructor[34] + ":\t" + ','.join(res))

    
if __name__ == '__main__':
    # grab the first line
    func = input()
    print(f'Doing {func}')
    if len(re.findall(r'problem[1-4]', func)) == 1:
        eval(func)


