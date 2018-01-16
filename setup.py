from setuptools import setup

setup(name='snipeit',
      version='0.3.1',
      description='Python library to access the SnipeIT API',
      url='http://github.ove.local/jlbloomer/code_libraries/tree/master/Python/snipeit',
      author='Jared Bloomer (Cox Automotive Inc.)',
      author_email='jared.bloomer@coxautoinc.com',
      license='MIT',
      packages=['snipeit'],
      install_requires=['requests','json'],
      zip_safe=False)
