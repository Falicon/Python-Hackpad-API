from distutils.core import setup

setup(name='python_hackpad_api',
      version='beta',
      description='A simple wrapper library for the Hackpad API',
      url='https://github.com/Falicon/Python-Hackpad-API',
      package_dir={'python_hackpad_api': 'hackpad_api'},
      packages=['hackpad_api'],
      install_requires=[
            'argparse==1.2.1',
            'httplib2==0.8',
            'requests-oauthlib==0.4.2',
            'requests==2.2.1',
            'wsgiref==0.1.2']
      )
