#####
#
#
# Test operations
#
#
# ###### ##############
from blocks import *
from pow import *

Option = raw_input()
if Option == 'blocks' :
    print('Testing the Block class, creating, initializating and loading, and printing')
    B = Block(0, "Hello World", 0)
    G = creategenb()
    BB = load(B.ascii_form())

    print(B.ascii_form())
    print(G.ascii_form())
    print(BB.ascii_form())
    BBC = load("{\
 'inx' : 0,\
 'msg' : 'Hello World',\
 'phs' : 4,\
 'nnc' : 0,\
 'dft' : 0\
}")

    print(BBC.ascii_form())
    print('Test that the ascii strings of the loaded and the generated are the same')
    print(BB.ascii_form() == B.ascii_form())
    print(BB.ascii_form() == BBC.ascii_form())

    print('\n' + '\n' + 'Round 2 ........ BlockChain')
    print('creting a blocchain, adding blocks and printing')
    C = BlockChain()
    C.add_block(G)
    C.add_block(B)
    C.add_block(BB)
    print(C.ascii_form())
    print('Loading a chain, printing and checking if they have the same ascii format')
    CC = load_chain('text.txt')
    print(CC.ascii_form())
    print(CC.ascii_form() == C.ascii_form())

elif Option == 'pow':
    B = Block(0, "Hello World", 0)

    print('Hashes')
    print('ZERO: Pringitn hash, getting the nonce, printing form and hash')
    print(get_hash(B))
    get_nonce_zero(B, 1)
    print(B.ascii_form())
    print(get_hash(B))

    print('SMALL: Pringitn hash, getting the nonce, printing form and hash')
    get_nonce_small(B, 978380702341287647097130533468955073631689280890312764165644466368986300)
    print(B.ascii_form())
    print(int(get_hash(B), 16))


    print('\n\n Chain validation')
    blockchain = BlockChain()
    genesis = creategenb()
    genesis.memblock['dft'] = 2
    blockchain.add_block(genesis)
    block1 = Block(1, 'First Block in the hood', get_hash(blockchain.chain[0]), 0, 3)
    blockchain.add_block(block1)
    print(blockchain.ascii_form())
    print('The first will fail')
    validate_chain_zero(blockchain, 1)
    get_nonce_zero(block1, 2)
    blockchain.chain[1] = block1
    print('\n'+blockchain.ascii_form())
    validate_chain_zero(blockchain, 1)
    print(get_hash(block1))
    block2 = Block(1, 'Second baby', get_hash(blockchain.chain[1]), 0, 2)
    get_nonce_zero(block2, 3)
    blockchain.add_block(block2)
    block3 = Block(1, 'Trio', get_hash(blockchain.chain[2]), 0, 2)
    get_nonce_zero(block3, 2)
    blockchain.add_block(block3)
    print(blockchain.ascii_form())
    validate_chain_zero(blockchain, 0)

else:
    print('Valid modules are \'blocks\' and \'pow\'')
