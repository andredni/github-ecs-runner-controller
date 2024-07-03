from setuptools import setup, find_packages

setup(
    name='github-ecs-runner-controller',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'boto3'
    ],
    entry_points={
        'console_scripts': [
            'controller=controller:main'
        ]
    }
)
