alphabets = list("abcdefghijklmnopqrstuvwxyz")
size = 5      
alphabets = alphabets[:size]
indices1 = list(range(size))
indices2 = indices1.copy()
indices2.reverse()
indices1.remove(indices1[-1])
indices = indices1 + indices2

for i in indices:
    start_idx = i+1
    original_list = alphabets[ -start_idx:]
    reverse_list = original_list.copy()
    reverse_list.reverse()
    reverse_list.remove(reverse_list[-1])
    new_list = reverse_list + original_list
    pattern = "-".join(new_list)
    width = size * 4 - 3
    pattern = pattern.center(width, "-")
    print(pattern)