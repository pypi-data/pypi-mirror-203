# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['najia']

package_data = \
{'': ['*'], 'najia': ['data/*']}

install_requires = \
['arrow>=1.2.3,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'sxtwl<2',
 'tzlocal>=4.3,<5.0']

setup_kwargs = {
    'name': 'najia',
    'version': '0.1.1',
    'description': '',
    'long_description': "# 纳甲六爻排盘项目\n\n[![image](https://img.shields.io/pypi/v/najia.svg)](https://pypi.python.org/pypi/najia)\n\n[![image](https://img.shields.io/travis/bopo/najia.svg)](https://travis-ci.org/bopo/najia)\n\n[![Documentation Status](https://readthedocs.org/projects/najia/badge/?version=latest)](https://najia.readthedocs.io/en/latest/?badge=latest)\n\n[![Updates](https://pyup.io/repos/github/bopo/najia/shield.svg)](https://pyup.io/repos/github/bopo/najia/)\n\nPython Boilerplate contains all the boilerplate you need to create a\nPython package.\n\n-   Free software: MIT license\n-   Documentation: <https://najia.readthedocs.io>.\n\n## Features\n\n-   全部安易卦爻\n-   函数独立编写\n-   测试各个函数\n-   重新命名函数\n\n阳历，阴历（干支，旬空）\n\n-   卦符: mark (001000)，自下而上\n-   卦名: name\n-   变爻: bian\n-   卦宫: gong\n-   六亲: qin6\n-   六神: god6\n-   世爻: shiy, ying\n-   纳甲: naja\n-   纳甲五行: dzwx\n-   卦宫五行: gowx\n\n## 修复问题\n\n-   解决: 六神不对\n-   解决: 世应也有点小BUG , 地天泰卦的世爻为3, 应爻为6\n-   解决: 归魂卦世爻为3 此处返回4, 需要修改\n\n\\* 解决: 归魂卦的六亲是不对的,原因是utils.py里\n判断六爻卦的卦宫名时,优先判读了if index in (1, 2, 3, 6)\n而归魂卦的世爻也在3爻,被这个条件带走了. 解决: elif hun==\\'归魂\\'\n这个条件调到前面即可 \\* 解决: 还有一个不知是否算是错误的地方,就是bian\n变卦中的六亲,\n程序中是按变卦所在的本宫卦来定的,而不是按初始卦所属的本宫卦来定的六亲.\n\n## Credits\n\nThis package was created with\n[Cookiecutter](https://github.com/audreyr/cookiecutter) and the\n[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)\nproject template.\n",
    'author': 'bopo',
    'author_email': 'ibopo@126.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
