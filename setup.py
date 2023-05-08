# -*- encoding: utf-8 -*-
# Author: li_colin

import setuptools

setuptools.setup(
    name="something_new",
    version="0.0.0",
    author="li colin",
    author_email="li_colin@126.com",
    description="xx",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/licolin/something_new",
    packages=setuptools.find_packages("pipeline_runner"),
    package_dir={"": "src"},
    # package_data=package_data,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Bug Tracking",
        "Topic :: System :: Logging"
    ],
    python_requires=">=3.7"
)
