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
        block.nonce = attempt
        if str(get_hash(block))[:n] == level:
            break

def get_nonce_small(block, n):
    """Computes a the nonce such that the hash of the block is smaller than n.
    This has much finer control than ZERO method, it is the one used by Bitcoin """

    for attempt in bruteforce(characters, NNN):
        block.nonce = attempt
        if int(get_hash(block), 16) < n:
            break

