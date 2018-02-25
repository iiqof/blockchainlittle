###############################################################################
# Author: IIQ0F
#
# Description:
#   This code contains the Block and BlockChain classes, functions to
#   manipulate them, in a trivial way. 
#
#
# This code is given as it is. License: public knowledge
###############################################################################

import ast

class Block:

    """ Memory structure for the Block. With the ability to write to ascii and load form ascii the structure.  """

    def __init__(self, bindex, bdata, prebhash, nonce=0):
        self.bindex = int(bindex)        # Block index
        self.bdata = str(bdata)          # Message that goes to the block
        self.prebhash = int(prebhash)    # Hash of the previous block
        self.nonce = int(nonce)          # Nonce of this block


    def ascii_form(self):
        """ Defines the standard form, how it is stored in the distributed chain, and how it is hashed"""
    
        return "{\n \'inx\' : %d,\n  \'msg\' : \'%s\',\n  \'phs\' : %d,\n  \'nnc\' : %d\n}" % (self.bindex, self.bdata, self.prebhash, self.nonce)


def load(block_ascii):
        """Transforms a valid ascii string into a memory structure block"""
        block = ast.literal_eval(block_ascii)
        return Block(block['inx'], block['msg'], block['phs'], block['nnc'])


def createGenb():
    """ Defines the first block of the chain. """
    return Block(0, "Genesis Block", 0)




class BlockChain:
    
    def __init__(self):
        self.clenght = 0
        self.chain = []

        
    def add_block(self, block):
        """ Adds a block to the memory structure of the chain """
        self.chain.append(block)
        self.clenght += 1
        return 0

    def ascii_form(self):
        """ Creates the ascii form for the block chain, from the asci forms of the blocks"""

        ascii = ''
        for block in self.chain:
            ascii += block.ascii_form() + '\n'
        return ascii


############ Test operations##############

B = Block(0, "Hello World", 0)

G = createGenb()

print(B.ascii_form())

print(G.ascii_form())

BB = load(B.ascii_form())

BBC = load("{ \
 'inx' : 0, \
  'msg' : 'Loaded Baby', \
  'phs' : 0, \
  'nnc' : 0 \
}")

print(BB.ascii_form() == B.ascii_form())

print('\n' + '\n' + 'Round 2 ........ BlockChain')
C = BlockChain()

C.add_block(G)

C.add_block(B)

C.add_block(BB)

C.add_block(BBC)


print(C.ascii_form())


