import pandas as pd
import numpy as np

# Load data from source
df = pd.read_csv(r'H:\TP\Email final\TP_Dataset.csv')

# 1. declare Ranges and labels
# <5, 5-9 , and >= 10
data_Range = [-np.inf, 4, 9, np.inf]
lbl_Experience = ['Junior', 'Mid', 'Senior']

# 2. Categorize employees into experience levels
df['Experience Level'] = pd.cut(df['TotalWorkingYears'], bins=data_Range, labels=lbl_Experience)

# 3. Create the summary table
tbl_summary = df['Experience Level'].value_counts().reset_index()
tbl_summary.columns = ['Experience Level', 'Employee Count']

tbl_summary.index = tbl_summary.index + 1

# Display summary table
print(tbl_summary)
