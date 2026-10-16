s1=int(input("Первая сторона:"))
s2=int(input("Второая сторона:"))
s3=int(input("Третья сторона:"))

if s1==s2==s3:
   print('Равносторонний')
elif s1==s2 or s2==s3 or s3==s1:
   print('Равнобедренный')
else:
   print('Разносторонний')

