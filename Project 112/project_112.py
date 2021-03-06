# -*- coding: utf-8 -*-
"""Project 112.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iGvFXPlGLbMQKfmdq_J3z67DbySnmeoF
"""

import plotly.express as px
import pandas as pd
import csv

from google.colab import files
dataToLoad = files.upload()

df = pd.read_csv("data.csv")
fig = px.scatter(df, y = "quant_saved", title = "Qty of Money($) saved by women", color = "female")
fig.show()

import csv

with open('data.csv', newline="") as f:
  reader = csv.reader(f)
  savingsData = list(reader)

savingsData.pop(0)

totalPeople = len(savingsData)
reminderCounter = 0
for i in savingsData:
  if int(i[3]) == 1:
    reminderCounter += 1

import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[reminderCounter, (totalPeople - reminderCounter)]))

fig.show()