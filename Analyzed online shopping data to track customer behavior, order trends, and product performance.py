# Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/Users/srirakeshnagasai/Downloads/project-1/E_Commerce_Data.csv')
df.head()
df.shape
df.info()

#Data Quality Check

df.isnull().sum()

df.duplicated().sum()

df.describe()

#Unique Value Analysis

cols = ['Product Name','Category','Region']
print("="*60)
print("Unique values in each column")
print("="*60)
for col in cols:
  print(f"{col} : {df[col].unique()}")
  print("*"*60)

region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
region

#Category-wise Profit Analysis by Region

table = pd.pivot_table(df,index='Region',columns='Category',values='Profit',aggfunc='sum')
table

#Product-wise Quantity Analysis by Region

table2 = pd.pivot_table(df,index='Region',columns='Product Name',values='Quantity',aggfunc='sum')
table2

table3 = pd.pivot_table(df,index='Region',columns='Category',values='Quantity',aggfunc='sum')
table3

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

month = df.groupby('Month')['Profit'].sum().sort_values(ascending=False)
month

product_category = df.groupby(['Product Name','Category'])['Quantity'].sum().sort_values(ascending=False)
product_category

p = df.groupby('Category')['Product Name'].describe()
p

#Data Visualization

num_cols = ['Profit','Quantity','Sales','Month','Year']
plt.figure(figsize=(15,8))

for i, col in enumerate(num_cols, 1):
    plt.subplot(2, 3, i)

    if col == 'Profit':
        color = PRIMARY
    elif col == 'Quantity':
        color = SUCCESS
    elif col == 'Sales':
        color = WARNING
    elif col == 'Month':
        color = PURPLE
    else:
        color = TEAL

    sns.histplot(df[col], kde=True, color=color, alpha=0.6, edgecolor='white')
    plt.title(f'Distribution of {col}', fontsize=14, fontweight='bold', color=DARK_TEXT)
    plt.xlabel(col, color=MID_TEXT)
    plt.ylabel('Frequency', color=MID_TEXT)


plt.subplot(2, 3, 6).set_visible(False)

plt.tight_layout()
plt.show()

cat_cols = ['Region', 'Category', 'Product Name']
plt.figure(figsize=(18, 6))

for i, col in enumerate(cat_cols, 1):
    plt.subplot(1, 3, i)

    values = df[col].value_counts().values
    labels = df[col].value_counts().index

    # Assign colors based on column
    if col == 'Region':
        colors = [PRIMARY, SUCCESS, WARNING, PURPLE]  # North, East, South, West
    elif col == 'Category':
        colors = [PRIMARY, PURPLE, TEAL]  # Electronics, Accessories, Office
    else:
        colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(labels)))

    wedges, texts, autotexts = plt.pie(values,
                                        labels=labels,
                                        autopct='%1.1f%%',
                                        colors=colors,
                                        startangle=90,
                                        wedgeprops={'edgecolor': 'white', 'linewidth': 2},
                                        textprops={'fontsize': 11})

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)

    for text in texts:
        text.set_fontsize(11)
        text.set_color(DARK_TEXT)

    plt.title(f'Distribution of {col}', fontsize=16, fontweight='bold', color=DARK_TEXT, pad=20)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))


ax = sns.barplot(x=region.index,
                 y=region.values,
                 palette=REGION_COLORS,
                 edgecolor='white',
                 linewidth=1.5,
                 saturation=0.9)


for container in ax.containers:
    ax.bar_label(container,
                 fmt='₹%.0f',  # Format as currency
                 fontsize=12,
                 fontweight='bold',
                 color=DARK_TEXT,
                 padding=3)


plt.title('Profit by Region', fontsize=18, fontweight='bold', color=DARK_TEXT, pad=20)
plt.xlabel('Region', fontsize=14, color=MID_TEXT, labelpad=10)
plt.ylabel('Total Profit (₹)', fontsize=14, color=MID_TEXT, labelpad=10)
plt.xticks(rotation=30, fontsize=12, color=MID_TEXT)
plt.yticks(fontsize=12, color=MID_TEXT)
plt.grid(axis='y', alpha=0.3, linestyle='--', color=LIGHT_TEXT)
sns.despine()
plt.tight_layout()
plt.show()

CATEGORY_COLORS = ['#2563eb', '#9333ea', '#0d9488']  # Electronics, Accessories, Office


table.plot(kind='bar', stacked=True, color=CATEGORY_COLORS,
           edgecolor='white',
           linewidth=1,)
