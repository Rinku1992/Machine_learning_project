from setuptools import setup, find_packages
from typing import List

def get_requirements_list()->List[str]:

    """
    Description: this function is going to return list of
    requirements for this project
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

#Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.3"
AUTHOR = "Ravikant"
DESCRIPTION = "This is a first FSDS Learning project"
# PACKAGES= ['housing']
REQUIREMENT_FILE_NAME = "requirements.txt"

setup(
    name = PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
install_requires = get_requirements_list( )

)