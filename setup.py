from setuptools import setup, find_packages

setup(
    name="your-django-project",
    version="0.1.0",
    author="Prathamb",
    author_email="your.email@example.com",
    description="A Django project",
    packages=find_packages(),
    install_requires=[
        "django",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
)
