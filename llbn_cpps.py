### Map of llbn cppsand gems locations

# Loading the packages
import geopandas as gpd
import folium
import matplotlib.pyplot as plt

# Loading the shapefiles
llbn_cpps_gems = gpd.read_file(r"D:\Natural State\Carbon\cpp_demo\cpps_gems\cpp_gems.shp")
study_extent = gpd.read_file(r"D:\Natural State\Carbon\study_extent\total_carbon_extent.shp")

# use the same coordinate system
llbn_cpps_gems = llbn_cpps_gems.to_crs(study_extent.crs)

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(12, 10))

# Plot study extent as background
study_extent.plot(ax=ax, color="lightgrey", edgecolor="black", linewidth=1, label="Study Extent")

# Plot cpp_gems on top
llbn_cpps_gems.plot(ax=ax, color="green", edgecolor="darkgreen", linewidth=0.5, alpha=0.7, label="CPP Gems")

# Add title and labels
ax.set_title("LLBN CPPs and Gems Locations", fontsize=16, fontweight="bold")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend()

# Save and show the map
plt.tight_layout()
plt.savefig("llbn_cpps_map.png", dpi=300)
plt.show()

