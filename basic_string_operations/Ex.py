s = "Hey there! I'm Vlada"
print ("Lenght of s = %d" % len(s))

print ("The first occurence of the letter r = %d" % s.index("r"))

print ("a occurs %d times" % s.count("a"))

print ("The first five characters are '%s'" % s[:5])
print ("The next five characters are '%s'" % s[5:10])
print ("The thirteenth character is '%s'" % s[12])
print ("The characters with odd index are '%s'" % s[1::2])
print ("The last five characters are '%s'" % s[-5:])

print ("String in uppercase: %s" % s.upper())

print ("String in lowercase: %s" % s.lower())

nameLength = (len(s) - 5)
firstPartSentence = s[0:nameLength].lower()
name = s[-5:]

print ("Vlada must be uppercase: %s%s" % (firstPartSentence, name))

if s.startswith("Wh"):
    print ("String starts with 'Hey'. Nice!")
else:
    print ("Fuuu")

if s.endswith("ada"):
    print ("Good!")
else:
    print ("Wrong")

print ("Split the words of the string: %s" % s.split(" "))
