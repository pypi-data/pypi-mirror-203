from setuptools import setup, find_packages

with open('README.md', encoding="utf8") as readme_file:
    README = readme_file.read()

setup(name='stringhandling',
    version='0.3',
    description='Python package for string handling',
    long_description_content_type="text/markdown",
    long_description=README,
    author='Subeesh Palamadathil',
    author_email='subi4020@gmail.com',
    license='MIT',
    packages=['stringhandling'],
    zip_safe=False)
