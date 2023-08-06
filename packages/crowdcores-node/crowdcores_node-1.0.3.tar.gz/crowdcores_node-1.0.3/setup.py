from setuptools import setup, find_packages

setup(
    name='crowdcores_node',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[
        'websockets',
        'torch',
        'transformers'
    ],
    entry_points={
        'console_scripts': [
            'crowdcores_node = crowdcores_node.node:main'
        ]
    }
)
