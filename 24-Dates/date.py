import datetime
print(str(datetime.datetime.now()))
x = datetime.datetime.now()
print("\n"+str(x.year))
print("\n"+str(x.strftime('%A')))
print("\n"+str(x.strftime('%B')))

#Creating Date Objects
'''
To create a date, we can use the datetime() class (constructor) of the datetime module.
'''
x = datetime.datetime(2020, 5, 17)
print(x)
