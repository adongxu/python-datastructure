import sys
from collections import OrderedDict
import json
# cloudml models create -n abc  --version=1 -a " -n 15 " -c 1
# {
#   "cmd" : "cloudml",
#   "subcmd1" : "models",
#   "subcmd2" : "create",
#   "parameters" : {
#     "-n" : "abc",
#     "--version" : "1",
#     "-a" : "-n 15",
#     "-c" : "1"
#   }
# }

# run: python cmd2json.py cloudml models create -n abc  --version=1 -a " -n 15 " -c 1

# 格式化后的字典 参数字典
dic = OrderedDict()
params = OrderedDict()
# 命令与参数的分割点
break_point = 0
# 命令行字符串 没有处理 ‘-n 15’
cmd_ls= sys.argv[1:]
# cmd_ls= "cloudml models create -n  abc --version=1 -a ' -n 15 ' -c 1".split()
# =========================对带引号参数进行处理=================================
if "'" in cmd_ls:
    # 记录''的位置
    mark = []
    for i in range(len(cmd_ls)):
        if cmd_ls[i] == "'":
            mark.append(i)
    # mark中两两配对找到's'中的s
    new_ls = cmd_ls[:mark[0]]
    for i in range(len(mark)):
        # 只处理左边的
        if i % 2 == 0:
            new_ls.append(' '.join(cmd_ls[mark[i]+1:mark[i+1]]))
            # 如果不是最后一对，继续追加引号中间的部分
            if i + 1 != len(mark) - 1:
                new_ls.extend(cmd_ls[mark[i+1]+1:mark[i+2]])
            else:
                new_ls.extend(cmd_ls[mark[i+1]+1:])

    cmd_ls = new_ls
# =========================处理各种边界情况=================================
length = len(cmd_ls)
# 无参数或者第一个参数不是命令
if length == 0 or cmd_ls[0].startswith('-'):
    raise ValueError('输入非法~')
# 找分割点（如果没有，就是最后一个，且命令不包含参数）
for i in range(length):
    if cmd_ls[i].startswith('-') or i == length-1:
        break_point = i
        break
# 以分割点为届，左边是命令，右边是参数
dic['cmd'] = cmd_ls[0]
if break_point == 0:
    pass
else:
    cur = 1
    # subcmd
    while cur < break_point:
        dic['subcmd%d'%cur] = cmd_ls[cur]
        cur += 1
    # params
    while cur >= break_point and cur < length:
        # 有=从该字符中抽取参数，否则偶从下一个字符抽取参数
        if '=' in cmd_ls[cur]:
            key, value = cmd_ls[cur].split('=')[0], cmd_ls[cur].split('=')[1]
            params[key] = value
        elif cmd_ls[cur].startswith('-'):
            params[cmd_ls[cur]] = cmd_ls[cur+1]
            cur += 1
        cur += 1
dic['parameters'] = params
# print(dic)
print(json.dumps(dic, indent=4))

