from subprocess import run as sprun
from hak.fake.subprocess.run import f as fake_sprun
from hak.directory.make import f as mkdirine
from hak.directory.remove import f as rmdirie
from hak.file.load import f as load
from hak.string.print_and_return_false import f as pf

_dir = '../start_upload'

up = lambda: mkdirine(_dir)

dn = lambda: rmdirie(_dir)

_username = load('username.secret').split('\n')[0]
_password = load('password.secret').split('\n')[0]

def f(sprun=sprun, cwd='.', capture_output=True):
  return sprun(
    ['twine', 'upload', 'dist/*', '-u', _username, '-p', _password],
    cwd=cwd,
    capture_output=capture_output
  )

def t():
  up()
  z = f(fake_sprun, cwd=_dir)
  dn()
  if not _password in z.args: return pf([
    "_password in z.args",
    f'z.args: {z.args}'
  ])
  if not _username in z.args: return pf("_username in z.args")
  if not 'twine' in z.args: return pf("'twine' in z.args")
  if not 'upload' in z.args: return pf("'upload' in z.args")
  if not 'dist/*' in z.args: return pf("'dist/*' in z.args")
  if not '-u' in z.args: return pf("'-u' in z.args")
  if not '-p' in z.args: return pf("'-p' in z.args")
  if not z.returncode == 0: return pf("z.returncode == 0")
  if not 'distributions to https://upload.pypi.org' in z.stdout.decode():
    return pf("'distributions to https://upload.pypi.org' in z.stdout.decode()")
  return True
