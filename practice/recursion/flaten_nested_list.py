lst = [1, 2, [3, 4, [5, 6]], 7, 8]
flat_lst = []


def remove_nesting(l):
    for ele in l:
        if isinstance(ele, list):
            remove_nesting(ele)
        else:
            flat_lst.append(ele)

remove_nesting(lst)
print(flat_lst)
