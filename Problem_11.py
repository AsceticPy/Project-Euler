#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:20:57 2021

@author: Habbo3
"""
from typing import Optional, List

Grille = List[List[Optional[int]]]

data_file = open("data_11.txt", "r")
grille: Grille = []

while True:
    line = data_file.readline().strip().split()
    if not line:
        break

    
    grille.append(list(map(int, line)))

data_file.close

max_num = 0
temp = 0

for n in range(20):
	if n + 4 <= 20:
		for i in range(0, 20):
			if i + 4 <= 20 and n + 4 <= 20:
				temp = grille[n][i] * grille[n + 1][i + 1] * grille[n + 2][i + 2] * grille[n + 3][i + 3]
				if temp > max_num:
					max_num = temp
			if i - 4 >=0 and n + 4 <=20:
				temp = grille[n][i] * grille[n + 1][i - 1] * grille[n + 2][i - 2] * grille[n + 3][i - 3]
				if temp > max_num:
					max_num = temp
			if n + 4 >= 0:
				temp = grille[n][i] * grille[n + 1][i] * grille[n + 2][i] * grille[n + 3][i]
				if temp > max_num:
					max_num = temp
			if i + 4 <= 20:
				temp = grille[n][i] * grille[n][i + 1] * grille[n][i + 2] * grille[n][i + 3]
				if temp > max_num:
					max_num = temp

print("The max sum is : ", max_num)

