import numpy as np
import random
import matplotlib.pyplot as plt
import math
import pandas as pd
from datetime import datetime

# CREATE RANDOM DATASET

# n_readings = total number of readings
# n_ samples = total number of samples in each reading
# frac_normal = fraction of total number of readings that will be normal aka no stenosis (a float between 0 to 1) 
# min_val = minimum value of audio signal (usually zero)
# max_val = maximum value of audio signal in normal reading (no stenosis)
# increment = how much to increase each iteration's value by

def create_data(n_readings, n_samples, frac_normal, min_val, max_val, increment): #n_samples in multiples of 5 please!
  dataset = []

  n_normal = (frac_normal)*n_readings #number of readings that are normal readings
  for i in range(int(n_normal)):
    dataset.append(np.array(np.random.uniform(min_val, max_val, n_samples)))
  
  n_rest = (1-frac_normal)*n_readings #the rest of the readings will show gradual increase in stenosis
  new_max_val = max_val

  for i in range(int(n_rest)):
    #new_min_val += np.random.uniform(0,increment) #adding a random number to increase the min val - NOT IN USE ANYMORE
    new_max_val += np.random.uniform(0,increment) #adding a random number to increase the max val
    noise = list(np.random.uniform(min_val, max_val, int(0.2*n_samples)))
    spike = list(np.random.uniform(min_val, new_max_val, int(0.6*n_samples)))
    dataset.append(np.array(noise + spike + noise)) #assume all readings take the same structure
  
  return dataset

##########################################################################################################################################

# Plots graph for each reading within the created dataset

def plot_dataset(dataset):
  ymax = math.ceil(max(sample_data[len(dataset)-1]))
  for i in range(len(dataset)):
    plt.plot(sample_data[i])
    plt.title('Reading %s' % (i+1))
    plt.xlabel('Time')
    plt.ylabel('Audio signal detected')
    plt.grid(color="#D6EAF8")
    plt.ylim(0,ymax)
    plt.show()

##########################################################################################################################################

# Plot one reading

def plot_reading(reading, title, xlabel, ylabel):
  ymax = math.ceil(max(reading))
  plt.plot(reading)
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.grid(color="#D6EAF8")
  plt.ylim(0,ymax)
  plt.show()

##########################################################################################################################################

def create_avglist(dataset):
  avg_list = []
  for i in range(len(dataset)):
    avg_list.append(np.average(dataset[i]))
  return avg_list

#################################################### STEP 1: CREATE DATA #################################################################

####################### Create base measurement data #######################

n_days = 100 # for how many consecutive days that data has been collected!

sample_data = create_data(n_days, 300, 0.4, 0, 2, 0.05)
#plot_reading(sample_data[0], 'Reading Plot', 'Time', 'Audio signal detected')
#plot_reading(sample_data[499], 'Reading Plot', 'Time', 'Audio signal detected')

data = sample_data[80]
time = list(range(1,301,1))
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(time, data, label='Raw Data')
y_avg = [np.mean(data)] * len(data)
ax.plot(time, y_avg, color='red', ls='--', label="Average Reading")
plt.xlabel("Time")
plt.ylabel("Signal acquired")
plt.ylim(0,5)
plt.legend()
plt.show()

# Find average audio signal per reading

full_data = create_avglist(sample_data)
#plot_reading(full_data, 'Average values across readings', 'Reading', 'Average audio signal')

####################### Create list of sample dates for period n_days #######################

datetime_list = pd.date_range(end = datetime.today(), periods = n_days).to_pydatetime().tolist()
date_list = []
for i in range(len(datetime_list)):
  date_list.append(str(datetime_list[i])[0:10])

#print(date_list)
print("Start date: ", date_list[0], "| End date: ", date_list[len(date_list)-1])

####################### Create Pandas Dataframe #######################

df = pd.DataFrame(list(zip(date_list, full_data)), columns =['Date', 'Daily Mean'])
df # This must be the last line to display df. Otherwise, use print(df)

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

####################################################### STEP 2: PLOTTING DATA ############################################################

y = df['Daily Mean']
fig, ax = plt.subplots(figsize=(20, 6))
plt.grid(color="#D6EAF8")
plt.title("Trendline Plot")
ax.plot(y,marker='.', linestyle='-', linewidth=0.5, label='Daily')
ax.plot(y.resample('W').mean(),marker='o', markersize=8, linestyle='-', label='Weekly Mean')
ax.set_ylabel('Audio signal acquired')
ax.legend();

####################################################### OPTIONAL: PLOTTING ALL DATA ############################################################

#for i in range(len(sample_data)):
#  data = sample_data[i]
#  time = list(range(1,301,1))
#  fig, ax = plt.subplots(figsize=(8, 6))
#  ax.plot(time, data, label='Raw Data')
#  y_avg = [np.mean(data)] * len(data)
#  ax.plot(time, y_avg, color='red', ls='--', label="Average Reading")
#  plt.title("Recording for Day " + str(i))
#  plt.xlabel("Time")
#  plt.ylabel("Signal acquired")
#  plt.ylim(0,5)
#  plt.legend()
#  plt.show()
