from distutils.core import setup

setup(
    name='CityState',
    version='0.0.1',
    author=['Zhifan Sang', 'Xinmei Gui'],
    author_email='zfsang@gmail.com',
    packages=['citystate'],
    scripts=['city_state.py'],
    url='https://github.com/zfsang/CityState',
    license='LICENSE',
    description='City State Game',
    long_description=open('README.md').read(),
    install_requires=[
        "pygame >= 1.9.6",
    ],
)