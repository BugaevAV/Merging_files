import os


BASE_PATH = os.getcwd()
catalog = os.path.join(BASE_PATH, 'txts')
file_names = dict.fromkeys(os.listdir(catalog))
for file in file_names:
    full_path = os.path.join(catalog, file)
    with open(full_path, encoding='utf-8') as file_object:
        content = file_object.read()
        str_number = len(content.split('\n'))
        file_names[file] = (str_number, content)
file_names = sorted(file_names.items(), key=lambda x: x[1])
new_file_names = dict(file_names)
# print(file_names)

new_file = open('result.txt', 'w', encoding='utf-8')
for file_name, elements in new_file_names.items():
    with open(new_file.name, 'a') as new_file_object:
        new_file_object.write(f'{file_name}\n')
        str_number, content = elements
        new_file_object.write(f'{str_number}\n{content}\n')