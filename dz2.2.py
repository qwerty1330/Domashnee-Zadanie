x= int (input))
if 1 <= x <= 3:
print ('I' * x)
elif x == 4:
print ('IV')
elif 5 <= x <= 8:
print ('V' + (x-5) * 'I')
elif x == 9:
print ('IX')
elif 10 <= x <= 13:
print ('X'+ (x-10) * 'I')
elif x == 14:
print ('XIV')
elif 15 <= x <= 18:
print ('XV' + (x-15) * 'I')
elif x == 19:
print ('XIX')
elif 20 <= x <= 23:
print ('XX' + (x-20) * 'I')
elif x == 30:
print ('XXX')
elif x == 40:
print ('XL')
elif x == 50:
print ('L')