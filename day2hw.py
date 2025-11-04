paragraph = """Python is a popular programming language that is easy to learn and powerful to use. 
This Python course helps beginners understand programming concepts and develop real-world projects."""

length = len(paragraph)
print("Length of paragraph:", length)

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

preview = paragraph[:50]
print("Preview:", preview)

paragraph_replaced = paragraph.replace("Python", "PYTHON")
print("After replacement:", paragraph_replaced)

paragraph_lower = paragraph_replaced.lower()
print("Lowercase paragraph:", paragraph_lower)

paragraph_stripped = paragraph_lower.strip()
print("Stripped paragraph:", paragraph_stripped)

words = paragraph_stripped.split()
print("List of words:", words)

if "course" in words:
    print("The word 'course' is found in the paragraph.")
else:
    print("The word 'course' is not found in the paragraph.")

print("The course description is {} characters long and has {} words.".format(length, len(words)))
