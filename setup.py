from setuptools import find_packages, setup

setup(
    name='api.anudeepchpaul.in',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'setuptools',
        'pymongo',
        'flask_cors',
        'bson'
    ],
    entry_points='''
        [console_scripts]
        api=commands:hello
    '''
)
