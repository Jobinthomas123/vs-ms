x = 4

while x < 1136:
    # Open the file for reading
    with open(f'{x}.txt', 'r') as file:
        # Read the contents of the file
        contents = file.read()

    # Replace tab spaces with 4.txt space bar spaces
    new_contents = contents.replace('\t', '    ')

    # Open the file for writing
    with open(f'{x}.txt', 'w') as file:
        # Write the modified contents back to the file
        file.write(new_contents)