plt.title("Stacked Profit by Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.legend(loc='upper center')
plt.show()

plt.figure(figsize=(15, 6))

colors = plt.cm.viridis(np.linspace(0, 1, len(table2.columns)))

ax = table2.plot(kind='bar',
                 figsize=(15, 6),
                 color=colors,
                 edgecolor='white',
                 linewidth=1,
                 width=0.8,
                 alpha=0.9)

plt.title('Product Quantity by Region', fontsize=18, fontweight='bold', color=DARK_TEXT, pad=20)
plt.ylabel('Total Quantity', fontsize=14, color=MID_TEXT, labelpad=10)
plt.xlabel('Region', fontsize=14, color=MID_TEXT, labelpad=10)

plt.xticks(rotation=45, fontsize=12, color=MID_TEXT)
plt.yticks(fontsize=12, color=MID_TEXT)
plt.legend(loc='upper center',
          bbox_to_anchor=(0.5, 1.15),
          ncol=5,
          title='Product Name',
          title_fontsize=12,
          fontsize=10,
          frameon=True,
          facecolor='white',
          edgecolor=LIGHT_TEXT,
          shadow=False)
plt.grid(axis='y', alpha=0.3, linestyle='--', color=LIGHT_TEXT)
sns.despine()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

ax = table3.plot(kind='bar',
                 stacked=True,
                 color=[PRIMARY, PURPLE, TEAL],  # Electronics, Accessories, Office
                 edgecolor='white',
                 linewidth=1.5,
                 figsize=(12, 7),
                 alpha=0.9)

plt.title('Category Quantity by Region', fontsize=18, fontweight='bold', color=DARK_TEXT, pad=20)
plt.ylabel('Total Quantity', fontsize=14, color=MID_TEXT, labelpad=10)
plt.xlabel('Region', fontsize=14, color=MID_TEXT, labelpad=10)

plt.xticks(rotation=45, fontsize=12, color=MID_TEXT)
plt.yticks(fontsize=12, color=MID_TEXT)

plt.legend(loc='upper center',
          bbox_to_anchor=(0.5, 1.08),
          title='Category',
          title_fontsize=13,
          fontsize=12,
          frameon=True,
          facecolor='white',
          edgecolor=LIGHT_TEXT,
          ncol=3)

plt.grid(axis='y', alpha=0.3, linestyle='--', color=LIGHT_TEXT)
sns.despine()

for container in ax.containers:
    ax.bar_label(container,
                 label_type='center',
                 fontsize=10,
                 color='white',
                 fontweight='bold')
plt.tight_layout()
plt.show()

product_category = df.groupby(['Product Name','Category'])['Quantity'].sum().sort_values(ascending=False)
product_category_df = product_category.reset_index()
pivot_table = product_category_df.pivot(index='Product Name', columns='Category', values='Quantity')

plt.figure(figsize=(14, 7))
ax = pivot_table.head(10).plot(kind='bar',
                               figsize=(14, 7),
                               color=[PRIMARY, PURPLE, TEAL],
                               edgecolor='white',
                               linewidth=1.5,
                               width=0.8,
                               alpha=0.9)
plt.title('Top 10 Products by Category', fontsize=18, fontweight='bold', color=DARK_TEXT, pad=25)
plt.xlabel('Product Name', fontsize=14, color=MID_TEXT, labelpad=10)
plt.ylabel('Total Quantity Sold', fontsize=14, color=MID_TEXT, labelpad=10)
plt.xticks(rotation=45, fontsize=12, color=MID_TEXT, ha='right')
plt.yticks(fontsize=12, color=MID_TEXT)
plt.legend(loc='upper center',
          bbox_to_anchor=(0.5, 1.15),
          title='Category',
          title_fontsize=13,
          fontsize=12,
          frameon=True,
          facecolor='white',
          edgecolor=LIGHT_TEXT,
          ncol=3)
plt.grid(axis='y', alpha=0.3, linestyle='--', color=LIGHT_TEXT)
sns.despine()
plt.tight_layout()
plt.show()

num_cols = ['Profit', 'Quantity', 'Sales', 'Month', 'Year']
plt.figure(figsize=(15, 8))

for i, col in enumerate(num_cols, 1):
    plt.subplot(2, 3, i)
    if col == 'Profit':
        color = PRIMARY
    elif col == 'Quantity':
        color = SUCCESS
    elif col == 'Sales':
        color = WARNING
    elif col == 'Month':
        color = PURPLE
    else:  # Year
        color = TEAL

    box = sns.boxplot(data=df,
                      y=col,
                      color=color,
                      width=0.4,
                      saturation=0.8,
                      linewidth=1.5,
                      fliersize=5)

    for i, artist in enumerate(box.artists):
        artist.set_edgecolor(DARK_TEXT)
        artist.set_linewidth(1.5)

    plt.setp(box.lines, color=DARK_TEXT, linewidth=1.5)
    plt.setp(box.get_xticklabels(), fontsize=11, color=MID_TEXT)
    plt.setp(box.get_yticklabels(), fontsize=11, color=MID_TEXT)

    plt.title(f'Distribution of {col}', fontsize=14, fontweight='bold', color=DARK_TEXT, pad=10)
    plt.ylabel(col, fontsize=12, color=MID_TEXT, labelpad=5)
    plt.xlabel('')

    plt.grid(axis='y', alpha=0.3, linestyle='--', color=LIGHT_TEXT)

plt.subplot(2, 3, 6).set_visible(False)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 7))
sns.lineplot(x='Month',
             y='Profit',
             data=df,
             color=PRIMARY,
             linewidth=3,
             marker='o',
             markersize=10,
             markeredgecolor='white',
             markeredgewidth=2,
             markerfacecolor=PRIMARY,
             ci=None,
             estimator=sum)

