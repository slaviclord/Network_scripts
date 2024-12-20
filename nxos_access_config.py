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

# Main script to prompt user input and generate NX-OS configuration
if __name__ == "__main__":
    # Prompt the user for the interface name, port description, and VLAN
    interface_name = input("Enter the interface name (e.g., Ethernet1/1): ")
    port_description = input("Enter the switch port description: ")
    vlan_number = input("Enter the VLAN number: ")

    # Generate the switch port configuration for NX-OS
    config = generate_nxos_switch_port_config(interface_name, port_description, vlan_number)

    # Print the generated configuration
    print("\nGenerated NX-OS switch port configuration:")
    print(config)
