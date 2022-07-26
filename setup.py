# - * -coding: utf - 8 - * -
import setuptools

setuptools.setup(
    name="observer-hooks",
    version="1.0.0",
    author="Ryan McConnell",
    author_email="",
    description="Easy, minimalist tools for function side-effects and observer pattern with weak references",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
    install_requires=['ordered-set>=4.1.0']
)
