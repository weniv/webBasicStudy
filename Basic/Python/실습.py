import matplotlib.pyplot as plt

# line
x = [100, 200, 300]
y = [10, 20, 30]

plt.plot(x, y)

# pie
labels = ['one', 'two', 'three']
size = [100, 20, 10]

plt.pie(size, labels=labels, shadow=True, autopct='%1.3f%%')
plt.show()

# bar
x = ['one', 'two', 'three']
y = [100, 20, 10]
plt.bar(x, y)
plt.show()

# 크롤링
import pandas as pd

tables = pd.read_html('https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%9D%B8%EA%B5%AC')

tables[0]
tables[4]
tables[4]['사망자수(명)']
tables[4]['사망자수(명)'].sum()
