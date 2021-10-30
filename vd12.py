import pandas as pd

s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
     'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
     'ba': pd.Series([9., -1.3, 3.5, 41.1], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(s)

# thêm cột bốn với giá trị mỗi ô theo công thức
df['bốn'] = df['hai'] - df['ba']

# thêm cột với giá trị vô hướng (scalar value)
df['Chuẩn'] = 'OK'

# thêm cột không cùng số lượng index với DataFrame
df['Khác'] = df['hai'][:3]

# thêm cột True/False theo điều kiện
df['KT'] = df['một'] == 3.0

# dùng hàm insert. Cột "chèn" bên dưới sẽ ở vị trí 2 (tính từ 0), có giá trị bằng cột một
df.insert(2, 'chèn', df['một'])

print(df)