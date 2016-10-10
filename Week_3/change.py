# Uses python3
import sys

def get_change(m):
    change = 0
    for i in [10,5,1]:
    	if m // i > 0:
    		change += m // i
    		m -= i * (m // i) 
    return change

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
