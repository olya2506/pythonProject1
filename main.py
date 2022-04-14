file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
files = [file_name_1, file_name_2, file_name_3]
list = []

for file_name in files:
    with open(file_name, encoding='utf-8') as file:
        lines = file.readlines()
        list.append([len(lines), file_name, lines])

list = sorted(list)
common = []

for i in list:
    i[0] = str(i[0])
    i[2] = ' '.join(i[2])
    string = ' '.join(i)
    common.append(string)

print(common)

new_file = open('new_file.txt', 'w', encoding='utf-8')
new_file.write(str(common))
new_file.close()