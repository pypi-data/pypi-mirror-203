from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()

VERSION = '1.2.1'
DESCRIPTION = 'Reading and writing to the memory of any process.'

# Setting up
setup(
	name="UserReadWriteMemory",
	url="https://github.com/User00092/UserReadWriteMemory/tree/1.2.1",
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
	]
)
