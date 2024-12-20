# Function to generate switch port configuration for Cisco Nexus (NX-OS)
def generate_nxos_switch_port_config(interface_name, description, vlan):
    config_template = f"""interface {interface_name}
 description {description}
 switchport mode access
 switchport access vlan {vlan}
 spanning-tree port type edge
 spanning-tree bpduguard enable
 no shut
"""
    return config_template

# Function to collect details and generate configuration for multiple interfaces
def generate_configs_for_multiple_interfaces():
    number_of_interfaces = int(input("Enter the number of interfaces you wish to configure: "))
    configs = []

    for i in range(number_of_interfaces):
        print(f"\nConfiguring interface #{i+1}")
        interface_name = input("Enter the interface name (e.g., Ethernet1/1): ")
        port_description = input("Enter the switch port description: ")
        vlan_number = input("Enter the VLAN number: ")
        config = generate_nxos_switch_port_config(interface_name, port_description, vlan_number)
        configs.append(config)

    return configs

# Main script
if __name__ == "__main__":
    # Generate configurations for multiple interfaces
    all_configs = generate_configs_for_multiple_interfaces()

    # Print all generated configurations
    print("\nGenerated NX-OS switch port configurations:")
    for config in all_configs:
        print(config)
