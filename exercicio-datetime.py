import datetime
agora = datetime.datetime.now()
print(agora)
data = datetime.timedelta(days=1, hours=2, minutes=30)
print(data)

agora + data
print(agora.month)
print(agora.day)
# Return the day of the week as an integer, where Monday is 0 and Sunday is 6
print(agora.weekday())
print(agora.strftime('%A'))

mais10 = agora + datetime.timedelta(days=10)
print(mais10.weekday())
print(mais10.strftime('%A'))