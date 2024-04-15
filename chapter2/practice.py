'''
1. What are the two values of the Boolean data type? How do you write them?
True and False

2. What are the three Boolean operators?
AND, OR, NOT

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
Sure, here are the truth tables for the three Boolean operators:

1. **AND (&&)**:

| Operand 1 | Operand 2 | Result |
|-----------|-----------|--------|
|   False   |   False   | False  |
|   False   |   True    | False  |
|   True    |   False   | False  |
|   True    |   True    | True   |

2. **OR (||)**:

| Operand 1 | Operand 2 | Result |
|-----------|-----------|--------|
|   False   |   False   | False  |
|   False   |   True    | True   |
|   True    |   False   | True   |
|   True    |   True    | True   |

3. **NOT (!)**:

| Operand | Result |
|---------|--------|
|  False  |  True  |
|  True   |  False |

4. What do the following expressions evaluate to?
(5 > 4) and (3 == 5) #False
not (5 > 4) #False
(5 > 4) or (3 == 5) #True
not ((5 > 4) or (3 == 5)) #False
(True and True) and (True == False) #False
(not False) or (not True) #True


5. What are the six comparison operators?
==
=>
=<
>
<
!=

6. What is the difference between the equal to operator and the assignment operator?
equal to operator ==(It compares) and assignment operator =(it assigns variables)

7. Explain what a condition is and where you would use one.
condition is a statement that evaluates true or false.
looping, decision making ani error handling ma use hunxaa

8. Identify the three blocks in this code:

spam = 0 
if spam == 10: 
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam') 
main block, outer if block, inner if block

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = input()
if spam == str(1):
    print("Hello")
elif spam == str(2):
    print("Howdy")
else:
    print(spam)

10. What keys can you press if your program is stuck in an infinite loop?
ctrl + c

11. What is the difference between break and continue?
break stops the loop and executes next program and continue skips the current iteration and moves on to next iteration

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
its the same b**ch

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(1,11):
    print(i)

j = 0
while j < 10:
    j += 1
    print(j)

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
spam.bacon()
'''




