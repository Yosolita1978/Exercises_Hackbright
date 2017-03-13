
def make_dic(string):
    d = {}
    for letter in string:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    return d

def sort_dict(d):
    new = sorted([(-value, key) for key, value in d.items()])
    for t in new:
        value, key = t
        if key == " ":
            pass
        else:
            print key
