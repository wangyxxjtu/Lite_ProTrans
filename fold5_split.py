import os
import random

def fold5():
    #the data of NSCLC, assume you save the data in ./data folder
    root_path = './data'

    filenames = [os.path.join(root_path, idx) for idx in os.listdir(root_path)]
    filenames = list(filter(lambda item: 'GTV' in item, filenames))

    #shuffle the results
    random.shuffle(filenames)
    #data split
    train_ratio, val_ratio =0.6, 0.2
    train_endat, val_endat = int(train_ratio*len(filenames)), int((train_ratio+val_ratio)*len(filenames))

    train_list = filenames[:train_endat]
    val_list = filenames[train_endat:val_endat]
    test_list = filenames[val_endat:]

    '''with open('train_filenames.txt', 'w') as f:
        rest = '\n'.join(train_list)
        f.write(rest)

    with open('val_filenames.txt', 'w') as f:
        rest = '\n'.join(val_list)
        f.write(rest)

    with open('test_filenames.txt', 'w') as f:
        rest = '\n'.join(test_list)
        f.write(rest)

    '''
    return {'train':train_list, 'val':val_list, 'test':test_list}


Hua Li, Junyan Liang, Ruiqi Wu, Runmin Cong, Wenhui Wu, Sam Tak-Wu Kwong: Stereo Superpixel Segmentation via Decoupled Dynamic Spatial-Embedding Fusion Network. IEEE Trans. Multim. 26: 367-378 (2024)
