from distutils.core import setup
import py2exe

setup(name="fijiconvert",
      version="0.1",
      author="Jean Fecteau",
      author_email="jfecteau@mbfbioscience.com",
      license="GNU General Public License (GPL)",
	  url="mbf.mbf",
	  windows=[{"script": "main.py"}])