import numpy as np
import random
import matplotlib.pyplot as plt
import math

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

# Create base measurement data

sample_data = create_data(500, 300, 0.4, 0, 2, 0.05)
#plot_reading(sample_data[0], 'Reading Plot', 'Time', 'Audio signal detected')
#plot_reading(sample_data[499], 'Reading Plot', 'Time', 'Audio signal detected')

####################################################### STEP 2: CLEANING DATA ############################################################

# Find average audio signal per reading

averages = create_avglist(sample_data)
#plot_reading(averages, 'Average values across readings', 'Reading', 'Average audio signal')

####################################################### STEP 3: PREDICTION ###############################################################

