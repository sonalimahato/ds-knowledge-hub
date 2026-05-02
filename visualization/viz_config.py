import matplotlib.pyplot as plt
import seaborn as sns

def set_aesthetic_style():
    # Setting up a minimalist white grid style
    sns.set_theme(style="whitegrid", palette="muted")
    
    # Customizing fonts and spine (edges)
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    
    print("Aesthetic style applied! ✨")


A. Distribution Plot (Histogram + KDE)
Data ki density aur spread dikhane ke liye best hai.

plt.figure(figsize=(10, 6))
sns.histplot(df['column_name'], kde=True, color='#7C3AED', bins=30)
plt.title('Distribution Analysis', fontsize=15, pad=20)
plt.show()


B. Correlation Heatmap (The Pro Look)
Variables ke beech ka rishta dikhane ke liye. Isme mask feature use karein taaki sirf niche ka half dikhe (cleaner look).

corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool)) # To hide the upper triangle

plt.figure(figsize=(12, 8))
sns.heatmap(corr, mask=mask, annot=True, cmap='Purples', fmt=".2f")
plt.title('Feature Correlation Matrix', fontsize=15)

C. Categorical Comparison (Box Plot)
Outliers aur medians dekhne ke liye best hai.

plt.figure(figsize=(10, 6))
sns.boxplot(x='category', y='value', data=df, palette='viridis')
plt.xticks(rotation=45)
