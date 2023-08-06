import setuptools 
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="birenci-infra", 
    version="0.0.4",    
    author="br_infra",    
    author_email="br_infra@birentech.com",    
    description="biren ci sdk",
    long_description=long_description,    
    long_description_content_type="text/markdown",
    url="https://gitlab.birentech.com/software/br_ci_db",    
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',   
)
