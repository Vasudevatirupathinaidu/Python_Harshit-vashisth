# word counter

text = "At Real Python you’ll learn real-world programming skills from a community of professional Pythonistas from all around the world. Everyone who worked on this book is a practitioner with several years of professional experience in the software industry."

count_letters = {}

i = 0

while i < len(text):
    count_letters[text[i]] = text.count(text[i])
    i += 1

print(count_letters)
