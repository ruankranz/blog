import setuptools
from package import Package

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="krankit-blog-pkg-ruank",  # Replace with your own username
    version="0.0.1",
    author="Ruan Kranz",
    author_email="ruan@krankit.co.za",
    description="The life and times of krankit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ruankranz/blog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    cmdclass={"package": Package},
)
