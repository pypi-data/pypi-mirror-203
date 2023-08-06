from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='i9-everywhere-client',
    version='0.1.0',
    description='A Python client library and CLI for the I9 Everywhere API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Paul Smith',
    author_email='paul@adhoc.team',
    url='https://github.com/adhocteam/i9everywhere-python',
    packages=find_packages(),
    install_requires=[
        'click',
        'httpx',
    ],
    entry_points={
        'console_scripts': [
            'i9everywhere = i9_everywhere_client.cli:cli',
        ]
    },
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
