import os
import random

#the data of NSCLC, assume you save the data in ./data folder
root_path = './data'

#filenames = [os.path.join(root_path, idx) for idx in os.listdir(root_path)]
#filenames = list(filter(lambda item: 'GTV' in item, filenames))

filenames = list(range(100))

random.shuffle(filenames)
#data split
train_ratio, val_ratio =0.6, 0.2
train_endat, val_endat = int(train_ratio*len(filenames)), int((train_ratio+val_ratio)*len(filenames))

train_list = filenames[:train_endat]
val_list = filenames[train_endat:val_endat]
test_list = filenames[val_endat:]

import pdb
pdb.set_trace()
with open('train_filenames.txt', 'w') as f:
    rest = '\n'.join(train_list)
    f.write(rest)

with open('val_filenames.txt', 'w') as f:
    rest = '\n'.join(val_list)
    f.write(rest)

with open('test_filenames.txt', 'w') as f:
    rest = '\n'.join(test_list)
    f.write(rest)


