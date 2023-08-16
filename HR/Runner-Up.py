if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr=list(arr)
    arr.sort()
    for i in range(n):
        if arr[i]<max(arr):
            runner=arr[i]
    
    print(runner)   