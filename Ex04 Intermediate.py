def set_by_path(input_dict, path, value):
    path_except_last = path[:-1]
    path_last = path[-1]
    sub_dict = input_dict
    for key in path_except_last:
        sub_dict[key] = {}
        sub_dict = sub_dict[key]
    sub_dict[path_last] = value
    return input_dict

print(set_by_path({'a':1}, ['b'], 2))
print(set_by_path({'a':1}, ['a','b'], 2))
print(set_by_path({'a':1}, ['b','c','d'], 2)) 