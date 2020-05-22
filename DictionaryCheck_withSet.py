def dictionary_symmetry_check(dict1, dict2):
    if set(dict1.keys()) ==set(dict2.keys()):
        for items in dict1:
            if dict1[items] != dict2[items]:
                return False
        return True
    else:
        return False





# dict1 = {'numbers' :{1: 'one', 2:"two", '3':'three'},'x':'y', 'alpha' : {'a': 'apple', 'b': 'ball','c':'cat'}, 'storm' : 'sonic'}
# dict2 = {'x':'y','numbers' :{1: 'one', 2:"two", '3':'three'}, 'alpha' : {'a': 'apple', 'b': 'ball','c':'cat'}, 'storm' : 'sonic'}
d1 = {'a' : 1, 'b' : {'a' :  1, 'b' :  {'a' :  'a',  'b' : 2}}, 'c' : 3 }
d2 = {'a' : 1, 'b' : {'a' :  1, 'b' :  {'a' :  'b',  'b' : 2}}, 'c' : 3 }

print(dictionary_symmetry_check(d1, d2))