from setuptools import setup,find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'modelreport',         
  packages = ['modelreport'],  
  version = '0.1',      
  license='MIT',        
  description = 'A lightweight library to get the all classification metric scores.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'SusmitPanda',                   
  author_email = 'susmit.vssut@gmail.com',  
  install_requires=['scikit-learn','pandas'],  
  keywords = ['accuracy', 'confusion_matrix','precision_score','recall_score','f1_score','auc','matthews_corrcoef','cohen_kappa_score','classification report'],   
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],)