from hashlib import sha256
from itertools import chain, product


# The data has to be the most basic ascii, as the read() function does not take special characters like enye or acento. Also @ $ % are reserved characters that marck structure on a block.

#TODO:
# 2 Add saveguards for @ $ %    
# 3 Add blockchain analysis (size,...)    
 
 
characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NNN = 100  # Maximum lenght of the tried nonces



class Block:
    
    def __init__(self, bindex, bdata, prebhash, nonce=0):
        self.bindex = bindex
        self.bdata = bdata
        self.prebhash = prebhash
        self.nonce = nonce
    
        
    def display(self):
        displayb(self)
        return 0
    

class BlockChain:
    
    def __init__(self, diffty=0):
        self.clenght = 1
        Genb = createGenb()
        get_nonce(Genb, diffty)
        self.chain = [Genb]
        
    def accb(self, b, difty):
        if str(get_hash(b))[:difty] == str(0)*difty:
            self.clenght += 1
            self.chain.append(b)
            print("Valid Block")
            return 0
        else:
            print('Invalid Block')
            return -1

    def displayc(self,opt=0):
        return displayc(self, opt)


           

def save(blockchain, name="blockchain"):
    f = open(str(name) + ".bc","w")
    f.write(str(blockchain.displayc(" ")))
    f.close()
    return 0

    
def headb(blockchain):
    if blockchain.clenght > 0: 
        return blockchain.chain[-1]
    else:
        print "Error: Not initilaized"
        return -1


def displayc(blockchain, opt=0):
    if opt == 0:
        for i in blockchain.chain:
            print(str(i.bindex)+" : " + str(i.bdata) + "\n")
        return 0
    elif opt == "FULL":
        for i in blockchain.chain:
            i.display()
        return 0
    else:
        clittle = ""
        for i in blockchain.chain:
            clittle = clittle + ( 
             "#" + str(i.nonce) 
            + "@" + str(i.bindex) 
            + "%" + str(i.bdata) 
            + "$" + str(i.prebhash) )
        return clittle


def createb(bdata, preb):
    return Block(preb.bindex + 1, bdata, get_hash(preb))
    

def displayb(b):
    print("Nonce:              " + str(b.nonce))
    print("Index:              " + str(b.bindex))
    print("Data:               " + str(b.bdata))
    print("Previous Block Hash:" + str(b.prebhash) + "\n")


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


def get_hash(block):
    data = '?' + str(block.nonce) + '@' + str(block.bindex) + '%' + \
        str(block.bdata) + '$' + str(block.prebhash)
    sha=sha256()
    sha.update(data)
    return sha.hexdigest()


def get_nonce(block, difty=0):
    pofw = str(0)*difty
    for attempt in bruteforce(characters, NNN):
        block.nonce = attempt
        if str(get_hash(block))[:difty] == pofw:
            break
    return 0
 

def createGenb():
    return Block(0, "Genesis Block", "0")


def loadc(name):
    f = open(str(name), 'r')
    cstring = f.read()
    BC = BlockChain()
    for block in cstring.split("#")[1:]:
        split_block1 = block.split('@')
        split_block2 = split_block1[1].split('%')
        split_block3 = split_block2[1].split('$')
        BC.chain.append(Block(int(split_block2[0]), str(split_block3[0]), split_block3[1], split_block1[0] ))
        BC.clenght = len(BC.chain)
    return BC
    

