import sys

# Generate the quay-requirements.txt fragments from requirements.txt
# Run via:
# $ cat requirements.txt | python3 gen_requirements.py > quay-3.2-rqmts

'''
aiowsgi==0.7

produces...

quay:3.2:quay/python-aiowsgi-0.6.pipfile

'''
if len(sys.argv) > 1:
    tag = sys.argv[1]
else:
    print('Error: must specify Quay release tag (e.g. 3.2)')
    exit()

print('')
for line in sys.stdin:
    t = line.split('==')
    if not t[0].startswith('#') and not t[0].startswith('-'):
        pkg = t[0]
        version = t[1].strip()
        print('quay:' + tag + ':quay/python-' + pkg + '-' + version)