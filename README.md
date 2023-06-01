# cryptography-algorithms
Here are some algorithmic programs written in python language to encrypt plain text and decipher an encrypted one!

*In those algorithms, only english characters and positive integers are considered while encrypting texts. 
As we only have 26 alphabetic characters, we are in the base 26 where values are like :
A: 0 - B: 1 - C: 2 - ... - Y: 24 - Z: 25*

## Getting started
To test an algorithm among the following one, you firstly have to execute the following comamand :
> git clone https://github.com/Belac/cryptography-algorithms.git 
         
Then, if you're in python interpreter, to call a particular algorithm, you just need to import it like:
````
>>> from affine_code import *
````

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

## Vigenere code
Here we group the letters by blocks of length k. We then choose a key consisting of k numbers from 0 to 25 (n1, n2, ..., nk). 
To encode a message we perform a translation whose offset depends on the rank of the letter in the block: an offset of n1 for the first letter of the block, 
of n2 for the second letter of the block, ..., of nk for the last letter of the block. 
To decode such a cryptogram, it is enough to make backward shifts.

### Sample tests
*Encoding*

Test : Using the word CRITERIA as key.
Note : Instead of CRITERIA, we can use (2, 17, 8, 19, 4, 17, 8, 0)

````
>>> print(cipher('This is an important information! Keep it secret!', 'CRITERIA'))
>>> Vyql mj in kdxhvkinv zvysiuavzwg! Ovmp kk axgimt!
````


*Decoding*

Test : Using the same word as key (CRITERIA).
````
>>> print(decipher('Vyql mj in kdxhvkinv zvysiuavzwg! Ovmp kk axgimt!', 'CRITERIA'))
>>> This is an important information! Keep it secret!
````

## Atbash cipher
The Atbash cipher is a method of substitution cryptography which consists of replacing each letter by first counting its place in the alphabet, 
and replacing it with the letter occupying the same place, but from the end of the alphabet . 
Thus, by applying it with our alphabet, we replace an A by a Z, a B by a Y, and so.
For this reason, it is also called mirror code. In particular, exactly the same method is applied to encrypt and to decrypt a message

### Sample tests
*Encoding*

Test : Coding "You deserve someone who is terrified of losing you."

````
>>> print(cipher('You deserve someone who is terrified of losing you.'))
>>> Blf wvhviev hlnvlmv dsl rh gviirurvw lu olhrmt blf.
````


*Decoding*

Test : Decoding "Gsvb glow nv R xlfowm'g. Gszg'h dsb R wrw rg."
````
>>> print(decipher("Gsvb glow nv R xlfowm'g. Gszg'h dsb R wrw rg."))
>>> They told me I couldn't. That's why I did it.
````