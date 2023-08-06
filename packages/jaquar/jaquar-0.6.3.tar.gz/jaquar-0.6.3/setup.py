from setuptools import setup, find_packages

setup(
    name='jaquar',
    version='0.6.3',
    description='A web framework for python',
    url='http://skillfam.writermint.com',
    license='BSD',
    author='Kipono Japhet',
    packages=find_packages(),
    include_package_data=True,
    package_data={'jaquar': ['templates/*', 'static/*', 'db/*', 'config/*', 'views/*', 'models/*', 'jq.py']},
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
