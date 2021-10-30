import pandas as pd

# tạo dict từ các series
s = {'một': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
     'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

# tại DataFrame từ dict
df = pd.DataFrame(s)

print(df)