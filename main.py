import pandas as pd

data = {
    'Name': ['Emily', 'Liam', 'Sophia', 'Jackson', 'Olivia', 'John', 'Anna', 'William', 'Mia', 'Benjamin'],
    'Age': [25, 32, 18, 40, 29, 50, 22, 36, 27, 45],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Score': [78, 92, 63, 85, 71, 96, 54, 89, 77, 68]
}
df = pd.DataFrame(data) # Створення DataFrame

print(df) # Початковий

print(df[:5]) # Перші 5

print(df['Age'].mean()) # Середній вік

filter_by_score = df[df['Score'] > 80] # Оцінка вище 80

df.loc[df['Name'] == 'Anna', 'Score'] = 95 # Оцінка Anna = 95

age_series = pd.Series(df['Age'], name='ages') # Series ages

print(df['Age'].max()) # Максимальний вік

df = df.drop(df[df['Name'] == 'John'].index) # Видалення рядка з іменем John

df.to_csv('main.csv') # Збереження у csv