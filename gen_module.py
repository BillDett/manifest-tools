import sys

# Generate the quay-builder-go-mod.txt fragments from modules.txt
# Run via:
# $ cat $OPERATOR_SRC/vendor/module.txt | python3 gen_module.py > quay-3.2-module

# Repeat for all Quay operators

'''
# go.uber.org/multierr v1.1.0

produces...

quay:master:quay-operator/go-module-go.uber.org-multierr-v1.1.0

'''
# Take a release tag if you don't want 'master'
if len(sys.argv) > 1:
    tag = sys.argv[1]
else:
    tag = 'master'

print('')
for line in sys.stdin:
    if line.startswith('#'):
        line = line[1:].strip()      # clean up leading '#' and whitespace
        t = line.split(' ')
        pkg = t[0]
        version = t[1]
        print('quay:' + tag + ':quay-operator/go-module-' + pkg + '-' + version)