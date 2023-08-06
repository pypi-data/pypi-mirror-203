from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='browseapi_sandbox',
    packages=find_packages(exclude=['test']),
    version='0.4',
    license='MIT',
    description='eBay Browse API Python client',
    long_description=long_description,
    author='Alexander Tedrow',
    author_email='atedrow@clemson.edu',
    url='https://github.com/atedrow/browseapi_sandbox',
    download_url='https://github.com/atedrow/browseapi_sandbox/archive/refs/tags/v_04.tar.gz',
    keywords=['ASYNC', 'BROWSE API', 'CLIENT'],

    install_requires=[
        'aiohttp',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
