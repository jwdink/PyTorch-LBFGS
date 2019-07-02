from setuptools import setup, find_packages

setup(name='lbfgs',
      version='0.1',
      description='A PyTorch Implementation of L-BFGS',
      # url='http://github.com/strongio/kpi',
      # author='Jacob Dink',
      # author_email='jacob.dink@strong.io',
      # license='MIT',
      packages=[p for p in find_packages() if 'lbfgs' in p],
      zip_safe=False,
      install_requires=['torch==1.*'])
