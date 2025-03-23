import seaborn as sns
import matplotlib.pyplot as plt

# Generate and save visualization 1: Average Scores per Subject
plt.figure(figsize=(10, 6))
sns.barplot(x='Subject', y='Average_Score', data=subject_avg, palette='coolwarm')
plt.title('Average Score per Subject')
plt.xticks(rotation=45)
avg_score_chart = '/mnt/data/Average_Score_Per_Subject.png'
plt.tight_layout()
plt.savefig(avg_score_chart)
plt.close()

# Generate and save visualization 2: Heatmap of sample student scores
plt.figure(figsize=(14, 8))
sample_data = df.set_index('Student_ID').iloc[:20]
sns.heatmap(sample_data, annot=True, cmap='YlGnBu')
plt.title('Heatmap - Sample Student Scores')
heatmap_chart = '/mnt/data/Heatmap_Sample_Students.png'
plt.tight_layout()
plt.savefig(heatmap_chart)
plt.close()

# Generate and save visualization 3: Boxplot for score distribution
plt.figure(figsize=(14, 8))
melted_df = df.melt(id_vars='Student_ID', var_name='Subject', value_name='Score')
sns.boxplot(x='Subject', y='Score', data=melted_df, palette='Set3')
plt.xticks(rotation=45)
plt.title('Score Distribution per Subject')
boxplot_chart = '/mnt/data/Boxplot_Score_Distribution.png'
plt.tight_layout()
plt.savefig(boxplot_chart)
plt.close()

avg_score_chart, heatmap_chart, boxplot_chart
