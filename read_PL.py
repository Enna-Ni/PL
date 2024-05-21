#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:25:37 2024

@author: enna
"""
import datetime
import pandas as pd
import numpy as np
import os


def calc_sec(filename, path):
    
    link = filename
    print("Начало")
    print(datetime.datetime.now())
    
    with open(link, mode='r') as file:
        count = 0
        for line in file:
            if line == "":
                break
            elif "#" in line:
                if 'rec' in line:
                    i = 0
                    if count == 0:
                        continue
                    li = line.split(",")[-1]
                    li = int(li.split("=")[-1])
                    
                    df['t'] = df['t'].apply(int)
                    df['x'] = df['x'].apply(int)
                    df['y'] = df['y'].apply(int)
            
                    df_cut = df[df['t']<= 999999999]
                    # print(df_cut)
        
                    img = np.zeros((512,512))
        
                    for index, row in df_cut.iterrows():
                        img[row['x'], row['y']] += 1
            
                    second = li
                    # plt.imshow(img)
                    # plt.title(second)
                    # plt.show()
                    np.save(path + str(second), img)
                    # print()
                    print("file "+ save_path, str(second) + " written")
                    
                    print(line, datetime.datetime.now())
                                    
                    
                else:
                    print(line)
                    df = pd.DataFrame({'t': pd.Series(dtype='int'),
                                   'x': pd.Series(dtype='int'),
                                   'y': pd.Series(dtype='int'),
                                   'f': pd.Series(dtype='int')})
                    if "###" in line:
                        count = 0
                    else:
                        count = 0
                        
                continue
                    
            else:
                df.loc[i] = line.split()
                i += 1
                count = 1
                
    print("Завершение")
    print(datetime.datetime.now())   




curr_dir = os.getcwd()
try:
    os.makedirs(curr_dir+"/ser_1")
except FileExistsError:
    pass    
try:
    os.makedirs(curr_dir+"/ser_2")
except:
    pass

data_path = curr_dir + "/Data/"

file_list = sorted(os.listdir(data_path))
ser1_list = file_list[:7]
ser2_list = file_list[7:]

print(ser1_list)
print(ser2_list)

# ser_1
for i in range(6, len(ser1_list) + 1):
    read_path = data_path + ser1_list[i-1]
    try:
        save_path = curr_dir + "/ser_1/img"+ str(i) + "/"
        os.makedirs(save_path)
    except FileExistsError:
        pass
    # calc_sec(read_path, save_path)

# ser_2
for i in range(1, len(ser2_list) + 1):
    read_path = data_path + ser2_list[i-1]
    try:
        save_path = curr_dir + "/ser_2/img"+ str(i) + "/"
        os.makedirs(save_path)
    except FileExistsError:
        pass
    calc_sec(read_path, save_path)
    
