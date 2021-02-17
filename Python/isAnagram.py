def isAnagram(str1, str2):
    h = dict()
    for s in str1:
        if s not in h.keys():
            h[s] = 1
        else:
            h[s] +=1

    for s in str2:
        if s in h.keys() and h[s] > 0:
            h[s] -=1
        else:
            return False
    
    
    return True

def main():
    print(isAnagram('elice','leice'))
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()
