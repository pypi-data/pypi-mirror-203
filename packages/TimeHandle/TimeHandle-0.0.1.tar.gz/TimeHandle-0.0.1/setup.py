import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TimeHandle",
    version="0.0.1",
    author="cahy-jjw",
    author_email="jjwjiawang@163.com",
    description="cahy Test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
