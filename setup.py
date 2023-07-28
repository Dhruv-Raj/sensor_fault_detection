# Setup.py file help in converting machine learning application as package.
# In Python, setup.py is a module used to build and distribute Python packages. 
# t typically contains information about the package, such as its name, version, -->
# -->                                                and dependencies, as well as instructions for building and installing the package. 

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.

    '''
    requirement_list:List[str]= []
    
    '''
    This code will read requirements.txt file and append each requirements in requirement_list variable.

    '''
    with open(file_path) as file_obj:
        requirement_list= file_obj.readlines()
        requirement_list= [req.replace('\n','') for req in requirement_list]

        if HYPEN_E_DOT in requirement_list:
            requirement_list= requirement_list.remove(HYPEN_E_DOT)
            print(requirement_list)

    return requirement_list

setup(name= 'Sensor',
      version= 0.01,
      author= 'Dhruv Saxena',
      author_email= 'saxena25dhruv@gmail.com',
      packages= find_packages(),
      install_requires=get_requirements('requirements.txt'),
      )