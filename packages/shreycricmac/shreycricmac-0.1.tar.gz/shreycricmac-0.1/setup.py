from setuptools import setup

setup(
    name='shreycricmac',
    version='0.1',
    py_modules=['my_package'],
    install_requires=[
        'requests',
        'lxml',
        'beautifulsoup4',
    ],
    entry_points='''
        [console_scripts]
        my_package=my_package:main
    ''',
)
