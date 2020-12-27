# \n : change line
print("Hello World.\nWelcome!")

# Two quotation marks
print('Hello, nmae is "Jay", how are you?')
print("Hello, nmae is \"Jay\", how are you?")

# \\ 
print("C:\\Users\\Desktop")

# \r : move the cursor to the front
print("Red Apple\rPine")

# \b : Backspace
print("Redd\bApple")

# \t : Tab
print("Red\tApple")

# Quiz: Password Generator using the website
# Ex: http://naver.com
# Rule 1: Don't put http://
# Rule 2: Remove after .
# Rule 3: First 3 letter of remaining words + number of words + number of 'E' + "!"

website = "http://daum.net"
website = website.replace("http://", "")
website = website[:website.index(".")]
password = website[:3] + str(len(website)) + str(website.count('e')) + "!"
print(password)