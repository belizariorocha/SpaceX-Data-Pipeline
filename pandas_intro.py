import pandas as pd

data = {
    'rocket': [
        'Falcon 1',
        'Falcon 9',
        'Falcon Heavy',
    ],
    'launches': [5, 100, 3],
}

df = pd.DataFrame(data)
print(df)

print(df['rocket'])

df_5launches = df[df['launches'] > 5]

df['success_rate'] = [0.4, 0.98, 1.0]
