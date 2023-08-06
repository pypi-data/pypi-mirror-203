import os

from dotenv import load_dotenv
from setuptools import setup

load_dotenv()

package_name = 'fastapi_ecommerce_ext'
url = f'{os.getenv("GIT_REPO")}/pypi/{package_name}'
version = 'v0.1.2'
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
    author=os.getenv("GIT_USERNAME"),
    description='logging extension for fastapi-microservices'
)
