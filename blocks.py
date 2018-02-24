class Block:
    """ Memory structure for the Block. With the ability to write to ascii and load form ascii the structure.  """
    def __init__(self, bindex, bdata, prebhash, nonce=0):
        self.bindex = bindex  # Block index
        self.bdata = bdata    # Message that goes to the block
        self.prebhash = prebhash # Hash of the previous block
        self.nonce = nonce


    def ascii_form(self):
        """ Defines the standart form, how it is stored in the distributed chain, and how it is hashed"""
    
        return '{{\n    {inx : %d }\n    {msg : %s }\n    {phs : %d }\n    {nnc : %d }\n}}'%(self.bindex, self.bdata, self.prebhash, self.nonce)

    def write_block(self):
        """Prints the actual block, in the ascii form."""
    
	print(self.ascii_form())


def createGenb():
    """ Defines the first block of the chain. """
    return Block(0, "Genesis Block", 0)



### Test operations

B = Block(0, "Hello World", 0)

G = createGenb()

B.write_block()

G.write_block()
