#This program tells the temperature
fahrenheit=float(input('enter temperature in fahrenheit:'))
celcius=((fahrenheit-32)*5)/9
print('temperature is:',celcius,'celcius')
if celcius<0:
                 print('It is freezing')
elif celcius<10:
                 print('It is very cold')
elif celcius<23:
                 print('It is mild pleasant')
elif celcius<30:
                 print('It is moderate hot')
else:
                 print('It is very hot')
