# manifest-tools - scripts to help generate Quay manifests

For each Quay release, a set of manifest files needs to be generated.  These scripts assist with converting the Quay dependency config into the necessary manifest fragments.  Run these commands shortly before creating Quay release candidate images for QE testing.

## Generating manifests

### clair-jwt-Dockerfile.txt
Run the clair-jwt container and verify the installed package versions match manifest file:

    $ podman run --entrypoint "/bin/bash" -it quay-clair-jwt:latest
    [root@160b88d792f0 clair]# rpm -qa | grep redhat-release-server
    redhat-release-server-7.7-10.el7.x86_64


### clair-Dockerfile.txt
Run the clair container and verify the installed package versions match manifest file:

    $ podman run --entrypoint "/bin/bash" -it clair:latest
    [root@160b88d792f0 clair]# rpm -qa | grep redhat-release
    redhat-release-8.1-3.3.el8.x86_64


### claircore-go-mod.txt

    $ cd claircore
    $ go mod vendor
    $ cat vendor/modules.txt | python3 ../manifest-tools/gen_module.py 3.3 > claircore-module
    $ cat claircore-module >> ../quay-manifests/rhquay/claircore-go-mod.txt


### quay-builder-go-mod.txt

    $ cd quay-builders
    $ go mod vendor
    $ cat vendor/modules.txt | python3 ../manifest-tools/gen_module.py 3.3 > quay-builder-module
    $ cat quay-builder-module >> ../quay-manifests/rhquay/quay-builder-go-mod.txt

### quay-builder-Dockerfile.txt
Run the quay-builder container and verify the installed package versions match manifest file:

    $ podman run --entrypoint "/bin/bash" -it quay-quay-builder:latest 
    [root@2f5fd2781a0a quay-builder]# 
    [root@2f5fd2781a0a quay-builder]# rpm -qa | grep redhat-release-server
    redhat-release-server-7.7-10.el7.x86_64

...and so forth...

### quay-Dockerfile.txt

Run the Quay container and verify the installed package versions match manifest file:

    $ podman run -it quay:latest bash 
       __   __
      /  \ /  \     ______   _    _     __   __   __
     / /\ / /\ \   /  __  \ | |  | |   /  \  \ \ / /
    / /  / /  \ \  | |  | | | |  | |  / /\ \  \   /
    \ \  \ \  / /  | |__| | | |__| | / ____ \  | |
     \ \/ \ \/ /   \_  ___/  \____/ /_/    \_\ |_|
      \__/ \__/      \ \__
                      \___\ by Red Hat

     Build, Store, and Distribute your Containers


    Running 'bash'
    [root@526d73b71153 quay-registry]# rpm -qa | grep python27-1.1-26
    python27-1.1-26.1.el7.x86_64
    root@526d73b71153 quay-registry]# rpm -qa | grep python27-python-pip
    python27-python-pip-8.1.2-3.el7.noarch

...and so forth...

### quay-operator-go-mod.txt

    $ cd quay-operator
    $ go mod vendor
    $ cat vendor/modules.txt | python3 ../manifest-tools/gen_module.py 3.3 > quay-operator-module
    $ cat quay-operator-module >> ../quay-manifests/rhquay/quay-operator-go-mod.txt


### container-security-operator-go-mod.txt

    $ cd container-security-operator
    $ go mod vendor
    $ cat vendor/modules.txt | python3 ../manifest-tools/gen_module.py 3.3 > cso-module
    $ cat cso-module >> ../quay-manifests/rhquay/container-security-operator-go-mod.txt


### quay-bridge-operator-go-mod.txt

    $ cd quay-bridge-operator
    $ go mod vendor
    $ cat vendor/modules.txt | python3 ../manifest-tools/gen_module.py 3.3 > qbo-module
    $ cat qbo-module >> ../quay-manifests/rhquay/quay-bridge-operator-go-mod.txt


### quay-requirements.txt

    $ cd quay
    $ cat requirements.txt | python3 ../manifest-tools/gen_requirements.py 3.3 > quay-rqmts
    $ cat quay-rqmts >> ../quay-manifests/rhquay/quay-requirements.txt


### quay-yarn.txt

    $ cd quay
    $ grep resolved yarn.lock | python3 ../manifest-tools/gen_yarn.py 3.3 > quay-yarn
    $ cat quay-yarn >> ../quay-manifests/rhquay/quay-yarn.txt


### Other manifest files
Typically you can just manually compare them against the relevant Quay side of things rather than re-generate as the number of lines is fairly small.
