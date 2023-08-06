from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='axisCalculator',
  version='0.0.1',
  description='Robotic kinematics calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Barış Çeliker',
  author_email='td21brs14@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='kinematics', 
  packages=find_packages(),
  install_requires=['matplotlib>=3.7.1','numpy>=1.24.2'] 
)
