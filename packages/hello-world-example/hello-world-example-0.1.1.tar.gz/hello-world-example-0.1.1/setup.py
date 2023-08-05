from setuptools import setup, find_packages

setup(
    name="hello-world-example",
    version="0.1.1",
    author="waterbottel2487",
    author_email="waterbottle2487@gmail.com",
    url="https://github.com/mulkong/package_tutorial.git",
    description="A hello-world example package",
    packages=find_packages(),
    install_requires=[
    'pandas'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
