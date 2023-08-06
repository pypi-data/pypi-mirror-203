import setuptools

setuptools.setup(
   name='flake8-checker',
   version='0.0.1',
   description='Plugin to comply with my picky standards',
   author='Harish, Dasika',
   author_email='harish.dasika@gmail.com',
   py_modules=['flake8_checker'],
   entry_points={
       'flake8.extension': [
           'ND001 = flake8_checker:NonDeterministicFunctionChecker',
       ],
   },
   install_requires=['flake8'],
   classifiers=[
       'Development Status :: 3 - Alpha',
   ],
)