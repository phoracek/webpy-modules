from distutils.core import setup

setup(
    name='web.py-modules',
    packages=['webmod', 'test'],
    version='v0.1.1',
    author='Petr Horacek',
    author_email='p.horacek94@gmail.com',
    url='https://github.com/PetrHoracek/webpy-modules',
    download_url='https://github.com/PetrHoracek/webpy-modules/archive/'
                 'v0.1.1.tar.gz',
    license='MIT License',
    description='Optional modules for web.py framework.',
    long_description=open('README.rst').read(),
    install_requires=[
        "web.py >= 0.37"
    ],
    platforms=["any"]
)
