import os
import versioneer

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup_options = dict(
    name='type_registry',

    cmdclass=versioneer.get_cmdclass(),
    version=versioneer.get_version(),

    description='Package for registering types and creating systems based on config files',

    long_description=long_description,
    long_description_content_type="text/markdown",

    author='Michael Wright',
    url='https://github.com/mikewright/py-type-registry.git',

    packages=find_packages(exclude=['tests*']),
    license="MIT License",

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    install_requires=[
        'PyYAML (>=3.13,<4.0)',
        'termcolor (>=1.1.0,<2.0)',
    ],

    extras_require={
        'dev': [
            'wheel>=0.29',
            'pytest>=3.0',
            'pytest-cov>=2.4',
            'pylint>=1.8.1'
        ],
    },
)

setup(**setup_options)
