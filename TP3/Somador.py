import re
import sys

def somador(file):
    lines = file.readlines()
    line = "".join(lines)
    status = False
    contador = 0

    patterns = re.findall(r'(off|on|=|\d+)',line,re.IGNORECASE)
    for pattern in patterns:
        if re.match(r'off',pattern,re.IGNORECASE):
            status = False
        elif re.match(r'on',pattern,re.IGNORECASE):
            status = True
        elif re.match(r'\d+',pattern):
            if status == True:
                contador += int(pattern)
        elif re.match(r'=',pattern):
            print(contador)
    

if __name__ == "__main__":
    file = open(sys.argv[1],"r")
    
    somador(file)

    file.close()