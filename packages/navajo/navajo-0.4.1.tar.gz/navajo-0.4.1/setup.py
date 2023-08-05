from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

def get_version():
   with open('src/navajo/assets/version.txt') as fp:
      return fp.read().strip()

def read_requirements():
   with open('requirements.txt', 'r') as req:
       requirements = req.readlines()
       requirements = [x.strip() for x in requirements]
   return requirements

setup(
   name="navajo",
   version=get_version(),
   package_dir={'': 'src'},
   packages=find_packages(where='src'),
   description="Talk to your code!",
   long_description=long_description,
   long_description_content_type='text/markdown',
   package_data={'navajo': ['assets/*', 'server/prompts/*']},
   install_requires=read_requirements(),
   entry_points={
      'console_scripts': [
         'navajo=navajo.main:main'
      ]
   }
)
