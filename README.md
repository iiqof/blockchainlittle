# blockchainlittle
A small implementation of a blockchain ledger.

## Description 

A small implementation of a blockchain ledger done with Python3 to understand better the technology. As it is said, it is only the ledger, with a nonce and a proof of work mechanism. There is no distribution mechanisms and selection mechanisms (yet). 

This code has the capacity of creating a blockchain as descrived [here](https://unwttng.com/what-is-a-blockchain) [1], and adding blocks with some 'data' or information on them. It can also display the blocks and the state of the blockchain can be saved and loadad to/from a file. 

On the file the block is saved as:

 | #nonce@block_index%data_on_the_block$hash_of_previous_block

This code contains two classes:

* Block, a block of the blockchain with an indexm the data that the block chain carries and the previous bloc hash.
* Blockchain, the ledger 'per se'. It is formed as a python list of Blocks.


## Use

1) _Create BlockChain_, this creates an empy blockchain

> blockchain = BlockChain 

2) _Initialize the blockchain_, adds a *Genesis Block* (@0%Genesis Block$0) to the blockchain.

> blockchian.initc()

3) _Create a block_, 

> block = Block(index, data, previous_block_hash, nonce)

3.5) _Compute a nonce_, finds a valid nonce for a block with difficoulty level.

> block.get_nonce(difficoulty_level)

4) _Add a new block to the blockchain_, creats block (@previous_block_index + 1%data$previosu_block_hash) from the data suplied and adds it to the blockchain.

> blockcain.accb(data, difficoulty) 

The block will be rejected if it doesn't fullfill the difficoulty level (first digits of the hasharen't zero)

5) _Save the blockchain_

6) _Load a blockchain_

## Warnings:

The data has to be the most basic ascii, as the read() function does not take special characters like Ñ or à. Also @ $ % are reserved characters that marck structure on a block.

## TODO:

* Create a block chain integrity check.
* Invert the order of the chain so that we have the head of the chian inthe 0th possition.
* Add saveguards for @ $ % #   
* Add blockchain analysis (size,...)    
* Add documentation 


 [1] https://unwttng.com/what-is-a-blockchain
