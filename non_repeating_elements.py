# 1,2,6,2,5,1,2
# out_put : 6,5


from collections import defaultdict


def get_non_repeating_elements(arr):
    elements_count = defaultdict(int)
    for elem in arr:
        elements_count[elem] += 1

    non_repeating_elements = []
    for key in elements_count.keys():
        if elements_count[key] == 1:
            non_repeating_elements.append(key)

    return non_repeating_elements
