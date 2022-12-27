import string

1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
*
'hello'
-87.8
-
/


6

Values- 'hello' , -87.8 , 6
Expression- * , - , / , +

2. What is the difference between string and variable?
A Variable is a store of information, and a String is a type of information you would store in a Variable.Variables are entities which help us store information and retrieve it
later whereas strings are used in Python to record text information, such as names.
for eg- x="mohan"
    here x is variable which stores information "mohan" as a string.



3. Describe three different data types.
Data types are the classification or categorization of data items.
Following are the standard or built-in data type of Python:
Numeric
Sequence Type
Boolean
Set
Dictionary

Numeric- In python numeric data types represent the data which has numeric value.Numeric value can be integer , floating number or even complex numbers. These values are defined as int,float, complex class in python.
 Integer- This value is represented by int class. It contains positive and negative whole numbers(without fraction or decimal ).
 Float- This value is represented by float class.It is a real number with floating point representation. It is specified by a decimal point.
 Complex Number- Complex number is represented by complex class. It is specified as (real part) + (imaginary part)j. For example – 2+3j

Sequence Type- In Python, sequence is the ordered collection of similar or different data types.There are several sequence types in Python –
String
List
Tuple

String- In Python, Strings are arrays of bytes representing Unicode characters. A string is a collection of one or more characters put in a single quote, double-quote or triple quote. In python there is no character data type, a character is a string of length one.
for eg- String with the use of Single Quotes:
'Welcome to the Geeks World'
list- Lists are just like the arrays, declared in other languages which is a ordered collection of data.Lists in Python can be created by just placing the sequence inside the square brackets[].
Tuple- Just like list, tuple is also an ordered collection of Python objects. The only difference between tuple and list is that tuples are immutable i.e. tuples cannot be modified after it is created

Boolean- Data type with one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false). But non-Boolean objects can be evaluated in Boolean context as well and determined to be true or false.

4.What is an expression made up of? What do all expressions do?
An expression is a combination of operators and operands that is interpreted to produce some other value. In any programming language, an expression is evaluated as per the precedence of its operators.
for eg- Expressions
x = 15 + 1.3
It’s a quite simple process to get the result of an expression if there is only one operator in an expression. But if there is more than one operator in an expression, it may give different results on basis of the order of operators executed. To sort out these confusions, the operator precedence is defined. Operator Precedence simply defines the priority of operators that which operator is to be executed first.


5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
In programming language terminology, an “expression” is a combination of values and functions that are combined and interpreted by the compiler to create a new value, as opposed to a “statement” which is just a standalone unit of execution and doesn’t return anything.
An expression is something that can be reduced to a value, for example "10" is an expression, but "spam = 1+3" is not. It's easy to check: print(spam = 10) If it doesn't work, it's a statement,

6.After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
Variable bacon contains 23.

7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3
'spamspamspam'
'spamspamspam'
Both have same values.

8. Why is eggs a valid variable name while 100 is invalid?
Because variable names cannot begin with a number.

9.What three functions can be used to get the integer, floating - point number, or string version of avalue?
The int() , float() , and str( ) functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.

10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
This expression is having error as concatenation operation cant be performed in string and integer data type,so we use format()
method.We can combine strings and numbers by using the format() method.

num=99;
text= "I have eaten {} burritos"
print(text.format(num))