from setuptools import setup, find_packages

setup(
    name='jaquar',
    version='0.5.3',
    description='A web framework for python',
    url='http://skillfam.writermint.com',
    license='BSD',
    author='Kipono Japhet',
    packages=find_packages(),
    package_data={
        'jaquar': ['templates/*', 'static/*/*/*']
    },
    include_package_data=True,
    install_requires=[
        'click',
        'Jinja2',
        'sqlalchemy',
        'werkzeug',
    ],
    entry_points='''
        [console_scripts]
        jaquar=jaquar.cli:cli
    ''',
)
