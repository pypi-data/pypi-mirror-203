# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_penguin', 'nonebot_plugin_penguin.render']

package_data = \
{'': ['*'], 'nonebot_plugin_penguin.render': ['templates/*']}

install_requires = \
['freezegun>=1.2.2,<2.0.0',
 'httpx>=0.23.3,<0.24.0',
 'nonebot-adapter-onebot>=2.2.2,<3.0.0',
 'nonebot-plugin-apscheduler>=0.2.0,<0.3.0',
 'nonebot-plugin-htmlrender>=0.2.0.3,<0.3.0.0',
 'nonebot-plugin-send-anything-anywhere>=0.2.2,<0.3.0',
 'nonebot2[fastapi]>=2.0.0rc4,<3.0.0',
 'tinydb>=4.7.1,<5.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-penguin',
    'version': '0.0.1',
    'description': 'get penguin data and send from https://penguin-stats.io/',
    'long_description': '<div align="center">\n    <a href="https://v2.nonebot.dev/store">\n        <img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">\n    </a>\n    <br>\n    <p>\n        <img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText">\n    </p>\n</div>\n\n<div align="center">\n\n# nonebot-plugin-penguin\n\n_✨ 向企鹅物流查询关卡掉落物数据 ✨_\n\n[![license](https://img.shields.io/github/license/AzideCupric/nonebot-plugin-penguin)](https://github.com/AzideCupric/nonebot-plugin-penguin/blob/main/LICENSE)\n[![action](https://img.shields.io/github/actions/workflow/status/AzideCupric/nonebot-plugin-penguin/test.yml?branch=main)](https://github.com/AzideCupric/nonebot-plugin-penguin/actions/workflows/test.yml)\n[![codecov](https://codecov.io/gh/AzideCupric/nonebot-plugin-penguin/branch/main/graph/badge.svg?token=QCFIODJOOA)](https://codecov.io/gh/AzideCupric/nonebot-plugin-penguin)\n[![python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)\n\n</div>\n\n## 📖 介绍\n\n接入企鹅物流查询明日方舟关卡掉落物信息！\n\n## 💿 安装\n\n<del>\n<details>\n<summary> \n使用 nb-cli 安装 (还没上传pypi喵)\n</summary>\n在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装\n\n    nb plugin install nonebot-plugin-penguin\n\n</details>\n</del>\n\n<details>\n<summary>使用包管理器安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令\n\n<details>\n<summary>pip</summary>\n\n    pip install git+https://github.com/AzideCupric/nonebot-plugin-penguin.git\n\n</details>\n<details>\n<summary>pdm</summary>\n\n    pdm add git+https://github.com/AzideCupric/nonebot-plugin-penguin.git\n\n</details>\n<details>\n<summary>poetry</summary>\n\n    poetry add git+https://github.com/AzideCupric/nonebot-plugin-penguin.git\n\n</details>\n\n打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入\n\n    plugins = ["nonebot_plugin_penguin"]\n\n</details>\n\n## ⚙️ 配置\n\n在 nonebot2 项目的`.env`文件中添加下表中的必填配置\n\n|       配置项       | 必填 | 默认值 |                     说明                     |\n| :----------------: | :--: | :----: | :------------------------------------------: |\n|  penguin_mirrior   |  否  |   io   | 选择企鹅物流网站镜像为`国际(io)`或`国内(cn)` |\n| penguin_show_count |  否  |   5    |             查询结果显示的条目数             |\n\n## 🎉 使用\n\n### 指令\n\n    格式:\n    query [-h] {item,stage,exact} names [names ...] [-s {cn,kr,us,jp}] [-l {zh,ko,en,ja}] [-k {percentage,apPPR}] [-f {all,only_open,only_close}] [-t THRESHOLD] [-r]\n\n    位置参数:\n    {item,stage,exact}    查询类型\n    names                 关卡/掉落物名称或别名(H12-4 / 紫薯 / 固源岩), type为exact时，关卡在前，空格隔开, 例如: 1-7 固源岩\n\n    options:\n    -h, --help              显示帮助\n    -s {cn,kr,us,jp}, --server {cn,kr,us,jp}\n                            游戏服务器选择, 默认为cn\n    -l {zh,ko,en,ja}, --lang {zh,ko,en,ja}\n                            生成回复时使用的语言, 默认为zh\n    -k {percentage,apPPR}, --sort {percentage,apPPR}\n                            排序方式, 默认为percentage, apPPR: 每个掉落物平均消耗理智\n    -f {all,only_open,only_close}, --filter {all,only_open,only_close}\n                            关卡过滤方式，默认为all\n    -t THRESHOLD, --threshold THRESHOLD\n                            掉落物过滤阈值, 默认超过100的样本数才会显示\n    -r, --reverse         是否反转排序\n\n例子:\n\n1. 查询12-4的掉落物\n   query stage H12-4\n2. 查询紫薯的掉落关卡\n   query item 紫薯\n3. 查询12-4的掉落物, 且只显示开放的关卡\n   query stage 12-4 -f only_open\n4. 查询1-7的固源岩的掉落信息\n   query exact 1-7 固源岩\n\n\\*请自行添加你给bot设置的命令前缀，如/query, #query\n\n### :warning:已知问题\n\n0. 初次安装时，若之前没有使用过`nonebot-plugin-htmlrender`, 第一次发送命令时会开始安装浏览器，可能会比较~~非常~~慢\n1. stage/exact查询目前还无法区分别传，复刻，初次的活动关卡(如生于黑夜DM-X, 偷懒还没写 :dove::dove::dove:)\n2. 发送查询命令之后，还需要再发一条无关消息才会开始渲染图片(会话控制问题，在改了在改了)\n3. 如果使用物品别名进行查询(如：狗粮)，可能会提示出现多个结果，但需要发送一条无关消息后bot才会回复选项，之后才能回复相应序号(还是会话控制问题，在改了在改了)\n',
    'author': 'Azide',
    'author_email': 'rukuy@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/AzideCupric/nonebot-plugin-penguin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
