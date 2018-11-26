#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: r.li
@license: Apache Licence 
@contact: r.li@bmi-tech.com
@site: 
@software: PyCharm
@file: visualize.py
@time: 18-11-19 上午11:38
@brief： 
"""
import cv2

from face_alignment.utils.data_loader import PtsDataset, ArrayDataset, AFLW2000Dataset, LP300W_Dataset
from face_alignment.utils.cv2_utils import plot_kpt
import numpy as np
import tensorflow as tf


def vis_dataset(dataset):
    train_data = dataset(batch_size=1, shuffle=False, repeat_num=1)
    print("len ", len(dataset))
    next_element = train_data.make_one_shot_iterator().get_next()
    with tf.Session() as sess:
        try:
            while True:
                img, kpt = sess.run(next_element)
                # print(img.shape, kpts.shape)
                img = np.squeeze(img)
                kpt = np.squeeze(kpt)

                cv2.imshow("out", plot_kpt(img.astype(np.uint8), kpt))
                cv2.waitKey(0)

        except tf.errors.OutOfRangeError:
            pass

        except Exception:
            print("err")


if __name__ == '__main__':
    from face_alignment.utils.data_utils import crop_by_kpt
    # dataset = PtsDataset("/media/lirui/Personal/DeepLearning/FaceRec/datasets/300W",
    #                      ["afw", "helen/trainset"],
    #                      transform=crop_by_kpt, verbose=True)
    dataset = ArrayDataset('../../data/dataset_nimgs=20000_perturbations=[0.2, 0.2, 20, 0.25]_size=[112, 112].npz')
    # dataset = AFLW2000Dataset("/media/lirui/Personal/DeepLearning/FaceRec/LBF3000fps/datasets", verbose=True)
    # dataset = LP300W_Dataset("/media/lirui/Personal/DeepLearning/FaceRec/datasets/300W_LP", ["AFW_Flip"], verbose=True)
    print("n sample ", len(dataset))
    vis_dataset(dataset)