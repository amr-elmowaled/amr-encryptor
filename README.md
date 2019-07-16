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
>>> encrypted = amr.encrypt("java") # 0b1101010-0b110001-0b0111011-0b1010101
>>> amr.test(encrypted) # this line converts the binary to letters without decrypting the binary
'j1;U'
>>> amr.letter_encrypt("java") # this is the real output of the text encryption
'l1ye'
>>> # notice the effect of the binary layer
>>> # the binary layer caused to show the encrypted text layer `j1;U` while it's real value is `l1ye`
>>> amr.accuracy("java") # this function shows the difference of the encrypted text done by the binary layer and the `binary to text` without decrypting the binary
0.75
```

### disadvantages
english language is only supported
