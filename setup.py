

from setuptools import setup, find_packages

setup(
    name='fears_md', 
    version='0.1.0', 
    author = 'Eshan King', 
    author_email = '',
    # packages=['autorate', "autorate.test", "autorate.test.data"], 
    # pacakges=['fears','fears.data','fears.utils'],
    packages=find_packages(include=['fears_md','fears_md.population','fears_md.data','fears_md.utils','fears_md.utils.*']),
    # packages=find_packages(where="fears"),
    install_requires = [
      "pandas",
      "pytest",
      "scipy",
      "matplotlib",
      "numpy",
      "importlib_resources", 
      "lifelines", 
      "seaborn", 
      "networkx",
      "cycler",
      "matplotlib-label-lines"
    ],
    include_package_data=True,
    package_data={'': ['data/*.csv', 'data/plates/*.csv','data/*.xlsx']}
)