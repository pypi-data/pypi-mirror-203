from setuptools import setup, find_namespace_packages

setup(
    name = 'win-cmd-cleaner',
    author = 'Crimzega Sulvic',
    author_email = 'tpodCI@gmail.com',
    version = '1.0.0',
    license = 'GPL-3.0',
    description = 'A customized cleaner for Windows command-line files',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/crimzega/win-cmd-cleaner',
    keywords = 'windows command cleaner, command cleaner, win cmd cleaner, cmd cleaner',
    packages = find_namespace_packages(
        include = ['win-cmd-cleaner', 'win-cmd-cleaner.*']
    ),
    python_requires = '>=3.7'
)
