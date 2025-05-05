writing_file = input('Enter text to write to the file: ')
with open('output.txt', 'w') as file:
    file.write(writing_file + '\n')
print('Data successfully written to output.txt.')

appending_file = input('Enter additional text to append: ')
with open('output.txt', 'a') as file:
    file.write(appending_file + '\n')
print('Data successfully appended.')

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    Final_content = file.read()
    print(Final_content)
