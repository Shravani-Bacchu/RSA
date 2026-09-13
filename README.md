# RSA

This is a Python implementation of the RSA program. It also incorporates the naive factoring attack as well as a graphing function, which plots the time to crack the RSA algorithm against the key sizes.

## Features

- encryption of an message
- decryption of a message
- naive factoring attack

## Encryption & Decryption Function

This function does exactly what it says. It encrypts and decrypts the message that the user inputs. 

## Naive Factoring Attack

The naive factoring attack is the function that aims to crack the RSA program, which in simple terms means that it decrypts an encrypted message only using the public information. Following from this, my program also implements a function that tracks the time taken for this naive factoring attack to occur. This function tracks the time for the naive factoring attack occurs, based on the key size (measured in bits). As well as this, my program also plots a graph that aims to show the logarithmic relationships between key size and time.
