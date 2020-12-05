# amr-encryptor
this is a custom text encryptor and decryptor python file.
### how it works
the encryptor has two layers `text` and `binary` layer
the text layer converts each character into another one with by an equation
the equation uses only one variable which is the index of the character in the sentence
while the `binary` layer changes the order of a number in the binary code, also it works with
an equation that uses an equation with the index of each binary code.

# advantages
changing the order of the binary code in the binary layer makes it nearly impossible
for any algorithm to break the encryption as when he tries to convert the binary into text,
he will get a letter resulted from the encrypted binary with changed order of 0 and 1
so he will get a letter which is not in the encrypted text layer

### example

```python

>>> import amr
>>> encrypted = amr.encrypt("java")
>>> amr.test(encrypted) # this line converts the binary to letters without decrypting the binary
'j1;U'
>>> amr.letter_encrypt("java") # this is the real output of the text encryption
'l1ye'
>>> # notice the effect of the binary layer
>>> # the binary layer caused to show the encrypted text layer `j1;U` while it's real value is `l1ye`
>>> amr.accuracy(amr.encrypt("java")) # this function measures the rate of success of the binary encryption layer
0.75
```
some times the `encrypt` function returns a low encryption level done by the binary encryption layer
which increases the probability of decrypting the encrypted
```python
>>> amr.accuracy(amr.encrypt("hello"))
0.2 
```
as you see only one letter was changed by the binary layer, to solve this i created `safe_encrypt` function
this function returns a high percentage binary layer encryption
```python
>>> encrypted = amr.safe_encrypt("hello", percentage=0.7) # percentage takes the minimum accuracy value
>>> amr.accuracy(encrypted)
1.0
>>> # the whole word was fully encrypted !!!
>>> print amr.decrypt(encrypted)
hello
```
since that this encryptor returns a binary string, it will has x8 times or less of the storage of the normal text
to reduce its size i created `super_encrypt` and `super_decrypt` function
```python
>>> encrypted = amr.super_encrypt("welcome", safe_encryption=True) # turn true or false if you need to use safe_encryption or no
'x\x9c3H24\x00\x01]\x83$CCCd\x06\x84e\x00\xe4\x00\x00\x8d\x9e\x07\x8c'
>>> amr.super_decrypt(encrypted)
'welcome'
```
### disadvantages
only english is supported
