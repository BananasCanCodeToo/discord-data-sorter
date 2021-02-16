import os

fileCount = 0

for directory, subdirectories, files in os.walk('INPUT'):
    for file in files:
        path = os.path.join(directory, file)
        print(path)
        fileCount += 1

print(f'\n\n\n Listed all Files in all directories ({fileCount} Files)')

while True:
    continue
