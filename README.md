# ansible-azure-automation

## Automated Azure VM Provisioning with Post-Deployment Configuration

End-to-end solution that:

- Uses Terraform to provision the underlying Azure infrastructure (e.g., resource groups, virtual networks, subnets).
- Uses Ansible (with the azure.azcollection modules) to provision one or more Azure VMs with specific configurations (size, OS, networking, etc.).
- Uses a Python dynamic inventory script that calls the Azure CLI (or Azure SDK) to generate a live inventory of the provisioned VMs.
- Uses Ansible playbooks to perform post-deployment configuration (such as installing and configuring Nginx and Docker).
- Integrates the above steps into a CI/CD pipeline.
