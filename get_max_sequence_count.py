
def get_max_sequence_count(arr):
    max_seq = 1
    current_seq = 1
    for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]-1:
            current_seq += 1
        else:
            if current_seq > max_seq:
                max_seq = current_seq
            current_seq = 1

    return max_seq


# 1,2,4,6,6,7,8,9,11,14
print(get_max_sequence_count([1, 2, 4, 6, 7, 8, 9, 11, 14]))
