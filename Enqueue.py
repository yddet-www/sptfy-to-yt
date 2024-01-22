import os

# Appened input onto queue text file
def append_to_file(line):
    file = open("queue.txt", "a", encoding="utf-8")
    file.write(line + "\n")
    file.close()
    
# Return a list of all lines in the queue text file
def read_lines():
    file = open("queue.txt", "r", encoding="utf-8")
    return file.readlines()