# making a 3D list
if __name__ == '__main__':
    # 3 inputs
    x = int(input())
    y = int(input())
    z = int(input())
    # dimensions of the cuboid
    n = int(input())

    result_list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if sum([i, j,k]) != n] 
    print(result_list)