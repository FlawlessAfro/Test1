
empty_dict = {}
empty_dict_reversed = {}

info = input("User input: ")

x=0
y=1
revert_input = False
while not revert_input:

    if info == 'revert':
        for i, j in empty_dict.items():
            empty_dict_reversed[j] = i
            print(empty_dict)
            print(empty_dict_reversed)
            revert_input = True
            break
        break
    
    info_liste = info.split(';')

    print(info_liste)

    empty_dict[info_liste[x]] = info_liste[y]

    print(empty_dict)
    
    info = input("User input: ")