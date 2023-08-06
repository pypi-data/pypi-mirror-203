from setuptools import setup, find_packages

setup(
    name='openneurofirstlevel',
    version='0.1',
    packages=find_packages(),
    author='Paul Jaffe',
    author_email='pauljaffe7@gmail.com',
    install_requires=['nilearn', 'matplotlib', 'statsmodels', 
                      'scipy', 'pandas', 'numpy', 'pyyaml']
)
