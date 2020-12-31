absent = [2, 5]
no_book = [7]
for student in range(1, 11):
  if student in absent:
    continue
  elif student in no_book:
    print("End of the lecture, {0}, come to the office".format(student))
    break
  print("{0}, read the book".format(student))