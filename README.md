# Enasis Network Ansible Infrastructure Collection

> :warning: This project has not released its first major version.

Project for executing the Ansible playbooks for system automation.

## Playbooks and roles within project
- `sambadc` Operate and manage Windows domain with Samba.
- `sambafs` Configure and manage file shares using Samba.
- `bind` Install and configure BIND for DNS resolution.
- `httpd` Install and configure Apache2 for web serving.
- `routing` Configure routing within operating system.

`bird` and `openvpn` will not be required returning to OpenBSD.

## Quick start for local development
Start by cloning the repository to your local machine.
```
git clone https://github.com/enasisnetwork/ansible-domain.git
```
Set up the Python virtual environments expected by the Makefile.
```
make -s venv-create
```

### Execute the linters and tests
The comprehensive approach is to use the `check` recipe. This will stop on
any failure that is encountered.
```
make -s check
```
However you can run the linters in a non-blocking mode.
```
make -s linters-pass
```

## Version management
> :warning: Ensure that no changes are pending.

1. Rebuild the environment.
   ```
   make -s check-revenv
   ```

1. Update the [galaxy.yml](galaxy.yml) file.

1. Push to the `main` branch.

1. Create [repository](https://github.com/enasisnetwork/ansible-domain) release.

1. Build the Galaxy package.<br>Be sure no uncommited files in tree.
   ```
   make -s galaxy-build
   ```

1. Upload Galaxy package to Ansible servers.
   ```
   make -s galaxy-upload
   ```
