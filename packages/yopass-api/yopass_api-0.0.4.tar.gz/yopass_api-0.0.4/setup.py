from setuptools import find_packages, setup


def readme():
    with open(file="README.md", encoding="UTF-8", mode="r") as file_stream:
        return file_stream.read()


setup(
    name="yopass_api",
    version="0.0.4",
    author="Sergey Ilyashevich",
    author_email="silyashevich@gmail.com",
    description="This module will allow you to use Python and Yopass in automation projects",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/silyashevich/yopass_api",
    packages=find_packages(),
    install_requires=[
        "PGPy>=0.6.0",
        "requests>=2.28.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "yopass",
        "api",
        "cryptography",
    ],
    python_requires=">=3.6",
)
