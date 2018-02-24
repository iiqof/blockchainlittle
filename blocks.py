class Block:
    """ Memory structure for the Block. With the ability to write to ascii and load form ascii the structure.  """
    def __init__(self, bindex, bdata, prebhash, nonce=0):
        self.bindex = bindex  # Block index
        self.bdata = bdata    # Message that goes to the block
        self.prebhash = prebhash # Hash of the previous block
        self.nonce = nonce

    def write_block(self):
    """Prints the actual block, in the form:

{{
    {inx : sel.bindex }
    {msg : self.bdata }
    {phs : self.prebhash }
    {nnc : self.nonce }   
}}


This is the form that is also hashed later
 """
	print('{{\n    {inx : %d }\n    {msg : %s }\n    {phs : %d }\n    {nnc : %d }\n}}'%(self.bindex, self.bdata, self.prebhash, self.nonce))
def createGenb():
    return Block(0, "Genesis Block", "0")


B = Block(0, "Hello World", 0)

B.write_block()
