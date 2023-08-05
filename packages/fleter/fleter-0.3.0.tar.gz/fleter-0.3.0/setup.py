from setuptools import find_packages, setup

setup(
    name="fleter",
    version="0.3.0",
    author="XiangQinxi",
    author_email="XiangQinxi@outlook.com",
    description="flet extension library",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    install_requires=[
        "flet>=0.5.2"
    ],
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests", "docs", "fleter_test"]

    ),
    package_data={"fleter": ["*.ttc"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'gui_scripts': [
            'fleter-demo = fleter_demo:run',
        ],
    },
)
