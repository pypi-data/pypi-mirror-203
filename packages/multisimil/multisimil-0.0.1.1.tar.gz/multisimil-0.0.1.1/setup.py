from setuptools import setup, find_packages

with open("README.md", "r") as rd:
  long_description = rd.read()

setup(
 name='multisimil',
 version='0.0.1.1',
 description='A python package to find similarity between two images at multiple scales.',
 url='https://github.com/pratik-tan10/multisimil', 
 author='Pratik Dhungana',
 author_email='pdhungana@crimson.ua.edu',
 classifiers=[
   'Development Status :: 5 - Production/Stable',
   'Intended Audience :: Education',
   'Operating System :: OS Independent',
   'License :: OSI Approved :: MIT License',
   'Programming Language :: Python :: 3',
   'Programming Language :: Python :: 3.5',
   'Programming Language :: Python :: 3.6',
   'Programming Language :: Python :: 3.7',
   'Programming Language :: Python :: 3.8',
 ],
 install_requires=[
    "numpy ~= 1.24.1"
  ],
 keywords=['python', 'multisimil', 'land use validation', 'categorical similarity', 'multi-scale similarity'],
 packages=find_packages(),
 long_description=long_description,
 long_description_content_type="text/markdown"
)