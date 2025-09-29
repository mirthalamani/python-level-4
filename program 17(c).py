print("Sum of n numbers")
print("---------------")
sn = int(input("Enter the starting number: "))
en = int(input("Enter the ending number: "))
d = int(input("Enter the difference: "))
print("Result")
print("------")
print("Series:")
count = 0
total_sum = 0
for i in range(sn, en + 1, d):
    
  print("+" + str(i))
total_sum += i
count += 1
print("Sum value:", total_sum)
print("Count value:", count)
