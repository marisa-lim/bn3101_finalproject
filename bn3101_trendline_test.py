import numpy as np
import random
import matplotlib.pyplot as plt

##########################################################################################################################################
#################################################### STEP 1: CREATE DATA #################################################################
##########################################################################################################################################

# Create base measurement data

#noise = list(np.random.uniform(0, 2, 5)) # generate noise between 0-2
#spikes_2 = list(np.random.uniform(4, 5, 5)) # generate noise between 4-5
#spikes_3 = list(np.random.uniform(5, 6, 5)) # generate noise between 4-5
#spikes_4 = list(np.random.uniform(8, 10, 5)) # generate noise between 4-5
#spikes_5 = list(np.random.uniform(10, 12, 5)) # generate noise between 4-5

# each reading will have 300 entries in one np array

reading_1 = np.array(np.random.uniform(0, 2, 300)) # purely just noise - no stenosis
reading_2 = np.array(np.random.uniform(0, 2, 300)) # purely just noise - no stenosis

# some stenosis detected

# noise spike noise spike
reading_3 = np.array(list(np.random.uniform(0, 2, 150))+list(np.random.uniform(1, 3, 50))+list(np.random.uniform(0, 2, 50))+list(np.random.uniform(1, 3, 50)))
# noise spike noise spike noise
reading_4 = np.array(list(np.random.uniform(0, 2, 100))+list(np.random.uniform(1, 4, 50))+list(np.random.uniform(0, 2, 50))+list(np.random.uniform(1, 4, 50))+list(np.random.uniform(0, 2, 50)))
# noise spike noise spike
reading_5 = np.array(list(np.random.uniform(0, 2, 50))+list(np.random.uniform(1, 5, 100))+list(np.random.uniform(0, 2, 100))+list(np.random.uniform(1, 5, 50)))
# noise spike noise spike noise
reading_6 = np.array(list(np.random.uniform(0, 2, 100))+list(np.random.uniform(2, 5, 50))+list(np.random.uniform(0, 2, 50))+list(np.random.uniform(1, 5, 50))+list(np.random.uniform(0, 2, 50)))
# noise spike noise spike
reading_7 = np.array(list(np.random.uniform(0, 2, 150))+list(np.random.uniform(1, 6, 50))+list(np.random.uniform(0, 2, 50))+list(np.random.uniform(2, 5, 50)))
# noise spike noise spike
reading_8 = np.array(list(np.random.uniform(0, 2, 50))+list(np.random.uniform(2, 6, 100))+list(np.random.uniform(0, 2, 100))+list(np.random.uniform(2, 5, 50)))
# noise spike noise spike noise
reading_9 = np.array(list(np.random.uniform(0, 2, 100))+list(np.random.uniform(1, 5, 50))+list(np.random.uniform(0, 2, 50))+list(np.random.uniform(2, 7, 50))+list(np.random.uniform(0, 2, 50)))
# noise spike noise spike
reading_10 = np.array(list(np.random.uniform(0, 2, 50))+list(np.random.uniform(2, 7, 100))+list(np.random.uniform(0, 2, 100))+list(np.random.uniform(2, 8, 50)))

##########################################################################################################################################
####################################################### STEP 2: CLEANING DATA ############################################################
##########################################################################################################################################

# Find the number of spikes and value of spikes for each reading
reading_list = [reading_1, reading_2, reading_3, reading_4, reading_5, reading_6, reading_7, reading_8, reading_9, reading_10]

# get averages to compare
avg_list = []
for i in range(len(reading_list)):
  avg_list.append(np.average(reading_list[i]))

print("Average values for past reading are: ", avg_list)

# show average plot
plt.plot(avg_list)
plt.title('Trendline')
plt.xlabel('Readings')
plt.ylabel('Average signal')
plt.ylim(0,5)
plt.show()

##########################################################################################################################################
####################################################### OPTIONAL: PLOTTING DATA ##########################################################
##########################################################################################################################################


# plot each reading
ymax = 10

# reading 1 plot
plt.plot(reading_1)
plt.title('Reading 1')
plt.xlabel('Time')
plt.ylabel('Signal detected')
plt.ylim(0,ymax)
plt.show()

# reading 2 plot
plt.plot(reading_2)
plt.title('Reading 2')
plt.xlabel('Time')
plt.ylabel('Signal detected')
plt.ylim(0,ymax)
plt.show()

# reading 3 plot
plt.plot(reading_3)
plt.title('Reading 3')
plt.xlabel('Time')
plt.ylabel('Signal detected')
plt.ylim(0,ymax)
plt.show()

# reading 4 plot
plt.plot(reading_4)
plt.title('Reading 4')
plt.xlabel('Time')
plt.ylabel('Signal detected')
plt.ylim(0,ymax)
plt.show()

# reading 5 plot
plt.plot(reading_5)
plt.title('Reading 5')
plt.xlabel('Time')
plt.ylabel('Signal detected')
plt.ylim(0,ymax)
plt.show()