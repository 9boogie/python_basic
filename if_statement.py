# weather = input("How is the weather? ")
# if weather == "Rain" or weather == "Snow":
#   print("Take umbrella")
# elif weather == "Dust":
#   print("Wear the mask")
# else:
#   print("Enjoy the weather")

temp = int(input("What is the temperature? "))
if 30 <= temp:
  print("It's too hot. Don't go outside")
elif 10 <= temp and temp < 30:
  print("It is nice weather")
elif 0 <= temp and temp < 10:
  print("Take the jacket")
else:
  print("It is too cold, don't go outside")