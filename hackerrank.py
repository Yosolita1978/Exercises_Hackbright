
def make_set(ranges):
    sizes = set()
    for r in ranges:
        smallest, largest = r
        v_set = range(smallest, largest + 1)
        sizes.update(v_set)

    return sizes

def check_sizes(lst_sizes, smallest, largest):

    return [i for i in lst_sizes if i < smallest or i > largest]





q = 2
i = 5
# lst_sizes = [2 3 6 9 13]
num_vendors = 4
ranges = [[3, 7], [4,8], [14,16], [10,13]] 
set_sizes = make_set(ranges)
print check_sizes(lst_sizes, set_sizes)


