###############################################################################
#
#  Rutines for a prove of work Blockchain
#
#
#
#
# All the rutines are naive, probably betters can be done, but this is to learn the concepts
#
#
#
##############################
from hashlib import sha256
from blocks import Block, BlockChain
from crypto import bruteforce

characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NNN = 100  # Maximum lenght of the tried nonces

def get_hash(block):
    """ Hashes a block in its ascii form"""
    sha = sha256()
    sha.update(block.ascii_form())
    return sha.hexdigest()


def get_nonce_zero(block, n):
    """Computes a the nonce such that the hash of the block has n leading zeros """
    level = str(0)*n
    for attempt in bruteforce(characters, NNN):
        block.memblock['nnc'] = attempt
        if str(get_hash(block))[:n] == level:
            break


def get_nonce_small(block, n):
    """Computes a the nonce such that the hash of the block is smaller than n.
    This has much finer control than ZERO method, it is the one used by Bitcoin """

    for attempt in bruteforce(characters, NNN):
        block.memblock['nnc'] = attempt
        if int(get_hash(block), 16) < n:
            break


def validate_nonce_zero(block, n):
    """Validation function for the ZERO method"""
    return str(get_hash(block))[:n] == str(0)*n


def validate_nonce_small(block, n):
    """Validation function form the SMALL method"""
    return int(get_hash(block), 16) < n


def validate_previous(block, previous):
    """Checks that it has the previous blocks hash"""
    return block.memblock['phs'] == str(get_hash(previous))


def validate_chain_zero(chain, depth=0):
    """Validates the last 'depht' blocks of the chain, assuning that depht-1 is a valid block.
    Or if depth = 0, then it validates the whole chain"""
    if depth == 0:
        depth = chain.clength
    for i in range(chain.clength-1, chain.clength-1 - depth, -1):
        if i == 0:
            print('The chain is valid')  #TODO: Validate the genesis block
            return 0
        elif validate_nonce_zero(chain.chain[i], chain.chain[i-1].memblock['dft']) * \
             validate_previous(chain.chain[i], chain.chain[i-1]) == 1:
            print('Block {} correct'.format(i))
        else:
            print('Block {} not valid'.format(i))
            return -1
    return 0


def validate_chain_small(chain, depth=0):
    """Validates the last 'depht' blocks of the chain, assuning that depht-1 is a valid block.
    Or if depth = 0, then it validates the whole chain"""
    if depth == 0:
        depth = chain.clength
    for i in range(chain.clength-1, chain.clength-1 - depth, -1):
        if i == 0:
            print('The chain is valid')  #TODO: Validate the genesis block
            return 0
        elif validate_nonce_small(chain.chain[i], chain.chain[i-1].memblock['dft']) * \
             validate_previous(chain.chain[i], chain.chain[i-1]) == 1:
            print('Block {} correct'.format(i))
        else:
            print('Block {} not valid'.format(i))
            return -1
    return 0