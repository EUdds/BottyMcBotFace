from distutils.core import setup

setup(name='DaBotty',
      version='1.0',
      description='Dabotty',
      author='Da Baby',
      author_email='Udlis.eric@gmail.com',
      entry_points = {
            'console_scripts': [
                  'dabotty = dabotty.modules.main:main'
            ]
      }
)
