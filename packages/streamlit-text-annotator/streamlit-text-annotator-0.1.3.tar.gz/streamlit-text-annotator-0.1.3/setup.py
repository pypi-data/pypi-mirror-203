import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="st-text-annotator",
    version="0.1.3",
    author="Robin Marquet",
    author_email="robin.marquet3@gmail.com",
    description="Component for annotating text for NLP resolution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rmarquet21/steamlit-text-annotator",
    package_dir = {"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "streamlit >= 1.0.0",
    ],
)
