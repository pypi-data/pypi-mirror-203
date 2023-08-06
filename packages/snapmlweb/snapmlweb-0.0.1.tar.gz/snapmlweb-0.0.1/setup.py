from setuptools import setup, find_packages
from pathlib import Path

setup(
  name='snapmlweb',
  version= '0.0.1',
  description='ML Helper Webapp',
  long_description=Path("README.md").read_text(encoding="utf-8"),
  long_description_content_type="text/markdown",
  url='https://github.com/Parth162/snapmlweb',  
  author='Anish Adnani, Parth Goel',
  author_email='anishadnani00@gmail.com',
  license='MIT', 
  keywords=['python', 'coding', 'ml', 'algorithms'],
  packages=find_packages(),
  install_requires=['snapalgo', 'pandas', 'numpy', 'scikit-learn', 'snapmlengine'] ,
  classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
