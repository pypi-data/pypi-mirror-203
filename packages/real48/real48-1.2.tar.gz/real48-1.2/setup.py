from setuptools import setup, Extension

setup(
    name='real48',
    version='1.2',
    ext_modules=[Extension('real48', ['real48tofloat.c'])],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)