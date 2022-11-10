import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(31593)

st.title("College App Simulator")

reach = st.number_input("Number of \'Reach\' Schools", value = 3)
match = st.number_input("Number of \'Match\' Schools", value = 4)
likely = st.number_input("Number of \'Likely\' Schools", value = 3)

reachp = st.slider("Percent Accept for \'Reach\' Schools",
                   min_value = 0,
                   max_value = 100,
                   value = 15,
                   step = 1)
matchp = st.slider("Percent Accept for \'Match\' Schools",
                   min_value = 0,
                   max_value = 100,
                   value = 60,
                   step = 1)
likelyp = st.slider("Percent Accept for \'Likely\' Schools",
                   min_value = 0,
                   max_value = 100,
                   value = 80,
                   step = 1)

reachout = np.random.choice([True, False],
                            size = (1000, reach),
                            replace = True,
                            p = [reachp/100, 1-(reachp/100)])
matchout = np.random.choice([True, False],
                            size = (1000, match),
                            replace = True,
                            p = [matchp/100, 1-(matchp/100)])
likelyout = np.random.choice([True, False],
                            size = (1000, likely),
                            replace = True,
                            p = [likelyp/100, 1-(likelyp/100)])

reachagg = np.sum(reachout, axis = 1)
matchagg = np.sum(matchout, axis = 1)
likelyagg = np.sum(likelyout, axis = 1)

totagg = reachagg + matchagg + likelyagg
totmean = totagg.mean()
totno = (totagg == 0).sum()

reachmean = reachagg.mean()
reachno = (reachagg == 0).sum()

st.header('Admissions Outcomes')
st.write(f'Number of Colleges to Choose From \(On Average\): {totmean}')
st.write(f'Chances out of 1000 of No Acceptances: {totno}')
fig = plt.figure(figsize = (12,4))

sns.countplot(totagg)
st.pyplot(fig)

#st.write(f'Average Number of \'Reach\' Aceptances: {reachmean}')
#st.write(f'Chances out of 1000 of No \'Reach\' Acceptances: {reachno}')
#figreach = plt.figure(figsize = (12,4))
#sns.histplot(reachagg)
#st.pyplot(figreach)