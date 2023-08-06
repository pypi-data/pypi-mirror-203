from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(name='dsdata',
      version='1.1.0.3',
      author="datasense developer",
      description="load and upload datasense platform of data",
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['dsdata', 'dsdata.client', 'dsdata.db', 'dsdata.hosts', 'dsdata.models', 'dsdata.client._swagger', 'dsdata.client._swagger.apis'],
      install_requires=['pandas', 'JayDeBeApi', 'requests', 'tqdm'],
      package_data={'dsdata': ['datasense-jdbc-client.jar']},
      python_requires='>=3.7'
      )