from setuptools import setup, find_packages

setup(
    name='package01yxx',	# 包名
    version='0.1.0',	# 版本号
    description='My awesome module',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pytest',
    ],
)