if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


    # sorted_list = sorted(arr)
    # listed = list(set(sorted_list))
    # if len(listed) != 0 and len(listed) != 1:
    #     print(listed[-2])

    unique_arr = list(set(arr)) 
    sorted_arr = sorted(unique_arr, reverse=True) 
    second_highest = sorted_arr[1] 

    print(second_highest)