#essa aula é praticamente iteração e compreensão de lista


list = [1, 2 ,3]

new_list = [n + 1 for n in list]
# print(new_list)



name = "Caique"

new_list2 = [letter for letter in name]


doubled_list = [n * 2 for n in range(1,5)]

names = ["Caique", "Matheus", "Duda", "Salles", "Drop"]

condition_list = [name.upper() for name in names if len(name) < 5]
print(condition_list)
