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
    
        return "{ \'inx\' : %d, \'msg\' : \'%s\', \'phs\' : %d, \'nnc\' : %d}" % (self.bindex, self.bdata, self.prebhash, self.nonce)


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




def load_chain(file):
    with open(file) as f:
        BChain = BlockChain()
        chain = f.readlines()
        for block in chain:
            BChain.add_block(load(block))
    return BChain

