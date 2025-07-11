user_input1 = input("Enter text to write to the file: ")
write_file1 = open('output.txt','w')
write_file1.write(user_input1)
write_file1.write('\n')
write_file1.close()
print("Data successfully written to output.txt.\n")

user_input2 = input("Enter additional text to append: ")
write_file2 = open('output.txt','a')
write_file2.write(user_input2)
write_file2.close()
print("Data successfully appended.\n")

read_file = open('output.txt', 'r')
print('Final content of output.txt:')
print(read_file.read())
read_file.close()

