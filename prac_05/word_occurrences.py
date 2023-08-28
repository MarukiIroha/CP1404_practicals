"""
Word Occurrences
Estimate: 60 minutes
Actual:   40.5 minutes
"""
total_words = {}
max_length = 0
text = input("Text: ").split()
for word in text:
        total_words[word] = total_words.get(word, 0) + 1
for i in total_words:
    if len(i) > max_length:
        max_length = len(i)
for key in sorted(total_words):
    print(f"{key:{max_length}} : {total_words[key]}")
