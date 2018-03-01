# blockchainlittle
A small implementation of a blockchain ledger.

## Description 

A small implementation of a blockchain ledger done with Python3 to understand better the technology. As it is said, it is only the ledger, with a nonce and a proof of work mechanism. There is no distribution mechanisms and selection mechanisms (yet). 

This code has the capacity of creating a blockchain as descrived [here](https://unwttng.com/what-is-a-blockchain) [1], and adding blocks with some 'data' or information on them. It can also display the blocks and the state of the blockchain can be saved and loadad to/from a file. 

On the file the block is saved as:

 

> {inx : %d, msg : %s, phs : %d, nnc : %d }

it is a python dictionary.

This code contains two classes:

* Block, a block of the blockchain with an indexm, the data that the block chain carries, the previous bloc hash and the nonce.
* Blockchain, the ledger 'per se'. It is formed as a python list of Blocks in memory


## Use



## Warnings:

The data has to be the most basic ascii, as the read() function does not take special characters like Ñ or à. 

## License:

I choose to put this work on the public domain. 

## TODO:

* UPDATE README WITH NEW FORMAT
* Validate the genesis block on the validate_chain_zero function

 [1] https://unwttng.com/what-is-a-blockchain