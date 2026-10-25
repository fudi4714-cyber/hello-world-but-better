#!/usr/bin/env python3
"""一个会打印惊喜的脚本。"""

import random

SURPRISES = [
    "你打开了这个文件，说明你真的点进来了。",
    "Git 不只是存代码的地方，它是时间机器。",
    "这个仓库从零开始，就像所有伟大的项目一样。",
    "404: 惊喜未找到。开玩笑的，它就在这里。",
    "你现在运行的这段代码，是 AI 写的。",
]

def main():
    print(random.choice(SURPRISES))
    print("\n顺便说一句：你的 GitHub 账号现在有内容了。")

if __name__ == "__main__":
    main()