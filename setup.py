from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    
     with open('requirements.txt') as f:
        for line in f:
            requirement_list.append(line.strip())
    """
   

    return requirement_list


## setup.py: https://stackoverflow.com/questions/1471994/what-is-setup-py
setup(
    
    name = 'sensor',
    version = '0.0.1',
    author = 'Paris-DS',
    author_email= "paristian715@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(), #['pymongo==4.2.0']
)
