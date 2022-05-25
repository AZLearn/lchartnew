""" token GitHub 
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


https://stackoverflow.com/questions/68788998/authentication-was-removed-please-use-a-personal-access-token-instead
https://stackoverflow.com/questions/68780819/when-i-try-to-pull-or-push-in-github-i-am-getting-an-error-message-please-use
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:44:12 2020

@author: vanPC2015
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

#chart_data = pd.DataFrame(
     #np.random.randn(70, 3),
     #columns=['A', 'B', 'C'])

#st.line_chart(chart_data)

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(4)  # 👈 This makes the function take 2s to run
    return a * b

a = 3
b = 100
res = expensive_computation(a, b)

st.write("Result:", res)

import os
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#arr = np.random.normal(1, 1, size=100)
#plt.hist(arr, bins=20)
#st.pyplot()

t = np.arange(16.)
pics = np.zeros(16)
pics[0] = 0.
pics[1] = -1.
pics[2] = -4.
pics[3] = -3.
pics[4] = -5.
pics[5] = -2.
pics[6] = -8.
pics[7] = -5.
pics[8] = 0.
pics[9] = -5.
pics[10] = -3.
pics[11] = -1.
pics[12] = -7.
pics[13] = -5.
pics[14] = -3.
pics[15] = -1.

fig = plt.figure(figsize=(8,6), dpi=80)

plt.subplot(111)
plt.scatter(t, pics, color='blue', s= 20.)
plt.plot(t, pics, color='red', linewidth=1.0, linestyle="-")
plt.xticks(np.linspace(0., 15., 16, endpoint= True))
plt.yticks(np.linspace(-9., 0., 10, endpoint= True))
plt.grid(True)
plt.title('... Test scatter plot ***** ')
plt.legend()

st.pyplot(fig)

