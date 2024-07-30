import matplotlib.pyplot as plt

# Define initial variables
m1 = 100
x1 = 0.95
m2 = 300.47
x2 = 0.069825
n = 0.1088
times = 1800

# Lists to store time and abundances
time_list = []
x1_list = []
x2_list = []

# Loop to calculate and store the values
for i in range(times + 1):  # Loop from 0 to times (inclusive)
    x2 = (m2 * x2 + n * x1) / (m2 + n)
    x1 = (n * x2 + (m1 - n) * x1) / m1
    time_list.append(i)
    x1_list.append(x1)
    x2_list.append(x2)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_list, x1_list, label='6Li abundance in electrode (x1)')
plt.plot(time_list, x2_list, label='6Li abundance in electrolyte (x2)')
plt.xlabel('Time')
plt.ylabel('6Li Abundance')
plt.title('6Li Abundance in Electrode and Electrolyte Over Time')
plt.legend()
plt.grid(True)
plt.show()
