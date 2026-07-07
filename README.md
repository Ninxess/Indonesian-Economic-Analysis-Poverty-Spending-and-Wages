 Indonesian-Economic-Analysis-Poverty-Spending-and-Wages
My first project. This project analyzes the relationship between Poverty Line, Per Capita Spending, Provincial Minimum Wage (UMP), and Hourly Wages across Indonesia using publicly available data from kaggle :"https://www.kaggle.com/datasets/rezkyyayang/pekerja-sejahtera/data"
 📂 Data Sources
- gk.df.csv  : Per Capita Poverty Line 
- peng.df.csv: Average Per Capita Spending 
- ump.df.csv : Provincial Minimum Wage 
- upah.df.csv: Average Hourly Worker Wage 

 ⚙️ Analysis Process
1. Data Cleaning: Merged 4 separate datasets.
2. Aggregation: Grouped data by province and year using `.groupby().mean()` to standardize granularity.
3. Correlation Analysis: Calculated a correlation matrix to examine the strength of relationships between variables.
4. Visualization : Generated a heatmap and scatter plot to present findings clearly.



 Correlation Heatmap
<img width="1000" height="600" alt="Heatmap" src="https://github.com/user-attachments/assets/9a5bd78a-475a-4d09-ad68-0ed9c10074b6" />


 Scatter Plot: Spending vs Poverty Line
<img width="800" height="600" alt="Scatterplot" src="https://github.com/user-attachments/assets/6516d5a1-b972-4eba-ae80-c4dc5465a698" />


 💡 Key Takeaways
1. Strongest correlation (0.80): Per Capita Spending** and Hourly Wage. This suggests that provinces with higher spending levels also tend to have higher worker wages.
2. Lowest correlation (0.63): Poverty Line and Provincial Minimum Wage (UMP). While still a moderate-strong positive relationship, it is the weakest among the variables.
3. Important Note: Correlation does not imply causation. Further regression analysis is needed to explore causal relationships.
 🛠️ Technologies Used
- Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy)

 📝 About Me
This is my first project yet, completed before my first day of college. I will be starting in August majoring in Data Science
