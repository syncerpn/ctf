# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:47:35 2023

@author: Nghia
"""

bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
            
def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index - rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)
    
decode_secret(bezos_cc_secret)