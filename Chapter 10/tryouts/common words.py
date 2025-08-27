from pathlib import Path

# List of text files to analyze (replace with your downloaded files)
files = ["alice_in_wonderland.txt", "siddhartha.txt", "moby_dick.txt"]

# Loop through each file
for filename in files:
    path = Path(filename)
    try:
        # Read the entire contents of the file
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # Fail silently if the file is missing
        print(f"Sorry, the file {filename} does not exist.")
        continue
    else:
        # Convert text to lowercase for case-insensitive counting
        lower_contents = contents.lower()

        # Count the occurrences of 'the' (includes words like 'then', 'there')
        total_the = lower_contents.count("the")
        
        # Count occurrences of 'the ' (word 'the' followed by a space)
        exact_the = lower_contents.count("the ")

        # Print results
        print(f"File: {filename}")
        print(f"Approximate count of 'the': {total_the}")
        print(f"Count of 'the ' (word 'the' only): {exact_the}")
        print("-" * 40)
