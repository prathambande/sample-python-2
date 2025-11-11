from setuptools import setup, find_packages

setup(
    name='django-ogf',
    version='0.1.0',
    description='A simple Django application with placeholder endpoint',
    author='OGF Linux',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/django-ogf',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2,<5.0',
    ]
)
