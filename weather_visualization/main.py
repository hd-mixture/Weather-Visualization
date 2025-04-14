import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Read weather data
data = pd.read_csv('weather_data.csv')

# Set up the figure and subplots grid
plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 2)
plt.suptitle('📊 Weekly Weather Data Visualization', fontsize=18, fontweight='bold', color='#2c3e50')

# Line Plot - Temperature
ax1 = plt.subplot(gs[0, 0])
ax1.plot(data['Day'], data['Temperature'], marker='o', linestyle='-', color='#3498db', linewidth=2, markersize=8, markerfacecolor='white')
ax1.set_title('🌡️ Temperature Over the Week', fontsize=14, fontweight='bold')
ax1.set_xlabel('Day')
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_facecolor('#f4f6f7')

# Bar Chart - Humidity
ax2 = plt.subplot(gs[0, 1])
ax2.bar(data['Day'], data['Humidity'], color='#f39c12', edgecolor='black')
ax2.set_title('💧 Humidity Levels', fontsize=14, fontweight='bold')
ax2.set_xlabel('Day')
ax2.set_ylabel('Humidity (%)')
ax2.set_facecolor('#f4f6f7')

# Scatter Plot - Rainfall vs Temperature
ax3 = plt.subplot(gs[1, 0])
ax3.scatter(data['Temperature'], data['Rainfall'], color='#2ecc71', edgecolor='black', s=100)
ax3.set_title('☔ Rainfall vs Temperature', fontsize=14, fontweight='bold')
ax3.set_xlabel('Temperature (°C)')
ax3.set_ylabel('Rainfall (mm)')
ax3.grid(True, linestyle='--', alpha=0.5)
ax3.set_facecolor('#f4f6f7')

# Pie Chart - Rainfall Distribution (Improved)
ax4 = plt.subplot(gs[1, 1])

explode = [0.06] * len(data['Rainfall'])  # Explode slices
colors = plt.cm.Set3(range(len(data['Rainfall'])))  # Nice color palette

wedges, texts, autotexts = ax4.pie(
    data['Rainfall'],
    labels=data['Day'],
    autopct='%1.1f%%',
    explode=explode,
    shadow=True,
    colors=colors,
    startangle=100,
    pctdistance=0.85,
    labeldistance=1.2,
    textprops={'fontsize': 9}
)

# Beautify labels
for text in texts:
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(8)

# Add donut hole
centre_circle = plt.Circle((0, 0), 0.65, fc='white')
ax4.add_artist(centre_circle)

ax4.set_title('📈 Rainfall Distribution', fontsize=14, fontweight='bold')

# Final layout
plt.tight_layout(rect=[0, 0.03, 1, 0.100])
plt.show()