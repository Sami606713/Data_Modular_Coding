from setuptools import find_packages,setup
from typing import List
hifen='-e .'
def load_packages(file_path:str)->List[str]:
    """
    Reading the require packages
    """
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[file.replace("\n","") for file in requirements]

        if(hifen in requirements):
            requirements.remove(hifen)
    return requirements


setup(
   name='End-To-End DataScience Project',
   version='0.0.1',
   author="Samiullah",
   author_email="sami606713@gmail.com",
   packages=find_packages(),
   install_requiires=load_packages('requirements.txt')
)