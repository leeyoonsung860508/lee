import datetime as date
import createblock as cb
import nextblock as nb

def next_block(last_block):
    this_index = last_block.index +1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block" + str(this_index)
    this_hash = last_block.hash
    return cb.Block(this_index, this_timestamp, this_data, this_hash)

