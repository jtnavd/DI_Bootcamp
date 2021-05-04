my_list = ['John', 'Max', 'Peter']
copy_list = my_list.copy()
for n in my_list:
    age = input(f"Whats the age of {n}? ")
    if int(age) < 16:
        copy_list.remove(n)

print("other people : ", copy_list)
