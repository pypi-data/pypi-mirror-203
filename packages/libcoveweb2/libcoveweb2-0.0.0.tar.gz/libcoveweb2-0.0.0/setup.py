from setuptools import setup, find_packages

install_requires = []

setup(
    name='libcoveweb2',
    version='0.0.0',
    author='Open Data Services',
    author_email='code@opendataservices.coop',
    packages=find_packages(),
    package_data={
        'libcoveweb2': [
            'static/*',
            'static/*/*',
            'static/*/*/*',
            'static/*/*/*/*',
            'templates/*',
            'templates/*/*'
        ]
    },
    url='https://github.com/OpenDataServices/lib-cove-web-2',
    description='',
    classifiers=[
    ],
    python_requires=">=3.8",
    install_requires=[
    ],
    extras_require={
    }
)

