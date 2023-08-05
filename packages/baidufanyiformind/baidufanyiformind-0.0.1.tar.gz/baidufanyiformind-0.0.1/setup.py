import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="baidufanyiformind",
    version="0.0.1",
    author="liliang",
    author_email="liang.li@dfrobot.com",
    description="A package for baidufanyi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/liliang9693/baidufanyiformind",
    packages=setuptools.find_packages(),
    install_requires=['hashlib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)