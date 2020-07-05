import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('music.csv')
x = data.drop(columns='genre')  # 输入数据性别和年龄
y = data['genre']  # 输出数据是喜欢的音乐流派

model = DecisionTreeClassifier()
model.fit(x, y)
predictions = model.predict([[21, 1], [22, 0]])  # 根据年龄和性别预测
print(predictions)