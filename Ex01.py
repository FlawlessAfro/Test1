
oppslag = {'name': 'John',
           'age': 30,
           'city': 'New York',
           'salary': 50000
                      
}

age = oppslag['age']
'''
for key in oppslag:
    print(f"key: {key}")

for value in oppslag:
    print(f"Values: {value}")

for key, value in oppslag.items():
    print(f"Key/Value-pairs: {key}: {value}")
'''

my_dict_2 = {'John': 'name',
             30: 'age',
             'New York': 'city',
             50000: 'salary'
             
}

my_dict_3 = {'name': 0,
           'age': 0,
           'city': 0,
           'salary': 0
                      
}

my_dict_4 = oppslag.copy()

my_dict_4.update(my_dict_2)

print(my_dict_4)



