def sort_me(my_list):
    for _ in range(len(my_list)):
        for y in range(len(my_list) - 1):
            temp = list[y]
    
            if list[y] > list[y + 1]: 
                list[y] = list[y + 1]
                list[y + 1] = temp

    return my_list

print(sort_me([3, 4, 10, 8]))
                