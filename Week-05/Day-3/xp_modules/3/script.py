import datetime


def user_birthdate():
  birthdate = input(datetime.date)
  return birthdate

def convert():
  my_date = datetime.date.today()
  my_site = datetime.date.min()
  my_datetime = datetime.combine(my_date, my_time)
  print(my_datetime)


convert()
