from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.8'
]
 
setup(
  name='ListDash',
  version='0.0.1',
  description='returns the dashes based on the length of the biggest length character',
  long_description=open('README').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='http://monilboy.liveblog365.com',  
  author='Monil Darediya',
  author_email='monildarediya1@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='dir-organise', 
  packages=find_packages(),
  install_requires=[] 
)
