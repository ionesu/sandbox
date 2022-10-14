## Overview
In this exercise you are requested to program a component for encrypting and decrypting text in English. The component are two functions Encrypt and Decrypt. The functions scaffolding is given as part of the starter solution. Do not change the parameters or API.
## The Cipher
The encryption method takes a message to encrypt or decrypt and an encryption key, which works as described below.
1. The encryption key is 26 charcters long, all capital letters, with each capital letter appearing only once. E.g. "**JIECHSDUGFRVAWNQTYBZOLKMPX**".
2. The index of each letter in the array corresponds to the letter it should substitute, starting with "**A**". E.g. for the key above, the following encryptions will occur:
   1. **A** => **J** (since index 0 in the key is "J")
	 2. **ABC** => **JIE** (since indice 0+1+2 in the key is "JIE")
	 3. **XYZ** => **MPX**
3. Decryption works exactly the opposite. E.g. the encryption key above:
   1. The index of "**J**" is 0 so it decrypts to "**A**"
	 2. The index of "**I**" is 1 so it decrypts to "**B**"
	 3. The index of "**X**" is 25 so it decrypts to "**Z**"
	 4. **JIE** => **ABC**
4. The encryption and decription process should be **case sensitive**, i.e. the case of the letters in the message should be perserved.
   1. **AbCd** => **JiEc**
	 2. **XyZ** => **MpX**
5. Spaces in the message to encrypt/decrypt should be perserved as-is.

## Guidelines
When implementing the exercise, start with the `Encrypt` method and only if complete then continue with the `Decrypt` method. 
In addition, input is not guaranteed to be valid, however, it is advised to handle input validation only if enough time remains.