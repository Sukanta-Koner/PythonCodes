import ast

def dict_sim_chk(dict1, dict2):
    c = 0
    for k, _ in zip(dict1, dict2):
        c += 1
        if dict1[k] != dict2[k]:
            break
    larger_dict = max([str(dict1), str(dict2)], key=len)
    if len(ast.literal_eval(larger_dict).keys()) > c:
        return False
    return True


d1 = dict(a=1, c=3, b=2)
d2 = {'a' : 1, 'b' : 2, 'c' : 3}
d3 = {'a' : 1, 'b' : d1, 'c' : 3}

print(dict_sim_chk(d1, d2))
