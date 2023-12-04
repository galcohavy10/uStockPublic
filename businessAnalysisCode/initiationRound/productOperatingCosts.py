# The cost of operating uStock product for year 1 & 2

import numpy as np
import matplotlib.pyplot as plt

# Constants
s3_cost_per_gb = 0.022  # USD per GB
downloads_per_hour_per_user_gb = 0.2  # GB per hour per user, example value assuming a lot of images as opposed to videos, etc.
hours_per_week_per_user = 4
openai_fast_cost_per_message = 0.0067  # USD
openai_smart_cost_per_message = 0.0667  # USD
messages_per_hour_per_user = 5  # assuming 1 message every 12 minutes, this is a generous assumption
ec2_cost_per_user_per_hour = 0.01  # USD per hour, example value
openai_smart_ratio = 0.05 # the ratio of smart messages to fast messages

users_refined = 100  # Example value of starting with 100 users
growth_rate_refined = (200000 / users_refined) ** (1 / 24)  # Example value getting 200k users in 2 years assuming exponential growth
# Assumptions for cost reductions
s3_cost_reduction = 0.20 + 0.20 + 0.05  # Media Compression and more device-cache, CDN when more people on app, Monitoring

# OpenAI cost reduction assumes we cut free model from 3rd party and build our own, in the next 2 months or so. 100x cheaper.
# Premium messages are 10x more expensive than fast messages, so we can reduce cost by 10% by using smaller context window, etc.
openai_cost_reduction = 0.1  # Optimize API Calls & Build In-House Models, the 0.1 is 
ec2_cost_reduction = 0.15 + 0.20 + 0.10  # CDN, Server Optimization, Reserved Instances

# Costs over time with optimizations
total_costs_optimized = []
breakdown_openai_optimized = []
breakdown_s3_optimized = []
breakdown_ec2_optimized = []


# Calculate costs for 24 months with more exponential growth
users_optimized = 100 # saying we start with 100 users
print("starting loop")
for month in range(24):
    # S3 cost based on total download, with optimizations
    total_download_gb = users_optimized * downloads_per_hour_per_user_gb * hours_per_week_per_user   # Smaller bandwidth
    s3_cost_per_user = s3_cost_per_gb * downloads_per_hour_per_user_gb  * (1 - s3_cost_reduction)
    
    # OpenAI cost per user per hour, with optimizations
    openai_cost_per_user_per_hour = (
        openai_fast_cost_per_message * (1 - openai_smart_ratio)
        + openai_smart_cost_per_message * openai_smart_ratio
    ) * messages_per_hour_per_user * (1 - openai_cost_reduction)
    
    # Total cost per user per week, with optimizations
    total_cost_per_user_per_week = (
        hours_per_week_per_user
        * (openai_cost_per_user_per_hour + s3_cost_per_user + ec2_cost_per_user_per_hour * (1 - ec2_cost_reduction))
    )
    
    # Total cost per week
    total_cost_per_week = total_cost_per_user_per_week * users_optimized
    
    total_costs_optimized.append(total_cost_per_week * 4.33) # 4.33 weeks per month

    # Breakdown of expenses
    breakdown_openai_optimized.append(openai_cost_per_user_per_hour * users_optimized * hours_per_week_per_user)
    breakdown_s3_optimized.append(s3_cost_per_user * users_optimized * hours_per_week_per_user)
    breakdown_ec2_optimized.append(ec2_cost_per_user_per_hour * users_optimized * hours_per_week_per_user / 2 * (1 - ec2_cost_reduction))
    
    # Exponential user growth
    users_optimized *= growth_rate_refined

print("finished loop with this many users: " + str(users_optimized))

# Total cost after 2 years (Optimized)
total_cost_2_years_optimized = sum(total_costs_optimized) + 20000 # Assuming a 20,000 cushion
print("Total Cost Over 2 Years (Optimized): $" + str(total_cost_2_years_optimized))
print('Total Cost Over 2 Years (Optimized): $' + str(total_cost_2_years_optimized))
print('Total Breakdown OpenAI Optimized: $' + str(breakdown_openai_optimized))
print('Total Breakdown S3 Optimized: $' + str(breakdown_s3_optimized))
print('Total Breakdown EC2 Optimized: $' + str(breakdown_ec2_optimized))

# Breakdown of expenses
total_breakdown_openai_optimized = sum(breakdown_openai_optimized)
total_breakdown_s3_optimized = sum(breakdown_s3_optimized)
total_breakdown_ec2_optimized = sum(breakdown_ec2_optimized)
total_cost_2_years_optimized, total_breakdown_openai_optimized, total_breakdown_s3_optimized, total_breakdown_ec2_optimized



# Plotting Total Cost Over Time (Optimized)
plt.figure(figsize=[10, 6])
plt.plot(total_costs_optimized, label='Approximate Cost/Month Over Time (Optimized)')
plt.title('Total Hosting Cost Over 2 Years ~$499,202.34')
plt.xlabel('Months')
plt.ylabel('Cost/month (USD)')
plt.grid(True)
plt.legend()
plt.show()