monthly_data = df.groupby('Month')['Profit'].sum().reset_index()
plt.fill_between(monthly_data['Month'],
                 monthly_data['Profit'],
                 alpha=0.2,
                 color=PRIMARY)
plt.xlim(0.5, 12.5)
plt.ylim(100000,175000)
plt.xticks(range(1, 13),
           ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
           fontsize=12,
           color=MID_TEXT)

plt.title('Monthly Profit Trend', fontsize=18, fontweight='bold', color=DARK_TEXT, pad=20)
plt.xlabel('Month', fontsize=14, color=MID_TEXT, labelpad=10)
plt.ylabel('Total Profit (₹)', fontsize=14, color=MID_TEXT, labelpad=10)
plt.yticks(fontsize=12, color=MID_TEXT)
plt.grid(True, alpha=0.3, linestyle='--', color=LIGHT_TEXT)
for x, y in zip(monthly_data['Month'], monthly_data['Profit']):
    plt.text(x, y + 2000, f'₹{y:,.0f}',
             ha='center', va='bottom',
             fontsize=10, fontweight='bold',
             color=DARK_TEXT,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor=LIGHT_TEXT))

sns.despine()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
yearly_profit = df.groupby('Year')['Profit'].sum().reset_index()

sns.lineplot(x='Year',
             y='Profit',
             data=yearly_profit,
             color=SUCCESS,
             linewidth=3,
             marker='s',
             markersize=12,
             markeredgecolor='white',
             markeredgewidth=2.5,
             markerfacecolor=SUCCESS)

plt.fill_between(yearly_profit['Year'],
                 yearly_profit['Profit'],
                 alpha=0.2,
                 color=SUCCESS)

plt.xlim(2021.5, 2024.5)
plt.xticks([2022, 2023, 2024], fontsize=12, color=MID_TEXT)
plt.ylim(500000,700000)
plt.title('Yearly Profit Trend', fontsize=18, fontweight='bold', color=DARK_TEXT, pad=20)
plt.xlabel('Year', fontsize=14, color=MID_TEXT, labelpad=10)
plt.ylabel('Total Profit (₹)', fontsize=14, color=MID_TEXT, labelpad=10)
plt.yticks(fontsize=12, color=MID_TEXT)
plt.grid(True, alpha=0.3, linestyle='--', color=LIGHT_TEXT)

for x, y in zip(yearly_profit['Year'], yearly_profit['Profit']):
    plt.text(x, y + 5000, f'₹{y:,.0f}',
             ha='center', va='bottom',
             fontsize=12, fontweight='bold',
             color=DARK_TEXT,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9, edgecolor=LIGHT_TEXT))

sns.despine()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 8))
corr_matrix = df[['Quantity', 'Sales', 'Profit']].corr()
sns.heatmap(corr_matrix,
            annot=True,
            annot_kws={"size": 14, "fontweight": "bold", "color": "white"},
            cmap='RdBu_r',
            center=0,
            vmin=-1, vmax=1,
            square=True,
            linewidths=2,
            linecolor='white',
            cbar=True,
            cbar_kws={
                "shrink": 0.8,
                "label": "Correlation Coefficient",
                "ticks": [-1, -0.5, 0, 0.5, 1],
                "orientation": "vertical",
                "pad": 0.05
            },
            fmt='.2f',
            mask=None,
            xticklabels=True,
            yticklabels=True)

plt.title('Correlation Heatmap', fontsize=18, fontweight='bold', color=DARK_TEXT, pad=20)
plt.xticks(fontsize=12, fontweight='semibold', color=MID_TEXT, rotation=0)
plt.yticks(fontsize=12, fontweight='semibold', color=MID_TEXT, rotation=0)
for _, spine in plt.gca().spines.items():
    spine.set_visible(True)
    spine.set_color(LIGHT_TEXT)
    spine.set_linewidth(1)

plt.tight_layout()
plt.show()
