# String Operations in Python

s = input("Enter a string: ")

print("Original String:", s)

# 1. Length of string
print("Length:", len(s))

# 2. Uppercase
print("Uppercase:", s.upper())

# 3. String slicing
print("First 3 characters:", s[:3])
print("First 4 characters:", s[1:3])

# 4. Reverse string
print("Reverse:", s[::-1])

# 5. Replace
print("After replacing 'a' with 'A':", s.replace('a', 'A'))

# 6. Count a character
print("Count of 'a':", s.count('a'))

# 7. Find a character
print("Position of 'a':", s.find('a'))


# 8. Check starts with
print("Starts with 'A':", s.startswith('A'))

# 9. Check ends with
print("Ends with 'a':", s.endswith('a'))

# 10. Split string
print("Split:", s.split())

