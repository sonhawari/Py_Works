Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> test = [1,2,3,4,5]
>>> test
[1, 2, 3, 4, 5]
>>> test[0]
1
>>> test = (1,2,3,4,5)
>>> test
(1, 2, 3, 4, 5)
>>> test[0]
1
>>> test[-1]
5
>>> test[-2]
4
>>> test[1:3]
(2, 3)
>>> test[:]
(1, 2, 3, 4, 5)
>>> test[2:]
(3, 4, 5)
>>> range(1,10)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>  x = 100
divisors = ()
for i in range(1,x):
	if x%i == 0:
		divisors = divisors + (i,)
		
  File "<pyshell#12>", line 2
    x = 100
    ^
IndentationError: unexpected indent
>>> x = 100
divisors = ()
for i in range(1,x):
	if x%i == 0:
		divisors = divisors + (i,)
		
>>> divisors

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    divisors
NameError: name 'divisors' is not defined
>>> s1 = 'abcdefg'
>>> s1
'abcdefg'
>>> s2 = 'hijklmn'
>>> s2
'hijklmn'
>>> s1 + s2
'abcdefghijklmn'
>>> s1[0]
'a'
>>> s1
'abcdefg'
>>> 


>>> 

>>> 


>>> 

>>> 
>>> s1[2:4]
'cd'
>>> 
