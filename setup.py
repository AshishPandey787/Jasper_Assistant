from setuptools import setup, find_packages
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    "This function will return the list of requirements for the project"
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        print(requirements)
        requirements= [req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements


setup(
    name='Agentic Project',
    version='0.0.1',
    author='Ashish',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  ,

)