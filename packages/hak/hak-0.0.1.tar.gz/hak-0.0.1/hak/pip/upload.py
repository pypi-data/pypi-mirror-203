from subprocess import run as sprun
from hak.fake.subprocess.run import f as fake_sprun
from hak.directory.make import f as mkdirine
from hak.directory.remove import f as rmdirie
from hak.file.load import f as load

_dir = '../start_upload'

def up(): return mkdirine(_dir)

def dn(): return rmdirie(_dir)

_username = load('username.secret')
_password = load('password.secret')

def f(sprun=sprun, cwd='.', capture_output=True):
  return sprun(
    ['twine', 'upload', 'dist/*', '-u', _username, '-p', _password],
    cwd=cwd,
    capture_output=capture_output
  )

def t():
  up()
  z = f(fake_sprun, cwd=_dir)
  result = all([
    _password in z.args,
    _username in z.args,
    'twine' in z.args,
    'upload' in z.args,
    'dist/*' in z.args,
    '-u' in z.args,
    '-p' in z.args,
    z.returncode == 0,
    'Uploading distributions to https://upload.pypi.org' in z.stdout.decode()
  ])
  dn()
  return result
