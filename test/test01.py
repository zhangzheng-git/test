# import utils
# print(__name__)
# print(utils.chengfa(1,3,2))
#
# from utils import jianfa,chengfa  #推荐使用该方式
# print(jianfa(1,2,3,4))
#
# if __name__ == '__main__':
#     print(jianfa(1,2,2))

import utils.tool.utils #导入模块的命名空间

print(utils.tool.utils.jianfa(1,2,4))

import utils.tool.utils as ut

print(ut.jianfa(1,2,4))

#from utils.tool.utils import * #导入整个模块的全部方法，浪费内存

from utils.tool.utils import jianfa,chengfa
jianfa(1,2,4)

from utils.tool.utils import jianfa as jf
jf(1,2,4)


def fuc(var):
    if not var:
        print(var)
    else:
        print("var{}".format(var))

if __name__ == '__main__':
    fuc([1])