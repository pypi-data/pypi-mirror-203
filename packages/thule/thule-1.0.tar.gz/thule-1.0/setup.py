from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(name='thule',
      long_description=long_description,
      long_description_content_type='text/markdown',
      version='1.0',
      license='MIT',
      author='Cory Engdahl',
      author_email='cjengdahl@gmail.com',
      description='Module to facilitate actions on a file tree.',
      py_modules=["thule"],
      url='https://github.com/cjengdahl/thule',
      keywords='file walker',
     )

