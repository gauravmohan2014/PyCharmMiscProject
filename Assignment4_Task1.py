try:
    read_file = open('sample.txt', 'r')
    print(read_file.read())
    read_file.close()
except:
    print("The File 'sample.txt' was not found.")



