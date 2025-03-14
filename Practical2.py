#Array and length of array
#start counting from 0
firstArray = [12, 'gemini', "Happy", 12.72, True]
firstArrayLength = len(firstArray)
print(firstArrayLength)

#append adds the element at the end of the array
firstArray.append("Jigme")
secondArrayLength = len(firstArray)
print(secondArrayLength)

print(firstArrayLength - secondArrayLength)

#Range and to print it in sequence
programsAtCST=["EE", "CS", "IT", "ECE", "ME", "CE", "AE", "PE", "MSE", "MME", "EP", "CST"]
arrayLength= len(programsAtCST)

for index in range(arrayLength):
    print(programsAtCST[index].lower()) #lowercase

#lower function is working but it does not change the initial array. 
#It only changes the copy of the array.
#2ways to do for loop
for element in programsAtCST:
    print(element)

#While Loop
programsAtCST=["EE", "CS", "IT", "ECE", "ME", "CE", "AE", "PE", "MSE", "MME", "EP", "CST"]
arrayLength= len(programsAtCST)
index = 0
while index <= arrayLength:
    print(programsAtCST[index])
    index = index + 1
#will stop when it reaches 9(x<10)
#if in the loop there is no race condition and cause infinite loop

