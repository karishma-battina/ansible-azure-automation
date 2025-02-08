#main.tf
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "vm-automation-rg"
  location = "East US"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "vm-vnet"
  address_space       = ["10.0.0.0/16"]
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
}

# Add subnet, public IP, and NIC resources