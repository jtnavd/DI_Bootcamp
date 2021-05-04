import datetime


def user_birthdate():
  birthdate = input(datetime.date)
  return birthdate

def convert():
  my_date = datetime.date.today()
  my_site = datetime.time.min()
  my_datetime = datetime.combine(my_date, my_time)
  print(my_datetime)


convert()


# Create a function that accepts a birthdate as an argument
#  (in the format of your choice), then display a message 
# stating how many minutes the user has been alive.