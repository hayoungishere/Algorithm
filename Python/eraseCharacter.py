
def eraseChar(ori) :
    res = []
    if "#" not in ori:
        return ori
        
    for c in ori:
        #print(res)
        if c == "#":
            if len(res) > 0:
                res.pop()
        else:
            res.append(c)
        
    return ''.join(res)



in1 = input()
in2 = input()

in1 = eraseChar(in1)
in2 = eraseChar(in2)

if in1 != in2:
    print(False)
else:
    print(True)