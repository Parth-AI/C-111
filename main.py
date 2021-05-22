import csv
import pandas as pd
import plotly.figure_factory as pff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv('studentMarks.csv')
df_1 = pd.read_csv('data1.csv')
df_2 = pd.read_csv('data2.csv')
df_3 = pd.read_csv('data3.csv')

ls = df['Math_score'].to_list()
df1 = df_1['Math_score'].to_list()
df2 = df_2['Math_score'].to_list()
df3 = df_3['Math_score'].to_list()

m_m = statistics.mean(ls)
m_std = statistics.stdev(ls)

df1_m = statistics.mean(df1)
df1_std = statistics.stdev(df1)
print(df1_m)
print(df1_std)

df2_m = statistics.mean(df2)
df2_std = statistics.stdev(df2)
print(df2_m)
print(df2_std)

df3_m = statistics.mean(df3)
df3_std = statistics.stdev(df3)
print(df3_m)
print(df3_std)

print(m_m)
print(m_std)


d1 = (df1_m - m_m) / m_std
print(f'Z Score {d1}')

d2 = (df2_m - m_m) / m_std
print(f'Z Score {d2}')

d3 = (df3_m - m_m) / m_std
print(f'Z Score {d3}')

def random_set_of_mean(counter):
     dataset = []
     for i in range(0, counter):
          random_index = random.randint(0, len(ls)-1)
          value = ls[random_index]
          dataset.append(value)
     mean = statistics.mean(dataset)
     return mean

mean_list = []
for i in range(0, 1000):
     set_of_means = random_set_of_mean(100)
     mean_list.append(set_of_means)

mn_m = statistics.mean(mean_list)
mn_std = statistics.stdev(mean_list)

print(f'Mean of sampling distribution {mn_m}')
print(f'Mean of sampling distribution {mn_std}')

m_std_first, m_std_end = mn_m - mn_std, mn_m + mn_std
m_std_sec_s, m_std_sec_e = mn_m - (mn_std*2), mn_m + (mn_std*2)
m_std_three_s, m_std_three_e = mn_m - (mn_std*3), mn_m + (mn_std*3)

m1_std_first, m1_std_end = mn_m - mn_std, mn_m + mn_std

m2_std_first, m2_std_end = mn_m - mn_std, mn_m + mn_std

m3_std_first, m3_std_end = mn_m - mn_std, mn_m + mn_std

"""print(f'Std 1: {m_std_first}{m_std_end}')
print(f'Std 2: {m_std_sec_s}{m_std_sec_e}')
print(f'Std 3: {m_std_three_s}{m_std_three_e}')"""

gph = pff.create_distplot([mean_list], ['Score'], show_hist = False)
#gph.add_trace(go.Scatter(x=[mn_m, mn_m], y=[0, 0.17], mode = "lines", name = "Mean"))

"""gph.add_trace(go.Scatter(x=[m_std_first, m_std_first], y=[0, 0.17], mode = "lines", name = "std 1 s"))
gph.add_trace(go.Scatter(x=[m_std_end, m_std_end], y=[0, 0.17], mode = "lines", name = "std 1 e"))
gph.add_trace(go.Scatter(x=[m_std_sec_s, m_std_sec_s], y=[0, 0.17], mode = "lines", name = "std 2 s"))
gph.add_trace(go.Scatter(x=[m_std_sec_e, m_std_sec_e], y=[0, 0.17], mode = "lines", name = "std 2 e"))
gph.add_trace(go.Scatter(x=[m_std_three_s, m_std_three_s], y=[0, 0.17], mode = "lines", name = "std 3 s"))
gph.add_trace(go.Scatter(x=[m_std_three_e, m_std_three_e], y=[0, 0.17], mode = "lines", name = "std 3 e"))"""

gph.add_trace(go.Scatter(x=[df1_m, df1_m], y=[0, 0.17], mode = "lines", name = "Mean 1"))

gph.add_trace(go.Scatter(x=[m1_std_first, m1_std_first], y=[0, 0.17], mode = "lines", name = "std 1 s"))
gph.add_trace(go.Scatter(x=[m1_std_end, m1_std_end], y=[0, 0.17], mode = "lines", name = "std 1 e"))

gph.add_trace(go.Scatter(x=[df2_m, df2_m], y=[0, 0.17], mode = "lines", name = "Mean 2"))

gph.add_trace(go.Scatter(x=[m2_std_first, m2_std_first], y=[0, 0.17], mode = "lines", name = "std 2 s"))
gph.add_trace(go.Scatter(x=[m2_std_end, m2_std_end], y=[0, 0.17], mode = "lines", name = "std 2 e"))

gph.add_trace(go.Scatter(x=[df3_m, df3_m], y=[0, 0.17], mode = "lines", name = "Mean 3"))

gph.add_trace(go.Scatter(x=[m3_std_first, m3_std_first], y=[0, 0.17], mode = "lines", name = "std 3 s"))
gph.add_trace(go.Scatter(x=[m3_std_end, m3_std_end], y=[0, 0.17], mode = "lines", name = "std 3 e"))


gph.show()
