#! /usr/bin/env python
# -*- coding: utf-8 -*_
# ============================================
# 作者：
# 版本：
# 更新日期：
# ============================================
from distutils.core import setup
import setuptools

setup(
    name='E_ExecuteCommand',  # 包的名字
    version='0.0.1',  # 版本号
    description='串口命令读取',  # 描述
    author='Edison',  # 作者
    author_email='778470787@qq.com',  # 你的邮箱**
    url='https://gitee.com/toyylhome/edison_serial_command/E_ExecuteCommand.git',  # 可以写github上的地址，或者其他地址
    packages=setuptools.find_packages(exclude=[]),  # 包内不需要引用的文件夹

    # 依赖包
    # install_requires=['datetime', 'Duration', 'ExecuteCommand'
    # ],
    install_requires=['datetime'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: Microsoft'  # 你的操作系统
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: BSD License',  # BSD认证
        'Programming Language :: Python',  # 支持的语言
        'Programming Language :: Python :: 3',  # python版本 。。。
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
)
