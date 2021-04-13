import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()
fig1 =ff.create_distplot([data],["average"],show_hist=False)
#fig1.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))

fig1.show()

mean_pop=statistics.mean(data)
std_pop=statistics.stdev(data)
print("mean :"+str(mean_pop))
print("standard Deviation :"+str(std_pop))

def random_setof_mean(counter):
    data_list=[]
    for i in range(0,counter):
        rand=random.randint(0,len(data)-1)
        data_list.append(data[rand])

    mean=statistics.mean(data_list)
    return mean

def setup():
    mean_list=[]
    for i in range(0,1000):
        meanof_random_dataset=random_setof_mean(100)
        mean_list.append(meanof_random_dataset)
    mean_sam=statistics.mean(mean_list)
    std_sam=statistics.stdev(mean_list)
    print("mean :"+str(mean_sam))
    print("standard Deviation :"+str(std_sam))

    fig=ff.create_distplot([mean_list],["average"],show_hist=False)
   # fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

setup()