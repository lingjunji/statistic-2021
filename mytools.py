import pandas as pd
from yreadstat import pyreadstat 
plt.rcParams["font.sans-serief"] = ["simHei"] # 设置字体


def 有序变量描述统计表( 表名，变量名):
     result = 表名[变量名].value_counts(sort=False)
     描述统计表 = pd.DataFrame(result)
     描述统计表['比例'] = 描述统计表['count'] / 描述统计表['count'].sum()
     描述统计表['累计比例'] = 描述统计表['比例'].cumsum()
     return 描述统计表


def 绘制直方图(表名):
     x = 表名.index 
     y = 表名['count'].values
     fig,ax2 = plt.subplots
     ax2.bar(x,y)
     plt.show()
