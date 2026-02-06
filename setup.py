from setuptool import setup, find_packages   
from typing import List


def get_requirements(file_path:str)-> list[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements
setup(
    name='Ml projecty ',
    version='0.1',
    packages=find_packages(),
    author='aditya',
    install_requires=get_requirements('requirements.txt' )
    
     )
