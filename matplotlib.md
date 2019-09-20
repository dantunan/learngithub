matplotlib 用法
--

- 基本使用
```
import matplotlib as plt
plt.plot([1,2,3,4])
plt.ylable('some numbers')
plt.show()
``` 
<br/>

- `plt.axis` 可以用于设置x轴和y轴
```python
plt.plot([1,2,3,4], [4,5,6,7], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```
<br/>

- plt经常和numpy共同使用
```python
import numpy as np
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```
![结果图](https://matplotlib.org/_images/sphx_glr_pyplot_004.png)

<br/>  

- 画分类图
```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
```
![](https://matplotlib.org/_images/sphx_glr_pyplot_006.png)

<br/>  

- 使用axes和Line2D画图
```python
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
x = np.arange(0,5, 0.02)
y = np.exp(-x) * np.cos(2*np.pi*x)
fig = plt.figure()
axes = fig.add_subplot(1,1,1)
line = Line2D(x,y, linewidth=2)
axes.add_line(line)
axes.set_xlim(np.min(x), np.max(x))
axes.set_ylim(np.min(y), np.max(y))
axes.set_xlabel('x label')
axes.set_ylabel('y label')
plt.show()
```

- `plt.setp()`可以用于设置line的属性
```python
line = Line2D(x, y)
plt.setp(line, linewidth=2, color='r')
```

- Line2D的属性

|property|Value Type|
|:---|:---:|
|linestyle or ls| '-', '--', '-.' |
|linewidth or lw| float value in points|
|xdata| np.array|
|ydata| np.array|
|animated | True or Falser|  
可以用plt.setp(line)查各种属性, `clf()`和`cla()`可以清除当前figure和axes

- `text()`用于在图中放置文本
```python
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```
![](https://matplotlib.org/_images/sphx_glr_pyplot_008.png)

<br/>

- `annotate()`可以更方便的放置注释
```python
ax = plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()
```
![](https://matplotlib.org/_images/sphx_glr_pyplot_009.png)

<br/>

- `plt.xscale('log')`和`plt.yscale('linear')`可以设置x轴和y轴的尺度
```python
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)
plt.show()
```
![](https://matplotlib.org/_images/sphx_glr_pyplot_010.png)