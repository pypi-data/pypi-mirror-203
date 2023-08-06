from setuptools import setup, find_packages

requirements = [
    'opencv-python',
    'setuptools',
    'tensorrt',
    'numpy',
    'pycuda',
    'scipy',
    'lap',
    'cython',
    'cython_bbox'
]

__version__ = 'V3.04.18'

setup(
    name='meta-person',
    version=__version__,
    author='CachCheng',
    author_email='tkggpdc2007@163.com',
    url='https://github.com/CachCheng/cvtrack',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    description='Meta Person Toolkit',
    license='Apache-2.0',
    packages=find_packages(exclude=('docs', 'tests', 'scripts')),
    zip_safe=True,
    include_package_data=True,
    install_requires=requirements,
)
