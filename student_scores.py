n = int( input('How many students ? :'))

grade = []

for i in range(n) :
   score = float(input('Please enter student grade :'))
   grade.append(score)

grades = sum (grade)

average = grades / n
print (average )     

maximum = max (grade)
print ( maximum )      

minimum = min (grade)
print (minimum )     
