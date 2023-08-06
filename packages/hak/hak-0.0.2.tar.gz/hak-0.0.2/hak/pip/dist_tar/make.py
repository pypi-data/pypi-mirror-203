from subprocess import run as sprun
from hak.string.colour.primary import f as primary
from hak.directory.remove import f as rmdir
from hak.directory.make import f as mkdir
from hak.file.save import f as save
from hak.file.zip.extract import f as extract

_root = '../temp'
base = './hak/system/git/commit'
setup_filepath = _root + '/setup.py'

f = lambda cwd='.': sprun(
  ['python3', 'setup.py', 'sdist'], cwd=cwd, capture_output=True
)

def up():
  mkdir(_root)
  mkdir(_root+'/hak')
  save(_root+'/hak/__init__.py', '')
  extract(f'{base}/added_file_pre_commit.zip', '..')
  save(setup_filepath, "\n".join([
    'from setuptools import setup',
    'from pathlib import Path',
    '',
    "setup(",
    "  name='hak',",
    "  version='0.0.0',",
    "  description='Function Test Pair Toolbox',",
    "  long_description=Path('./README.md').read_text(),",
    "  long_description_content_type='text/markdown',",
    "  author='@JohnRForbes',",
    "  author_email='john.robert.forbes@gmail.com',",
    "  url='https://github.com/JohnForbes/hak',",
    "  packages=['hak'],",
    "  classifiers=[",
    "    'Programming Language :: Python :: 3',",
    "    'License :: OSI Approved :: MIT License',",
    "    'Operating System :: OS Independent',",
    "  ],",
    '  python_requires=">=3.7",',
    "  include_package_data=True,",
    ")",
  ]))

dn = lambda: rmdir(_root)

def t():
  up()
  z = f(_root)
  dn()
  return all([
    z.args == ['python3', 'setup.py', 'sdist'],
    z.returncode == 0,
    z.stdout.decode("utf-8") == '\n'.join([
      "running sdist",
      "running egg_info",
      "creating hak.egg-info",
      "writing hak.egg-info/PKG-INFO",
      "writing dependency_links to hak.egg-info/dependency_links.txt",
      "writing top-level names to hak.egg-info/top_level.txt",
      "writing manifest file 'hak.egg-info/SOURCES.txt'",
      "reading manifest file 'hak.egg-info/SOURCES.txt'",
      "writing manifest file 'hak.egg-info/SOURCES.txt'",
      "running check",
      "creating hak-0.0.0",
      "creating hak-0.0.0/hak",
      "creating hak-0.0.0/hak.egg-info",
      "copying files to hak-0.0.0...",
      "copying README.md -> hak-0.0.0",
      "copying setup.py -> hak-0.0.0",
      "copying hak/__init__.py -> hak-0.0.0/hak",
      "copying hak.egg-info/PKG-INFO -> hak-0.0.0/hak.egg-info",
      "copying hak.egg-info/SOURCES.txt -> hak-0.0.0/hak.egg-info",
      "copying hak.egg-info/dependency_links.txt -> hak-0.0.0/hak.egg-info",
      "copying hak.egg-info/top_level.txt -> hak-0.0.0/hak.egg-info",
      "Writing hak-0.0.0/setup.cfg",
      "creating dist",
      "Creating tar archive",
      "removing 'hak-0.0.0' (and everything under it)",
      "",
    ]),
    z.stderr.decode("utf-8") == ''
  ])
