import sys

def ducci_diff(art):
    arr = list(art)
    arr.append(art[0])
    return tuple(abs(arr[idex] - arr[idex+1]) for idex,y in enumerate(arr) if idex < len(arr) - 1)

if __name__== "__main__":
    lines = [line.split(',') for line in [line.strip('()\n') for line in open(sys.argv[1])]]
    for x in lines:
        line = tuple(int(y) for y in x)
        print line
        rows = set()
        while ((sum(line) != 0) and (line not in rows)):
            rows.add(line)
            line = ducci_diff(line)
            print line
            
        print str(len(rows)+1) + " steps\n"    
            