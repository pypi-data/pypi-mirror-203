from distutils.core import setup

setup(
  name = 'botpunk-jed',         
  packages = ['botpunk'],   
  version = '0.5',      
  license='MIT',        
  description = 'A bot that solves quizzes for you',   
  author = 'Jed',                   
  author_email = 'joshuaelijah.davis@gmail.com',     
  url = 'https://github.com/JJJed/botpunk',   
  download_url = 'https://github.com/JJJed/botpunk/archive/refs/heads/master.zip',    
  keywords = ['BOT', 'QUIZZES', 'JETPUNK'],   
  install_requires=[            
          'selenium',
          'beautifulsoup4',
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.8',
  ],
)
