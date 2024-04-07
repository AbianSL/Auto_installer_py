
from distutils.core import setup, Extension

module = Extension('ped', sources = ['ped.c'])

setup(name = 'PackageName',
      version = '1.0',
      description = 'Calculate the proximity edit distance between two strings',
      author = 'Abian Santana Ledesma',
      ext_modules = [module])
