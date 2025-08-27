from pathlib import Path

path = Path("learning_python.txt")

# Loop directly over splitlines() and replace "Python" with "C"
for line in path.read_text().splitlines():
    print(line.replace("Python", "C"))
