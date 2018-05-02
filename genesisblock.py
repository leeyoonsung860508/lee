import datetime as date
import createblock as cb

def create_genesis_block():
    return cb.Block(0, date.datetime.now(), "Genesis Block", "0")

