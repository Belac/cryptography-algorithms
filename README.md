# cryptography-algorithms
Here are some algorithmic programs written in python language to encrypt plain text and decipher an encrypted one!

*In those algorithms, only english characters and positive integers are considered while encrypting texts. 
As we only have 26 alphabetic characters, we are in the base 26 where values are like :
A: 0 - B: 1 - C: 2 - ... - Y: 24 - Z: 25*

## Affine code
The encoding formula is c = am + b mod 26. Here the key is the couple (a; b). 
The decoding formula is m = a'(c − b) mod 26 where a' is the inverse mod 26 of a (a x a' = 1 mod 26); this implies that a and 26 must be prime between them.

### Sample tests
*Encoding*

Test 1 : Using the couple (7, 10) as key.
Note : That key is a good one because 7 is prime with 26 (gcd(7, 26) == 1).

````
>>> print(cipher('This is an important information! Keep it secret!', 7, 10))
>>> Nhog og kx oqleznkxn oxtezqknoex! Cmml on gmyzmn!
````

Test 2 : Using the couple (10, 7) as key.
Note : Even if we can cipher the text, that key is still a bad one because 10 is not prime with 26 (gcd(10, 26) == 1). 
So, the text obtained will be undecryptable.

````
>>> print(cipher('This is an important information! Keep it secret!', 10, 7))
>>> Pzjf jf hh jxbrvphhp jhfrvxhpjrh! Dvvb jp fvbvvp!
````

*Decoding*

Test 1 : Using the couple (7, 10) as key.
````
>>> print(decipher('Nhog og kx oqleznkxn oxtezqknoex! Cmml on gmyzmn!', 7, 10))
>>> This is an important information! Keep it secret!
````

Test 2 : Using the couple (10, 7) as key.
````
>>> print(decipher('Pzjf jf hh jxbrvphhp jhfrvxhpjrh! Dvvb jp fvbvvp!', 10, 7))
TypeError: bad operand type for unary -: 'NoneType'
````
*We have a type error because the function inv() does not find any inverse for 10 in base 26,
so returns a NoneType as inv(10) instead of a positive integer that should be used while
decrepting*

