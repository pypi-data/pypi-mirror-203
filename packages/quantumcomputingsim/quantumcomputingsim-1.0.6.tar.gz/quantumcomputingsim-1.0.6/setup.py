from distutils.core import setup
setup(
  name = 'quantumcomputingsim',         # How you named your package folder (MyLib)
  packages = ['quantumcomputingsim'],   # Chose the same as "name"
  version = '1.0.6',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A library to simulate quantum computations',   # Give a short description about your library
  author = 'Shaik Mohammed Touseef',                   # Type in your name
  author_email = 'shaikm259@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/stealthypanda/quantumcomputingsim',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/stealthypanda/quantumcomputingsim/archive/v_1.0.1.tar.gz',    # I explain this later on
  keywords = ['quantum', 'simulator'],   # Keywords that define your package best
  install_requires = [],
  classifiers=[
    #'Development Status :: Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)