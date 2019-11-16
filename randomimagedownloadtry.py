# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:09:14 2019

@author: ktjgu
"""

import os
import random
import string
import urllib.request

#variables
BASE_URL = "http://imgur.com/"
CHARSET = string.ascii_letters + string.digits
DIR_PATH = "images/"

#lambda
gen_alpha = lambda: ''.join(random.sample(CHARSET, 5))
gen_url = lambda suffix: ''.join(BASE_URL + suffix)

#functions
def main():
    CURR_SUFF = gen_alpha()
    print(CURR_SUFF, sep = '', end = '')

    CURR_URL = gen_url(CURR_SUFF) + ".png"

    if not os.path.exists(DIR_PATH):
        os.makedirs(DIR_PATH)

    urllib.request.urlretrieve(CURR_URL, DIR_PATH + CURR_SUFF + ".png")
    
    if os.stat(DIR_PATH + CURR_SUFF + ".png").st_size < 1024:
        os.remove(DIR_PATH + CURR_SUFF + ".png")
        print(" - invalid, was removed :(")
    else: print(" - valid, was downloaded :)")


if __name__ == '__main__':
    for i in range(int(input("How many images should I try to download? "))):
        main()