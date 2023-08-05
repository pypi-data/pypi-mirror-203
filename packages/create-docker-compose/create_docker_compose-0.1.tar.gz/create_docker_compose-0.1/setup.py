from setuptools import setup, find_packages

setup(
    name='create_docker_compose',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'create_docker_compose = create_docker_compose.create_docker_compose:main',
            'create_env_file = create_env_file.create_env_file:main',
        ]
    }
)