string = str(input("Enter the whole string: ")).lower()

freq = {}
for i in string:
    freq[i] = freq.get(i, 0) + 1

for i in string:
    if freq[i] == 1:
        print("First non-repeating character is:", i)
        break
else:
    print("None")
