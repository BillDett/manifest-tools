import sys
from urllib.parse import urlparse

# Generate the quay-yarn.txt fragments from yarn.lock
# Run via:
# $ grep resolved ~/dev/quay/yarn.lock | python3 gen_yarn.py > quay-3.1-yarn

'''
$ grep resolved $QUAY_SRC/yarn.lock
  resolved "https://registry.yarnpkg.com/yeast/-/yeast-0.1.2.tgz#008e06d8094320c372dbc2f8ed76a0ca6c8ac419"
  resolved "https://registry.yarnpkg.com/yn/-/yn-1.2.0.tgz#d237a4c533f279b2b89d3acac2db4b8c795e4a63"
  resolved "https://registry.yarnpkg.com/yn/-/yn-2.0.0.tgz#e5adabc8acf408f6385fc76495684c88e6af689a"
  resolved "https://registry.yarnpkg.com/zeroclipboard/-/zeroclipboard-2.3.0.tgz#592ebd833a4308688b0739697d3dbf989002c9af"

should produce something like:

quay:3.0:quay/yarnpkg-yargs-parser-4.2.1.tgz

'''
if len(sys.argv) > 1:
    tag = sys.argv[1]
else:
    print('Error: must specify Quay release tag (e.g. 3.2)')
    exit()

print('')
for line in sys.stdin:
    t = line.split()
    u = urlparse(str(t[1]).replace('"',''))
    p = u.path.split('/')
    pkg = p[len(p)-1]
    prefix = 'nodejs'
    print('quay:' + tag + ':quay/' + prefix + '-' + pkg)
