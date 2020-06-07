import os
import setuptools

install_requires = []
req_path = os.path.dirname(os.path.realpath(__file__)) + '/requirements.txt'
with open('./requirements.txt') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="torchtils",
    version="0.0.31",
    author="Saandeep Aathreya",
    author_email="saandeepa.93@gmail.com",
    description="Utility of vision methods",
    long_description="""
    Torchtils is a utility library with implementations of primitive algorithms
    as well as intricate scholarly papers, all in PyTorch
    """,
    long_description_content_type="text/markdown",
    url="https://torchtils.surge.sh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_requires
)