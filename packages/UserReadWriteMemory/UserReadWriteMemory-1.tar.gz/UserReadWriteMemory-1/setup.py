from setuptools import setup

VERSION = '1'
DESCRIPTION = 'Reading and writing to the memory of any process.'
LONG_DESCRIPTION = '''The ReadWriteMemory Class is made on Python for reading and writing to the memory of any process.
                   This Class does not depend on any extra modules and only uses standard Python libraries like ctypes.
                   '''

# Setting up
setup(
	name="UserReadWriteMemory",
	version=VERSION,
	author="User0092",
	author_email="unknownuser0092@protonmail.com",
	description=DESCRIPTION,
	long_description_content_type="text/markdown",
	long_description=LONG_DESCRIPTION,
	packages=['UserReadWriteMemory'],
	keywords=['Read Memory', 'Write Memory', 'Process memory', 'Hacking', 'UserReadWriteMemory'],
	python_requires='>=3.4.0',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Topic :: Utilities',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python',
		'Intended Audience :: Developers'
	],
)
