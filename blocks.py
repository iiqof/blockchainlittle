class Block:
    """ Memory structure for the Block. With the ability to write to ascii and load form ascii the structure.  """
    def __init__(self, bindex, bdata, prebhash, nonce=0):
        self.bindex = bindex
        self.bdata = bdata
        self.prebhash = prebhash
        self.nonce = nonce

    def wirite_block(self):
	print("{{\n
               index : " + str(bindex) + "\n
               }}")

def createGenb():
    return Block(0, "Genesis Block", "0")

