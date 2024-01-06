import setuptools
from setuptools import find_packages
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()



HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


__version__ = "0.0.0"

REPO_NAME = "text_summarization"
AUTHOR_USER_NAME = "Vampaxx"
SRC_REPO = "text_summarization"
AUTHOR_EMAIL = "arjunappu1001@gmail.com"


setuptools.setup(
    name                    = SRC_REPO,
    version                 = __version__,
    author                  = AUTHOR_USER_NAME,
    author_email            = AUTHOR_EMAIL,
    description             = "Text summarization is a crucial natural language processing task that involves condensing a given piece of text while retaining its essential information",
    long_description        = long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "text summarization" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))