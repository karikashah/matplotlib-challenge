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
print(average_fare)
average_fare = pdk.DataFrame(average_fare).reset_index()
print("---------------------------------------------")
print(average_fare)
##average_fare = average_fare.rename(columns = {'fare': 'avg_fare'})
# x-axis: Total Number of Rides Per City
# total_rides = combined_data.groupby("city")["ride_id"].count()
# total_rides = pd.DataFrame(total_rides).reset_index()
# total_rides = total_rides.rename(columns = {'ride_id': 'total_rides'})
# #Total Drivers
# total_drivers = combined_data[["city", "driver_count"]].drop_duplicates("city")
# #City Type
# city_type = combined_data[["city", "type"]].drop_duplicates("city")
# final_df = pd.merge(pd.merge(pd.merge(average_fare, total_rides, on="city"), 
#                              total_drivers, on="city"), city_type, on="city")
# Build the scatter plots for each city types

# Incorporate the other graph properties

# Create a legend

# Incorporate a text label regarding circle size

# Save Figure

