# Function to generate switch port configuration for Cisco Nexus (NX-OS)
def generate_nxos_switch_port_config(interface_name, description, vlan):
    return f"""interface {interface_name}
 description {description}
 switchport mode access
 switchport access vlan {vlan}
 spanning-tree port type edge
 spanning-tree bpduguard enable
"""

# Function to generate switch port configuration for Cisco Catalyst (IOS)
def generate_catalyst_switch_port_config(interface_name, description, vlan):
    return f"""interface {interface_name}
 description {description}
 switchport mode access
 switchport access vlan {vlan}
 spanning-tree portfast
 spanning-tree bpduguard enable
"""

# Function to collect details and generate configuration for multiple interfaces
def generate_configs_for_multiple_interfaces(switch_type):
    number_of_interfaces = int(input("Enter the number of interfaces you wish to configure: "))
    configs = []

    for i in range(number_of_interfaces):
        print(f"\nConfiguring interface #{i+1}")
        interface_name = input("Enter the interface name (e.g., Ethernet1/1 for NX-OS or FastEthernet0/1 for Catalyst): ")
        port_description = input("Enter the switch port description: ")
        vlan_number = input("Enter the VLAN number: ")
        
        if switch_type == 'nxos':
            config = generate_nxos_switch_port_config(interface_name, port_description, vlan_number)
        elif switch_type == 'catalyst':
            config = generate_catalyst_switch_port_config(interface_name, port_description, vlan_number)
        else:
            print("Invalid switch type selected.")
            return
        
        configs.append(config)

    return configs

# Main script
if __name__ == "__main__":
    switch_type = input("Enter the switch type ('nxos' or 'catalyst'): ").lower()
    
    # Generate configurations for multiple interfaces
    all_configs = generate_configs_for_multiple_interfaces(switch_type)

    # Print all generated configurations
    print("\nGenerated switch port configurations:")
    for config in all_configs:
        print(config)
