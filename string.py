sentence = 'I am a boy'

print(sentence)

paragraph = '''
Python is easy. 
JavaScript is good.
C++ is Nice.
'''

print(paragraph)

#Slicing
jumin = "991225-1234567"

print("Gender: " + jumin[7])
print("Year: " + jumin[0:2])
print("Month " + jumin[2:4])

print("Birthday: " + jumin[:6]) # Start to 6th index
print("Last 7 digits: " + jumin[7:]) # 7th index to end
print("Last 7 digits (from the back): " + jumin[-7:])