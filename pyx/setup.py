from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
	name = 'compute',
	ext_modules=cythonize([
		Extension("compute", ["compute.pyx"]),
	]),
)
