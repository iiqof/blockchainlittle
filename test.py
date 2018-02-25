########### Test operations##############
from blocks import *


B = Block(0, "Hello World", 0)

G = createGenb()

print(B.ascii_form())

print(G.ascii_form())



print('Test that the ascii strings of the loaded and the generated are the same')

BB = load(B.ascii_form())

BBC = load("{ \
 'inx' : 0, \
  'msg' : 'Hello World', \
  'phs' : 0, \
  'nnc' : 0 \
}")

print(BB.ascii_form() == B.ascii_form())
print(BB.ascii_form() == BBC.ascii_form())




print('\n' + '\n' + 'Round 2 ........ BlockChain')
C = BlockChain()

C.add_block(G)

C.add_block(B)

C.add_block(BB)


print(C.ascii_form())

print('Loading a chain')


CC = load_chain('text.txt')
print(CC.ascii_form())

print(CC.ascii_form() == C.ascii_form())
