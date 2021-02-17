
def removeDuplicate(nums):
    s = set(nums)
    print(s)
    return list(s)

def main():
    print(removeDuplicate([1, 1, 5, 2, 2, 2, 5, 7, 7, 8])) # [1, 2, 5, 7, 8]을 리턴해야 합니다

if __name__ == "__main__":
    main()