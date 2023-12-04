# Customer-Acquisition-Cost (CAC) Estimation for uStock over the next 2 years
import numpy as np
import matplotlib.pyplot as plt

# Constants
initial_cac = 1000
regular_engineer_impact = 0.5 / 100
talented_engineer_impact = 1 / 100
talented_ratio = 0.20

# Adjusted constants for word of mouth effect
word_of_mouth_impact = 0.05 / 100
regular_engineer_impact_word_of_mouth = 0.4 / 100
talented_engineer_impact_word_of_mouth = 0.8 / 100

# Function to calculate monthly CAC considering word of mouth
def calculate_cac_word_of_mouth(month, previous_cac):
    # Linear growth of engineers
    if month <= 12:
        engineers = (5 / 12) * month
    else:
        engineers = 5 + (5 / 12) * (month - 12)

    talented_engineers = engineers * talented_ratio
    regular_engineers = engineers - talented_engineers

    # Calculate the improvement factor including word of mouth
    improvement = (regular_engineers * regular_engineer_impact_word_of_mouth +
                   talented_engineers * talented_engineer_impact_word_of_mouth +
                   word_of_mouth_impact)

    # Marketing spikes (reduced impact)
    if month % 5 == 0:
        return max(previous_cac - previous_cac * improvement + 0.25, 1)  # $0.25 spike, minimum $1

    return max(previous_cac - previous_cac * improvement, 1)  # Minimum CAC of $1

# Monthly customer acquisition cost considering word of mouth
cac_word_of_mouth = [initial_cac_free]
for month in range(1, 24):  # 2 years = 24 months
    cac_word_of_mouth.append(calculate_cac_word_of_mouth(month, cac_word_of_mouth[-1]))

# Plotting
plt.figure(figsize=[10, 6])
plt.plot(cac_word_of_mouth, label='Customer Acquisition Cost')
plt.title('Estimated Customer Acquisition Cost (CAC) Over 2 Years Considering Word of Mouth (USD)')
plt.xlabel('Months')
plt.ylabel('Customer Acquisition Cost (USD)')
plt.axhline(y=cac_word_of_mouth[-1], color='r', linestyle='--', label='Final CAC')
plt.legend()
plt.grid(True)
plt.show()

cac_word_of_mouth[-1]  # Final CAC value after 2 years
