from distutils.core import setup

setup(
    name='webmod',
    packages=['webmod', 'test'],
    version='0.1',
    author='Petr Horacek',
    author_email='p.horacek94@gmail.com',
    url='http://pypi.python.org/pypi/web.py-modules/',
    license='MIT License',
    description='Optional modules for web.py framework.',
    long_description=open('README.rst').read(),
    install_requires=[
        "web.py >= 0.37"
    ],
)
