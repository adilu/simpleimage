from distutils.core import setup
setup(
  name = 'simpleimage',
  packages = ['simpleimage'],
  version = '1.0.8',
  license='MIT',
  description = 'Simple image API for educational purposes',
  author = '3e8',
  author_email = 'info@3e8.ch',
  url = 'https://github.com/adilu/simpleimage',
  download_url = 'https://github.com/adilu/simpleimage/archive/v_1.0.8.tar.gz',
  keywords = ['Image', 'python', 'educational'],
  install_requires=[
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)