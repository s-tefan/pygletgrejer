import datetime

sofie=datetime.date(1989,9,17)
stefan=datetime.date(1968,6,4)
d=sofie-stefan
fy=datetime.timedelta(days=5*365+1)
x=2*(d+fy)
dagen=stefan+x
print(stefan,sofie,d,dagen)



