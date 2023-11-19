'''
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)

Write a function called “unfold_dict” that takes a
single dictionary as input. And return an unfolded
version of the dictionary
example:'''



'''
empty_dict = {}

for key, sub_dict in input_dict.items():
    for key_2, value in sub_dict.items():
        composite_key = key + key_2
        empty_dict[composite_key] = value'''



def unfold_dict(input_dict):
    empty_dict = {}
    for key, sub_dict in input_dict.items():
        for key_2, value in sub_dict.items():
            composite_key = key + key_2
            empty_dict[composite_key] = value
    return empty_dict
    
dennis = {
 'a':{'d':1, 'e':2},
 'b':{'f':3},
 'c':{'g':4, 'h':5}
}

losning = unfold_dict(dennis)

print(losning)