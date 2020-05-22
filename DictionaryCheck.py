# Comparing 2 Dictionaries


def dictionary_check(dict1, dict2):
    for item1, value1 in dict1.items():
        flag = False
        for item2, value2 in dict2.items():
            if item1 == item2:
                if value1 == value2:
                    flag = True
                else:
                    flag = False
                    break
        if flag == False:
            break
    if (flag == 1):
        for item2, value2 in dict2.items():
            flag = False
            for item1, value1 in dict1.items():
                if item1 == item2:
                    if value2 == value1:
                        flag = True
                    else:
                        flag = False
                        break
            if flag == False:
                break

    if flag == False:
        print("Not same")
    elif flag  == True:
        print("Both are same")



dict1 = {'numbers' :{1: 'one', 2:"two", '3':'three'}, 'alpha' : {'a': 'apple', 'b': 'ball','c':'cat'}, 'storm' : 'sonic'}
dict2 = {'numbers' :{1: 'one', 2:"two", '3':'three'}, 'alpha' : {'a': 'apple', 'b': 'ball','c':'cat'}, 'storm' : 'sonic'}

dictionary_check(dict1, dict2)