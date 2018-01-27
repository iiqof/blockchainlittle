from hashlib import sha256


# The data has to be the most basic ascii, as the read() function does not take special characters like Ñ or à. Also @ $ % are reserved characters that marck structure on a block.

#TODO:
# Add saveguards for @ $ %    
# Add blockchain analysis (size,...)    
 
class Block:
    
    def __init__(self, bindex, bdata, prebhash):
        self.bindex = bindex
        self.bdata = bdata
        self.prebhash = prebhash
        self.bhash = self.get_hash()
    
    def get_hash(self):
        data = str(self.bindex) + str(self.bdata) + str(self.prebhash)
        sha=sha256()
        sha.update(data)
        return sha.hexdigest()
        
    def display(self):
        displayb(self)
        return 0
    

def createb(bdata, preb):
    return Block(preb.bindex + 1, bdata, preb.bhash)
    

def displayb(b):
    print("Index:              " + str(b.bindex))
    print("Data:               " + str(b.bdata))
    print("Previous Block Hash:" + str(b.prebhash) + "\n")


def createGenb():
    return Block(0, "Genesis Block", "0")


class BlockChain:
    
    def __init__(self):
        self.chain = []
        self.clenght = len(self.chain)
        
    def addb(self, b):
        self.clenght += 1
        self.chain.append(b)
        return 0
    
    def headb(self):
        if self.clenght > 0: 
            return self.chain[-1]
        else:
            print "Error: Not initilaized"
            return -1

    def nextb(self,data):
        newb = createb(data,self.headb())
        self.addb(newb)
        return 0
    
    def initc(self):
        self.clenght = 1
        self.chain.append(createGenb())
    
    def display(self,opt=0):
        if opt == 0:
            for i in self.chain:
                print(str(i.bindex)+" : " + str(i.bdata) + "\n")
            return 0
        elif opt == "FULL":
            for i in self.chain:
                i.display()
            return 0
        else:
            clittle = ""
            for i in self.chain:
                clittle = clittle + "@" + str(i.bindex)+"%"+str(i.bdata)+"$"+str(i.prebhash)
            return clittle

    def save(self, name="blockchain"):
        f = open(str(name) + ".bc","w")
        f.write(str(self.display(" ")))
        f.close()
        return 0

def loadc(name):
    f = open(str(name), 'r')
    cstring = f.read()
    BC = BlockChain()
    for block in cstring.split("@")[1:]:
        split_block1 = block.split('%')
        split_block2 = split_block1[1].split('$')
        BC.chain.append(Block(int(split_block1[0]), str(split_block2[0]), split_block2[1] ))
        BC.clenght = len(BC.chain)
    return BC
    



