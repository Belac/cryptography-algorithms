# cryptography-algorithms
Here are some algorithmic programs written in python language to encrypt plain text and decipher an encrypted one!

*In those algorithms, only english characters are considered while encrypting texts. 
As we only have 26 characters, we are in the base 26 where values are like :
A: 0 - B: 1 - C: 2 - ... - Y: 24 - Z: 25*

## Affine code
The encoding formula is c = am + b mod 26. Here the key is the couple (a; b). 
The decoding formula is m = a'(c − b) mod 26 where a' is the inverse mod 26 of a (a x a' = 1 mod 26); this implies that a and 26 must be prime between them.

### Sample tests
*Encoding*
Test 1 : Using the couple (7, 10) as key.
Note : That key is a good one because 7 is prime with 26 (gcd(7, 26) == 1).
  print(cipher('This is an important information! Keep it secret!', 7, 10))
  Nhog og kx oqleznkxn oxtezqknoex! Cmml on gmyzmn!````
