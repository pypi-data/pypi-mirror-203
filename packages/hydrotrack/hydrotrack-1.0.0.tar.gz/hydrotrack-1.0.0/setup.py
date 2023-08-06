import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hydrotrack",
    version="1.0.0",
    author="Helvecio B. L. Neto, Alan J. P. Calheiros",
    author_email="hydrotrack.project@gmail.com",
    description="A Python package for track and forecasting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hydrotrack-project/hydrotrack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",  
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)