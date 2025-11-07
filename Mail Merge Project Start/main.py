# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names = []

with open("Input/Names/invited_names.txt", mode = "r") as list_of_names:
    for name in list_of_names:
        names.append(name.strip())

for name in names:
    with open(f"Output/ReadyToSend/{name}.docx", "x") as file1, open("Input/Letters/starting_letter.txt", 'r') as file2:
        for line in file2:
            file1.write(line)

for name in names:
    with open(f"Output/ReadyToSend/{name}.docx", "r") as file:
        filedata = file.read()
        filedata = filedata.replace("[name]", name)

    with open(f"Output/ReadyToSend/{name}.docx", "w") as file:
        file.write(filedata)