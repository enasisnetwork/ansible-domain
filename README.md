# Enasis Network Ansible Infrastructure Collection

> This project has not released its first major version.

> This collection is only a placeholder for the moment.

Ansible content for installing and configuring the infrastructure.

Check out this collection on
[Ansible Galaxy](https://galaxy.ansible.com/ui/repo/published/enasisnetwork/domain)
for more information.

<a href="https://galaxy.ansible.com/ui/repo/published/enasisnetwork/domain"><img src="https://enasisnetwork.github.io/ansible-domain/badges/galaxy.png"></a><br>
<a href="https://enasisnetwork.github.io/ansible-domain/validate/flake8.txt"><img src="https://enasisnetwork.github.io/ansible-domain/badges/flake8.png"></a><br>
<a href="https://enasisnetwork.github.io/ansible-domain/validate/pylint.txt"><img src="https://enasisnetwork.github.io/ansible-domain/badges/pylint.png"></a><br>
<a href="https://enasisnetwork.github.io/ansible-domain/validate/ruff.txt"><img src="https://enasisnetwork.github.io/ansible-domain/badges/ruff.png"></a><br>
<a href="https://enasisnetwork.github.io/ansible-domain/validate/mypy.txt"><img src="https://enasisnetwork.github.io/ansible-domain/badges/mypy.png"></a><br>
<a href="https://enasisnetwork.github.io/ansible-domain/validate/yamllint.txt"><img src="https://enasisnetwork.github.io/ansible-domain/badges/yamllint.png"></a><br>
<a href="https://enasisnetwork.github.io/ansible-domain/validate/ansblint.txt"><img src="https://enasisnetwork.github.io/ansible-domain/badges/ansblint.png"></a><br>
<a href="https://enasisnetwork.github.io/ansible-domain/validate/pytest.txt"><img src="https://enasisnetwork.github.io/ansible-domain/badges/pytest.png"></a><br>
<a href="https://enasisnetwork.github.io/ansible-domain/validate/coverage.txt"><img src="https://enasisnetwork.github.io/ansible-domain/badges/coverage.png"></a><br>

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
