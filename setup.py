from setuptools import setup,find_packages
from typing import List

PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION = "This is Machine Learning Project"
AUTHOR = "Chandrakant Thakur"
AUTHOR_EMAIL = "chandrakantthakur817@gmail.com"
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

# 1st we open requirements.txt file
# 2nd read 
# 3rd replace new line with empty " "
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        requirements_list = requirements_file.readlines()
        requirements_list = [requirement_name.replace("\n","") for requirement_name in requirements_list]
        
        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)

            return requirements_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requries = get_requirements_list()
     )