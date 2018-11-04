import setuptools


setuptools.setup(
    #
    # Package
    #

    name='ltsv-scores',
    version='0.1.0',

    url='https://github.com/okeyaki/ltsv-scores',
    description='A tool for calculating LTSV field scores',
    license='MIT',

    #
    #
    #

    packages=setuptools.find_packages(),

    entry_points={
        'console_scripts': [
            'ltsv-scores = app.main:main',
        ],
    },

    #
    # Requirements
    #

    install_requires=[
        'PyYAML==3.13',
        'injector==0.14.1',
        'logbook==1.4.1',
        'numpy==1.15.3',
        'pandas==0.23.4',
    ],

    extras_require={
        "dev": [
            'flake8==3.6.0',
        ],
    },
)
