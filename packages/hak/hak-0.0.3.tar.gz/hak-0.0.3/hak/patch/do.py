from hak.pip.version.get import f as get_pip_version
from hak.pip.version.get import t as t_get_pip_version

from hak.setup.cfg.update import f as update_setup_cfg
from hak.setup.cfg.update import t as t_update_setup_cfg

from hak.setup.py.update import f as update_setup_py
from hak.setup.py.update import t as t_update_setup_py

from hak.pip.dist_tar.make import f as generate_new_dist_tar
from hak.pip.dist_tar.make import t as t_generate_new_dist_tar

from hak.system.git.commit.run import f as add_to_git
from hak.system.git.commit.run import t as t_add_to_git

from hak.pip.upload import f as start_upload
from hak.pip.upload import t as t_start_upload

from hak.directory.remove import f as rmdirie

from hak.file.save import f as save

from hak.pip.dist_tar.remove import f as remove_dist_tar
from hak.pip.dist_tar.remove import t as t_remove_dist_tar

from subprocess import run as sprun
from hak.string.print_and_return_false import f as pf

from hak.directory.make import f as mkdir

temp_root = '.'
temp_dir_path = f'{temp_root}/hak_test'
temp_cfg_path = f'{temp_dir_path}/setup.cfg'
temp_py_path = f'{temp_dir_path}/setup.py'

def up():
  mkdir(temp_dir_path)

  _ = sprun(
    ['git', 'clone', 'git@gitlab.com:zereiji/hak_test.git'],
    cwd=temp_root,
    capture_output=True
  )

  save(temp_cfg_path, "\n".join([
    "[metadata]",
    "name = hak",
    "version = 1.2.3",
    "author = John Forbes",
    "author_email = john.robert.forbes@gmail.com",
    "description = Function Test Pair Toolbox",
    "long_description = file: README.md",
    "long_description_content_type = text/markdown",
    "url = https://github.com/JohnForbes/hak",
    "license_files=LICENSE",
    "classifiers = ",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    "",
    "[options]",
    "packages = find:",
    "python_requires = >=3.7",
    "include_package_data = True",
  ]))

  save(temp_py_path, "\n".join([
    "from setuptools import setup",
    "from pathlib import Path",
    "long_description = Path('./README.md').read_text()",
    "",
    "setup(",
    "  name='hak',",
    "  version='1.2.4',",
    "  license='MIT',",
    "  description='Function Test Pair Toolbox',",
    "  long_description=long_description,",
    "  long_description_content_type='text/markdown',",
    "  author='@JohnRForbes',",
    "  author_email='john.robert.forbes@gmail.com',",
    "  url='https://github.com/JohnForbes/hak',",
    "  packages=['hak'],",
    "  keywords='hak',",
    "  install_requires=[],",
    ")",
  ]))

dn = lambda: rmdirie(temp_dir_path)

def f(x):
  z = {}
  z['v'] = x['v'] if 'v' in x else None
  z['root'] = x['root'] if 'root' in x else '.'
  z['cfg_path'] = f'{z["root"]}/setup.cfg'
  z['py_path'] = f'{z["root"]}/setup.py'

  z['v'] = z['v'] or get_pip_version('hak')
  z['v']['patch'] += 1

  update_setup_cfg(z)
  update_setup_py(z)
  remove_dist_tar(x)
  generate_new_dist_tar(x)
  # add_to_git(cwd=_root, cap_out=True)
  # upload_result = start_upload()
  z['upload_result'] = True

  return z
  # return {
  #   'v': v,
  #   'cfg_path': cfg_path,
  #   'py_path': py_path,
  #   'upload_result': upload_result
  # } 

def t():
  x = {
    'v': {'major': 1, 'minor': 2, 'patch': 3},
    'root': temp_dir_path
  }
  y = {
    'v': {'major': 1, 'minor': 2, 'patch': 4},
    'cfg_path': './hak_test/setup.cfg',
    'py_path': './hak_test/setup.py',
    'upload_result': True,
    'root': temp_dir_path
  }
  up()
  z = f(x)
  dn()

  if z is None: return pf([f"z is None", f'x: {x}', f'y: {y}', f'z: {z}'])

  if y != z:
    print('y != z')
    for k in (set(y.keys()) | set(z.keys())):
      if not y[k] == z[k]:
        return pf([
          f"y[{k}] == z[{k}]",
          f'y[{k}]: {y[k]}',
          f'z[{k}]: {z[k]}',
        ])
    
    return False

  if y['v'] != z['v']:
    return pf([f"y['v'] != z['v']", f'x: {x}', f'y: {y}', f'z: {z}'])
  
  for k in (set(y.keys()) | set(z.keys())):
    if not y[k] == z[k]:
      return pf([
        f"y[{k}] == z[{k}]",
        f'x: {x}',
        f'y: {y}',
        f'z: {z}'
      ])

  if not t_get_pip_version():
    return pf([f"t_get_pip_version()", f'x: {x}', f'y: {y}', f'z: {z}'])

  if not t_update_setup_cfg():
    return pf([f"t_update_setup_cfg()", f'x: {x}', f'y: {y}', f'z: {z}'])

  if not t_update_setup_py():
    return pf([f"t_update_setup_py()", f'x: {x}', f'y: {y}', f'z: {z}'])

  if not t_remove_dist_tar():
    return pf([f"t_remove_dist_tar()", f'x: {x}', f'y: {y}', f'z: {z}'])

  if not t_generate_new_dist_tar():
    print(f"t_generate_new_dist_tar()")
    print(f'x: {x}')
    for k in (set(y.keys()) | set(z.keys())):
      if y[k] != z[k]:
        print('\n'.join([f'y[{k}]: {y[{k}]}', f'z[{k}]: {z[{k}]}', '']))
    return False

  if not t_add_to_git():
    return pf([f"t_add_to_git()", f'x: {x}', f'y: {y}', f'z: {z}'])

  if not t_start_upload():
    return pf([f"t_start_upload()", f'x: {x}', f'y: {y}', f'z: {z}'])

  # print(f'x: {x}')
  # print(f'y: {y}')
  # print(f'z: {z}')

  return True
