import setuptools

from bmgen.info import VERSION

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name = 'bmgen',
    version = VERSION,
    author = 'bms',
    author_email = 'bmgen@brokenmouse.studio',
    description = 'Broken Mouse Studios\' build solution',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://git.brokenmouse.studio/bms/bmgen',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
    ],
    install_requires = ['colorama'],
    python_requires = '>=3.10',
    entry_points={
        'console_scripts': [
            'bmgen=bmgen.__main__:main',
        ],
    },
)
