subject = int(input("How many subject is ? :  "))

mark= []

for i in range(subject):
     m = int(input(f" Subject {i+1} mark is: "))
     mark.append(m)

total = sum(mark)
max_mark = subject*100
percentage = (total /max_mark)*100

fail = False
for m in mark:
    if m < 33:
        fail = True
        break

if fail:
    result = "Fail"
else:
    result = "Pass"



#For Grade Comparision
if percentage>90:
    grade = "A+"
elif percentage>80:
    grade = "A"
elif percentage>70:
    grade = "B"
elif percentage>60:
    grade = "C"
elif percentage>50:
    grade = "D"
elif percentage>40:
    grade = "F"


print(f"\n-------Result-------\n")
print(f"Total      :  {total}/{max_mark}")
print(f"Percentage :  {round(percentage,2)}")
print(f"Result     :  {result}")
print(f"Grade      :  {grade}")

     