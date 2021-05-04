import  datetime

today = datetime.date.today()
future = datetime.date(2022,1,1)
comp = future - today

print(comp.days)

