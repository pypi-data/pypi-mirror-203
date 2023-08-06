import os

from setuptools import setup

package_name = 'fastapi_ecommerce_ext'
url = f'https://github.com/coolworld2049/fastapi-ecommerce/pypi/{package_name}'
version = 'v0.2.2'
setup(
    name=package_name,
    version=version,
    packages=['fastapi_ecommerce_ext.logger'],
    install_requires=[
        'loguru',
        'starlette',
    ],
    url=url,
    download_url=f'{url}-{version}.tar.gz',
    license='MIT',
    author='coolworld2049',
    description='logging extension for fastapi-microservices'
)
