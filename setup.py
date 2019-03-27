from setuptools import setup

with open("README.md","r") as fh:
	long_description = fh.read()
	
setup(name='snipeit',
      version='0.11',
      description='Python library to access the SnipeIT API',
      url='https://github.com/veenone/SnipeIT-PythonAPI',
      author='Jared Bloomer (Cox Automotive Inc.)',
      author_email='jared.bloomer@coxautoinc.com',
      license='MIT',
      packages=['snipeit'],
      install_requires=['requests','simplejson'],
	  long_description=long_description,
	  long_description_content_type="text/markdown",
      zip_safe=False)
