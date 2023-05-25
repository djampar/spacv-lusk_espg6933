from setuptools import setup

# Dependencies.
with open("requirements.txt") as f:
    tests_require = f.readlines()
install_requires = [t.strip() for t in tests_require]

with open("README.md") as f:
    long_description = f.read()

setup(
    name="spacv-lusk",
    version="0.0.21",
    description="Spatial cross-validation in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dluks/spacv-lusk",
    author="Sam Comber, Daniel Lusk",
    author_email="sam.comber@hotmail.co.uk, lusk@uni-potsdam.de",
    license="3-Clause BSD",
    packages=["spacv"],
    package_data={"": ["requirements.txt"]},
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Framework :: Matplotlib",
    ],
    python_requires=">=3.6",
    install_requires=install_requires,
    zip_safe=False,
)
