# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pdk

# Specify path to files
city_data_csv = "./data/city_data.csv"
ride_data_csv = "./data/ride_data.csv"

# read the data from the files into resp dataframes
city_data = pdk.read_csv(city_data_csv, low_memory=False)
ride_data = pdk.read_csv(ride_data_csv, low_memory=False)

# merge both dataframes on city column, & how='left' is to match the screenshot as mentioned in problem stmt 
ride_city_merge = pdk.merge(ride_data, city_data, on="city", how="left")
print(ride_city_merge.head(5))

# -----------------Bubble Plot of Ride Sharing Data----------------------------------------------------------------
# Obtain the x and y coordinates for each of the three city types
# y-axis: Average Fare Per City
average_fare = ride_city_merge.groupby("city")["fare"].mean()
average_fare_df = pdk.DataFrame(average_fare).reset_index()
average_fare_df = average_fare_df.rename(columns = {'fare': 'avg_fare'})

# x-axis: Total Number of Rides Per City
total_rides = ride_city_merge.groupby("city")["ride_id"].count()
total_rides_df = pdk.DataFrame(total_rides).reset_index()
total_rides_df = total_rides_df.rename(columns = {'ride_id': 'total_rides'})

# calculate total Drivers
total_drivers = ride_city_merge[["city", "driver_count"]].drop_duplicates("city")
# get city Type
city_type = ride_city_merge[["city", "type"]].drop_duplicates("city")

final_df = pdk.merge(pdk.merge(pdk.merge(average_fare_df, total_rides_df, on="city"), 
                             total_drivers, on="city"), city_type, on="city")

# Build the scatter plots for each city types
urban_group = final_df.loc[final_df['type'] == 'Urban']
suburban_group = final_df.loc[final_df['type'] == 'Suburban']
rural_group = final_df.loc[final_df['type'] == 'Rural']

# Incorporate the other graph properties
ax1 = urban_group.plot(kind='scatter',x='total_rides', y='avg_fare',
                       color='lightcoral', s=final_df['driver_count']*5, label = 'Urban', 
                       alpha = 0.5, edgecolor = "black", linewidths = 1)    
ax2 = suburban_group.plot(kind='scatter', x='total_rides', y='avg_fare', 
                          color='lightskyblue',s=final_df['driver_count']*5, label = 'Suburban', 
                          alpha = 0.5, edgecolor = "black", linewidths = 1, ax=ax1)    
ax3 = rural_group.plot(kind='scatter', x='total_rides', y='avg_fare', 
                       color='gold', s=final_df['driver_count']*5, label = 'Rural', 
                       alpha = 0.5, edgecolor = "black", linewidths = 1, ax=ax1)
plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare ($)")

# Incorporate a text label regarding circle size  
textstr = 'Note:\nCircle size correlates with driver count per city.'
plt.xlim(0, 42)
plt.ylim(19, 45)
print(textstr)
plt.text(43, 32, textstr, fontsize=10)
plt.subplots_adjust(right=0.55)

# Create a legend
plt.legend(title = 'City Types')
plt.grid(True)
# Save Figure
plt.savefig("./data/Bubble_01_ride_share.png")
plt.show()