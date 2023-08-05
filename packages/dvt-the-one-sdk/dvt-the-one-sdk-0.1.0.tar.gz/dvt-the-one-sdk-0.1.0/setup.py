from setuptools import setup, find_packages
from common.version import __version__

setup(
    name='dvt-the-one-sdk',
    version=__version__,
    description='The Lord of the Rings SDK encapsulating https://the-one-api.dev/documentation',
    author='Daniel Van Tassell',
    author_email='danielvantassell@gmail.com',
    package_data={
        "dvt-the-one-sdk": ["config.ini"]
    },
    include_package_data=True,
    packages=["src", "src.api", "src.client", "src.common"],
    install_requires=[
        'requests',
        'requests_mock',
        'setuptools'
    ],
)

