try:
    with open("Sample.txt", "r") as file:
        print("Reading file content:\n")
        reading_file = file.read()
        print(reading_file)
except FileNotFoundError:
    print("Error: The file 'Sample.txt' was not found.")