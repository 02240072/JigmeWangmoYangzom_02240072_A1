#stack and ques
#whatever goes in the stack first comes out the last and stack is a list implimentation
#used for arrenging things
#pop removes the end element and only prints the remaining elements
list = ["sonam","tashi","karma","dorji"]
list.pop()
print(list)

#index is a variable that numbers the elements in the list
#append adds the elements in the new list after pop
stack = ["sonam","tashi","karma","dorji"]
new_stack = []
for index in range(len(stack)):
    new_stack.append(stack.pop())
print(new_stack)

#ques makes it easir to show the recent
#the firt element is comes out first
stack = ["sonam","tashi","karma","dorji"]
new_stack = []
for index in range(len(stack)):
    new_stack.append(stack.pop(0))#start from the start due to adding 0 in the bracket
print(new_stack)