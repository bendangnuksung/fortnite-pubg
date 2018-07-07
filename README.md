# Fortnite - PUBG
Originally inspired from this [blog](https://towardsdatascience.com/turning-fortnite-into-pubg-with-deep-learning-cyclegan-2f9d339dcdb0)

Converting Fortnite to PUBG using [CycleGAN](https://arxiv.org/abs/1703.10593) and vice versa using Keras

## Demo
This Model was trained with 50,000 image each of Fortnite and PUBG
Results after 3 Epochs

![demo]()

## Prerequisites
* python 3.5
* keras==2.1.5
* keras-contrib==2.0.8
* tensorflow==1.5.0
* opencv-python==3.4.0.12
* NVIDIA GPU CUDA

## Get Started

1. Prepare Data:
  * Copy your two directory containing images(Fortnite, PUBG) in 'data/raw/'
  * Then run the below command. This will save the data in batch numpy format at 'data/prepared/'
  ```sh
  # prepare data
  python3 prepare_data.py
  ```
2. Build Model
  * To build Model from scratch you can directly run 'fortnite_pubg.ipynb'
  <br/>OR<br/>
  * [Download](https://drive.google.com/file/d/10gWOh0opCzYzadhcfnc6YF936nWAOrrC/view) checkpoint and move it to 'checkpoint/' and run 'fortnite_pubg.ipynb'

## References
* [NIPS2016](https://github.com/soumith/ganhacks) hacks 
* [eriklindernoren](https://github.com/eriklindernoren/Keras-GAN)
* [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/pdf/1611.07004v1.pdf)