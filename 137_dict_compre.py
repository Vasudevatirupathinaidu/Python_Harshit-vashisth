# dictionary comprehension
# square - {1:1, 2:4, 3:9}

square = {num: num**2 for num in range(1, 4)}
print(square)
print()

# word count
# "vasudev"

text = "vasudev"

word_count = {char:text.count(char) for char in text}
print(word_count)
