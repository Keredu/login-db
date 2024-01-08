from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='login_db',
    version='0.1.0',
    description='Login DB',
    url='https://github.com/keredu/login-db',
    #author='Keredu',
    #author_email='your_email@example.com',
    packages=find_packages(where='login_db'),
    python_requires='>=3.10',
    install_requires=requirements
)