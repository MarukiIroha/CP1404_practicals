"""
Word Occurrences
Estimate: 60 minutes
Actual:   40.5 minutes
"""
total_words = {}
max1 = 0
text = input("Text: ").split()
for word in text:
        total_words[word] = total_words.get(word, 0) + 1
for i in total_words:
    if len(i) > max1:
        max1 = len(i)
for key in sorted(total_words):
    thing, width, other_thing = key, max1, total_words[key]
    print(f"{thing:{width}} : {other_thing}")
