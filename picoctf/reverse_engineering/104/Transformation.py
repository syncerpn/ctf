# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 12:57:48 2023

@author: Nghia
"""


# flag = ?
# enc = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽"
flag = ''.join([chr(ord(enc[i]) // 256) + chr(ord(enc[i]) % 256) for i in range(len(enc))])
print(flag)