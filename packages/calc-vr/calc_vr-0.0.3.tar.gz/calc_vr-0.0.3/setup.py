import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="calc_vr",
    version="0.0.3",
    author="ramachandran",
    author_email="rama5864@gmail.com",
    description="a simple arithmetic package",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    url="https://github.com/rmvr/calc_vr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires='>3.6'
)

    