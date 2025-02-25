import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='BraketLab',  
     version='0.93',
     author="Audun Skau Hansen",
     author_email="a.s.hansen@kjemi.uio.no",
     description="Educational tool for learning quantum theory with Jupyter Notebooks",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.uio.no/audunsh/braketlab",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires = ["sympy", "numba", "py3Dmol", "bubblebox"],
 )
