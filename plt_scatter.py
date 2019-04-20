import matplotlib.pyplot as plt
import numpy as np

savings = [18.54, 48.64, 34.30, 24.03, 26.18, 20.45, 11.56, 24.318]
investment = [20.414, 47.251, 34.024, 23.19, 19.512, 22.287, 16.244, 48.646]
names = ['USA', 'China', 'India', 'Japan', 'Germany', 'France', 'UK', 'Bhutan']

fig, ax = plt.subplots()
ax.scatter(savings, investment)

for i, txt in enumerate(names):
	ax.annotate(txt, (savings[i], investment[i]), textcoords='offset pixels', xytext=(5, 5))


x = np.linspace(10, 60,  1000)
ax.plot(x, x, color='red', linestyle='--')
plt.xlabel('Gross savings (% of GDP) in 2013')
plt.ylabel('Total investment (% of GDP) in 2013')
plt.savefig('Q4_plot.eps', format='eps', dpi=1000)

