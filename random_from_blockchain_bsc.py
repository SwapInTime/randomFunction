##############################################################################
# Swap In Time
#
# randomFromBlockchainBSC is a python function that extracts a random number
# by initializing the seed from a string formed by the hash of the last block
# of the BSC (Binance Smart Chain) blockchain followed by the block number.
# 
# Example seed:
# 0x889627d51cea0371dbd93e8c6ff72f537e210ce32df9379296e0d724838977c29144233
# 0x7b7aa7feb5138edb0f28fdbadd0941b59400dee70f52de97f96478099db8c6669144268
# 0xbb8be2a84e404c9f424a000cf7ac7a65004a07672bf5cd01dbf92d9fc034583a9144277
##############################################################################

from web3 import Web3
from web3.middleware import geth_poa_middleware
import random

# return int from min_r to max_r
# if error return 9999
def randomFromBlockchainBSC(min_r, max_r) -> int:
    try:
        bsc = "https://bsc-dataseed.binance.org/"  #https://docs.binance.org/smart-chain/developer/rpc.html
        web3 = Web3(Web3.HTTPProvider(bsc))
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        if web3.isConnected():
            n_last_block = web3.eth.block_number
            blockHash = web3.eth.getBlock(n_last_block).hash
            seed_str = blockHash.hex()+str(n_last_block)
            #print(seed_str)
            random.seed(seed_str) #With version 2 (the default), a str, bytes, or bytearray object gets converted to an int and all of its bits are used.
            random_tmp = random.randint(min_r, max_r)
            return random_tmp
        else:
            return 9999
    except:
        return 9999

def main() -> None:
    random_test = randomFromBlockchainBSC(0,99)
    print(str(random_test))

if __name__ == '__main__':
    main()
