from setuptools import setup

setup(
    name='db_cli',
    version='0.1.0',
    license='Public Domain',
    long_description=open('README.md').read(),
    py_modules=['database_url_cli'],
    install_requires=[
        'click==3.3'
    ],
    entry_points={
        'console_scripts': [
            'db=database_url_cli:connect_to_database'
        ]
    }
)
