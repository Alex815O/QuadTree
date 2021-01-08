import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QuadTree", # Replace with your own username
    version="0.0.1",
    author="Alex Ofner",
    author_email="alexofner01@gmail.com",
    description="An implementation of a quadtree",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alex815O/QuadTree",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)