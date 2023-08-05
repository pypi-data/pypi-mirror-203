from setuptools import setup, find_packages

# Read the content of the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='gitpulse',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here:
        'gitpython',
        'jinja2',
        'python-dateutil',
    ],
    entry_points={
        'console_scripts': [
            'gitpulse = gitpulse.gitpulse_cli:main',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
