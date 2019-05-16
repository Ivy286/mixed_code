#!usr/bin/env python
# conver DFT energy
#coding: utf-8

import numpy as np


def getData(filename):
    h_list = []
    sigma_list = []
    fai_list = []
    with open(filename, 'r') as f:
        for line in f:
            h, sigma, fai = list(map(float, line.strip().split(',')[1:]))
            h_list.append(h)
            sigma_list.append(sigma)
            fai_list.append(fai)
    return h_list, sigam_list, fai_list



def Tm(H, sigma, fai):
    R = 8.314
    return H/(50- R*np.log(sigma) + R*np.log(fai))


if __name__ == '__main__':
    h, sigma, fai = getData('XX.csv')
    h = np.array(h)
    sigma = np.array(sigma)
    fai = np.array(fai)
    print(Tm(h,sigma, fai))
