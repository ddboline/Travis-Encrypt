from setuptools import setup

setup(name='travis-client',
      version='0.0.1',
      author='Mandeep Bhutani',
      author_email='info@mandeep.xyz',
      description='A command line application that encrypts passwords for use with Travis CI.',
      license='GPLv3+',
      packages=['travis', 'travis.tests'],
      install_requires=[
        'click==6.6',
        'cryptography==1.5',
        'PyYAML==3.12',
        'requests==2.9.1'
      ],
      entry_points='''
        [console_scripts]
        travis-encrypt=travis.encrypt:cli
        ''',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
      ],
      )
