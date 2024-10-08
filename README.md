# Lite-ProSENet
The officie pytorch code of our paper [Multimodal Learning for Non-small Cell Lung Cancer Prognosis](https://arxiv.org/pdf/2211.03280.pdf)

#### AUthors:
* [Yujiao Wu](https://scholar.google.com/citations?user=4t9fSdwAAAAJ&hl=zh-CN), [Yaxiong Wang](https://scholar.google.com/citations?user=lDChiR4AAAAJ&hl=zh-CN), [Xiaoshui Huang](https://xiaoshuihuang.github.io/), [Fan Yang](https://www.linkedin.com/in/fanyang0510/), [Sai Ho Ling](https://ieeexplore.ieee.org/author/37594256300), [Steven Su](https://profiles.uts.edu.au/Steven.Su)

## Introduction
The Illustration of Lite-ProSENe:

<img src="https://github.com/wangyxxjtu/Lite-ProSENet/blob/main/figures/framework.png" width="845" alt="workflow" />

### Overview

This paper focuses on the task of survival time analysis for lung cancer. Although much progress has been made in this problem in recent years, the performance of existing methods is still far from satisfactory. Traditional and some deep learning- based survival time analyses for lung cancer are mostly based on textual clinical information such as staging, age, histology, etc. Unlike existing methods that predicting on the single modality, we observe that a human clinician usually takes multimodal data\ such as text clinical data and visual scans to estimate survival time. Motivated by this, in this work, we contribute a smart cross-modality network for survival analysis network named Lite-ProSENet that simulates a human’s manner of decision making. To be specific, Lite-ProSENet is a two-tower architecture that takes the clinical data and the CT scans as inputs to create the survival prediction. The textural tower is responsible for modelling the clinical data, we build a light transformer using multi-head self-attention as our textural tower. The visual tower (namely ProSENet) is responsible
for extracting features from the CT scans. The backbone of ProSENet is a 3D Resnet that works together with several repeatable building block named 3D-SE Resblock for a compact feature extraction. Our 3D-SE Resblock is composed of a 3D channel “Squeeze-and-Excitation” (SE) block and a temporal SE block. The purpose of 3D-SE Resblock is to adaptively select the valuable features from CT scans. Besides, to further filter out the redundant information among CT scans, we develop a simple but effective frame difference mechanism that takes the performance of our model to the new state- of-the-art. Extensive experiments were conducted using data from 422 NSCLC patients from The Cancer Imaging Archive (TCIA). The results show that our Lite-ProSENet outperforms favorably again all comparison methods and achieves the new state of the art with the 89.3% on concordance.



## Usage
### Data Prepration
We considered 422 NSCLC patients from TCIA to assess the proposed framework, download from [here](https:)

### Environment setup
Our experiments are conducted with Python 3.6.9, Pytorch 1.2.0, CUDA 11.5.
```
#create a virual environment using anaconda
conda create -n LiteProTrans python=3.6
#Install all dependencies:
pip install -r requirements.txt
```


### 🌻 Training and testing
```
#training option 1
CUDA_VISIBLE_DEVICES=GPU_ID python main.py --ckpt_path ./ --data_root ./data/ --alpha 0.5 --beta 0.5 --seed 1000
#training option 2, specify the configurations in train.sh and run
sh train.sh

#testing option 1
CUDA_VISIBLE_DEVICES=GPU_ID python test.py --data_path ./data/test  --ckpt ./best.pth --seed 1000
#testing option 2, specify the configurations in eval.sh and run
sh eval.sh
```

## Performance
Our model can acheive STOA performance on practical dataset:
<img src="https://github.com/wangyxxjtu/Lite-ProSENet/blob/main/figures/performance.png" width="845" alt="workflow" />

## Citation
If you think this repo useful, please cite
```
@article{DBLP:journals/corr/abs-2211-03280,
  author       = {Yujiao Wu and
                  Yaxiong Wang and
                  Xiaoshui Huang and
                  Fan Yang and
                  Sai Ho Ling and
                  Steven Weidong Su},
  title        = {Multimodal Learning for Non-small Cell Lung Cancer Prognosis},
  journal      = {CoRR},
  volume       = {abs/2211.03280},
  year         = {2022},
  url          = {https://doi.org/10.48550/arXiv.2211.03280},
  doi          = {10.48550/arXiv.2211.03280},
  eprinttype    = {arXiv},
  eprint       = {2211.03280},
  timestamp    = {Wed, 09 Nov 2022 17:33:26 +0100},
  biburl       = {https://dblp.org/rec/journals/corr/abs-2211-03280.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```
