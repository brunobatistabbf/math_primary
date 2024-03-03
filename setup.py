from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='math_primary',
    version='0.0.1',
    license='MIT License',
    author='Bruno Batista',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='brunobatistaferreirabbf@gmail.com',
    keywords='basic math primary',
    description=u'All Math Basic Package',
    packages=['math_primary'],
    install_requires=[''],)