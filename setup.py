from distutils.core import setup

with open('README') as file:
    readme = file.read()

setup(
    name='game_knight',
    version='1.0.0',
    packages=['wargame'],
    url='http://localhost:8081/simple/',
    license='LICENSE',
    description='Python study knight game',
    long_description=readme,
    author='helewonder',
    author_email='wxd465@hotmail.com'
)
