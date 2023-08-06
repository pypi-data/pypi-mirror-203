from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Optimization Model of Unit Commitment and Economic Dispatch with Calculation of LMP Prices'

# Setting up
setup(
    name="powergridsim",
    version=VERSION,
    author="Junying (Alice) Fang",
    author_email="jf3187@columbia.edu",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy>1.21', 'pandas', 'scipy', 'dill', 'matplotlib',
        'gurobipy'],
    keywords=['optimization', 'grid', 'electricity', 'energy', 'unit commitment', 'economic dispatch', 'lmp']
    # python_requires='>=3.8,<=3.11'
)