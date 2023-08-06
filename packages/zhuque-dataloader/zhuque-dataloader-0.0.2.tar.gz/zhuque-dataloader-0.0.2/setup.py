# -*- coding:utf-8 -*-


from setuptools import setup, find_packages

setup(
    name='zhuque-dataloader',
    version='0.0.2',
    description='zhuque graph platform dataloader component',
    author='yanrisheng',
    author_email='yanrs@zhejianglab.com',
    packages=find_packages(),
    requires=[],  # 定义依赖
    license='GPL 3.0'
)


# python setup.py bdist_wheel
# python setup.py sdist
# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
