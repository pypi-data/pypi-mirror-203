from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='create_docker_compose',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'create_docker_compose = create_docker_compose.create_docker_compose:main',
            'create_env_file = create_env_file.create_env_file:main',
        ]
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)