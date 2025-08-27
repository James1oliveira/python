from pathlib import Path  # Import Path class to work with filesystem paths

# Create a string variable with multiple lines of text
contents = "Jackie Chan was here\n"
contents += "He loves to kick enemies\n"
contents += "He is the original stuntman actor\n"

# Define the file path where the contents will be saved
path = Path('programming.txt')

# Write the contents string to the specified file (overwrites if file exists)
path.write_text(contents)
