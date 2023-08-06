import setuptools

long_description = ""
with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pexicdb",
    version="0.0.1",
    author="Harkishan Khuva",
    author_email="harkishankhuva02@gmail.com",
    description="Pexicdb is a simple model based file database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hakiKhuva/pexicdb",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Environment :: Console"
    ],
    package_dir={"pexicdb": "pexicdb"},
    packages=["pexicdb"],
    python_requires=">=3.10",
    license="MIT"
)