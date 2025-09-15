# Description
Provides installation and configuration tasks for the BIND services.

# Using this role with tags
- `overview` Information about the role operations
- `install` Install the service on inventory host
- `configure` Template the service configuration file
- `state-started` Control the state of package service
- `state-restarted` Control the state of package service
- `state-stopped` Control the state of package service

# Example with role and tags
```yaml
- hosts: ...
  tasks:

    - name: Information about the role operations
      import_role:
        name: enasisnetwork.domain.named
      tags: overview

    - name: Install the service on inventory host
      import_role:
        name: enasisnetwork.domain.named
      tags: install
```

# Example from command line
*Information about the role operations*
```
ansible-playbook \
  ...
  --tags "overview" \
  enasisnetwork.domain.named
```

## Variables for Ansible inventory
- `named_forward` Default forwarders for recursion
- `named_access` Horizon restriction access list
- `named_horizon` Configuraiton for split horizon

Check out the parameter model on
[GitHub](https://github.com/enasisnetwork/ansible-domain/blob/main/collection/plugins/action/named/params.py)
for more information.
