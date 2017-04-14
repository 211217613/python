from __future__ import print_function, division

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
#  Ref: https://www.oreilly.com/learning/data-visualization-with-seaborn

x = np.linspace(0,10,1000)
#plt.plot(x, np.sin(x), x, np.cos(x))



sns.set()

data = np.random.multivariate_normal([0,0],[[5,2],[2,2]], size=2000 )
data = pd.DataFrame(data, columns=['x', 'y'])
for col in 'xy':
	plt.hist(data[col], normed=True, alpha=0.5)
for col in 'xy':
	sns.kdeplot(data[col], shade=True)
sns.kdeplot(data);

plt.show()
