from setuptools import setup

setup(
    name='shreycriclivemac',
    version='0.3',
    py_modules=['shreycricmac'],
    install_requires=[
        'requests',
        'lxml',
        'beautifulsoup4',
    ],
    entry_points='''
        [console_scripts]
        shreycriclivemac-run=shreycriclivemac:main
    ''',
)
