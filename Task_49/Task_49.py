template1 = list(str(input("Input first template: ")))
template2 = list(str(input("Input second template: ")))

default_dict = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', '?']
my_dict = {
    'a': [0, 1, 2, 3],
    'b': [1, 2, 3, 4],
    'c': [2, 3, 4, 5],
    'd': [3, 4, 5, 6],
    'e': [4, 5, 6, 7],
    'f': [5, 6, 7, 8],
    'g': [6, 7, 8, 9],
    '?': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    '0': [0], '1': [1], '2': [2], '3': [3], '4': [4], '5': [5], '6': [6], '7': [7], '8': [8], '9': [9],
}


def find_error(template1, template2):
    error_sum = 0
    error_sum += find_len_error(template1, template2)
    error_sum += find_dict_error(template1)
    error_sum += find_dict_error(template2)
    if error_sum > 0:
        return 1
    else:
        return 0


def find_dict_error(template):
    for i in template:
        if i not in default_dict:
            return 1
        else:
            return 0


def find_len_error(template1, template2):
    if len(template1) != len(template2) or len(template1) > 9 or len(template2) > 9:
        return 1
    else:
        return 0


def search_summ(template1, template2):
    summ = 0
    finalsumm = 1
    iter = 0
    for i in range(len(template1)):
        summ = len(list(set(my_dict[template1[i]]).intersection(my_dict[template2[i]])))
        if summ != 0:
            finalsumm = finalsumm * summ
        else:
            iter += 1
    if iter == len(template1):
        return 0
    return finalsumm


error_check = find_error(template1, template2)

if error_check == 1:
    print("FATAL ERROR")
    exit()

f = search_summ(template1, template2)
print(f)
