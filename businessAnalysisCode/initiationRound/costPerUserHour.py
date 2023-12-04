# mapping out negative trajectory of cost per user hour
import numpy as np
import matplotlib.pyplot as plt

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

# Calculate costs for 24 months with exponential growth
users_optimized = users_refined
for month in range(24):
    # S3 cost per user, with optimizations
    s3_cost_per_user = s3_cost_per_gb * downloads_per_hour_per_user_gb * (1 - s3_cost_reduction)
    
    # OpenAI cost per user per hour, with optimizations
    openai_cost_per_user_per_hour = (
        openai_fast_cost_per_message * (1 - openai_smart_ratio)
        + openai_smart_cost_per_message * openai_smart_ratio
    ) * messages_per_hour_per_user * (1 - openai_cost_reduction)
    
    # EC2 cost per user per hour, with optimizations
    ec2_cost_per_user_per_hour_with_reduction = ec2_cost_per_user_per_hour * (1 - ec2_cost_reduction)
    
    # Total cost per user per week
    total_cost_per_user_per_week = (
        hours_per_week_per_user
        * (openai_cost_per_user_per_hour + s3_cost_per_user + ec2_cost_per_user_per_hour_with_reduction)
    )
    
    # Total cost per week
    total_cost_per_week = total_cost_per_user_per_week * users_optimized
    
    total_costs_optimized.append(total_cost_per_week * 4)
    
    # Exponential user growth
    users_optimized *= growth_rate_refined

# Calculating the cost per user per hour over time
cost_per_user_per_hour = [total_cost / (users_refined * growth_rate_refined ** month * hours_per_week_per_user * 4) for month, total_cost in enumerate(total_costs_optimized)]

# Adjusting the starting value and the exponential decrease factor

# Adjusting the starting value b/c much of the big cost reductions happen in the first few months (e.g. model compression, media compression, etc.) 
# This may prove to be naive, as deployment of in-house models may take longer than 2 months, but we can adjust this later.
start_value = max(cost_per_user_per_hour) + 0.3
decrease_factor = 0.92  # 8% decrease per month

# Applying exponential decrease
cost_per_user_per_hour_adjusted = [start_value * decrease_factor**month for month in range(24)]

# Plotting the cost per user per hour over time
plt.figure(figsize=[10, 6])
plt.plot(cost_per_user_per_hour_adjusted, label='Approximate Cost/User/Hour Over Time (Optimized)')
plt.title('Driving Down Cost per User per Hour Over 2 Years')
plt.xlabel('Months')
plt.ylabel('Cost/user/hour (USD)')
plt.grid(True)
plt.legend()
plt.show()
