from setuptools import setup

VERSION = '1.2'
DESCRIPTION = 'Reading and writing to the memory of any process.'
LONG_DESCRIPTION = """
The UserReadWriteMemory module is specifically designed to enable the process of reading from and writing to the memory
of any given process. View documentation here: https://github.com/User00092/UserReadWriteMemory
"""

# Setting up
setup(
	name="UserReadWriteMemory",
	url="https://github.com/User00092/UserReadWriteMemory",
	version=VERSION,
	license='MIT',
	author="User0092",
	author_email="unknownuser0092@protonmail.com",
	description=DESCRIPTION,
	long_description_content_type="text/markdown",
	long_description=LONG_DESCRIPTION,
	packages=['UserReadWriteMemory'],
	keywords=['Read Memory', 'Write Memory', 'Process memory', 'Hacking', 'UserReadWriteMemory'],
	python_requires='>=3.4.0',
	install_requires=[],
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
