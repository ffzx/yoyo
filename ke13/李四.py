"""
模块导入：记住一点
从项目根目录（pycharm一定打开项目根目录)，第一层开始导入
"""
from ke13.张三 import func
import ke13
"""
每个py 都有一个__name__  "__main__"
"""

print(ke13.张三.__name__)

print(__name__)   # __main__ 它自己
