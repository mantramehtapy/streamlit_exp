def files_write():
    print("hello")
    with open('test2.txt', 'w') as file2:
        file2.write('Programming is Fun.')
        file2.write('Programiz for beginners')