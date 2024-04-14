print('Hello World')
print("What is your name?")
myName = input()
print("Nice to meet you" , myName)
print("The length of your name is", len(myName))
print("What is your age?")

myAge = input()
if not myAge.isdigit():
    print("Please use number")
else:
    myAge = int(myAge)
    if myAge < 20:
        print("You are younger than me...")
    else:
        print("You are older than me...")

    # explicitly converts the age into string while printing
    print("You will be" + str(myAge+1) + "year old in a year")  

    #  Python automatically handles the conversion to string and space separation between elements when using the comma , in print().
    print("You will be" , myAge+1 , "year old in a year")

bacon = 20
bacon + 1
print(bacon)

a= 'spam' + 'spamspam'
b = 'spam' * 3
print(a,'\n', b)


# SOLVED QUESTION ANSWERS
'''
1. Which of the following are operators, and which are values?
Ans:
*(operator)
'hello'(value)
-88.8(value)
-(operator)
/(operator)
+(operator)
5(value)

2. Which of the following is a variable, and which is a string?
Ans:
spam(variable)
'spam'(string)

3. Name three data types.
Ans:
- String
- Integer
- Boolean

4. What is an expression made up of? What do all expressions do?
Ans:
An expression is made up of variable, operator and method calls that produce a value. Expressions can calculate value, manipulate data, call functions and so on..

5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
Ans:
Expression is a piece of code and statement is a whole instruction that python can execute.

6. What does the variable bacon contain after the following code runs?
bacon = 20
bacon + 1
Ans:
It will still contain 20 because it does not assign its value back to the variable..

7. What should the following two expressions evaluate to?
'spam' + 'spamspam'
'spam' * 3
Ans:
First will concatenate spam and spamspam resulting in spamspamspam
Second will multiply the spam by 3 resulting in spamspamspam

8. Why is eggs a valid variable name while 100 is invalid?
Ans:
A variable cannot start with numbers.. or python will not understand it..

9. What three functions can be used to get the integer, floating-point number, or string version of a value?
Ans:
int()
float()
str()

10. Why does this expression cause an error? How can you fix it?

'I have eaten ' + 99 + ' burritos.'
Ans:
Python assumes all the expressions are string while printing..we can convert it in two ways
'I have eaten ' + str(99) + 'burritos.'
'I have eaten', 99, 'burritos.'
'''