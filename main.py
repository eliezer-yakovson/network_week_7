
from core.output_string import format_cidr_mask,format_num_hosts,format_broadcast_address, format_classful_status, format_input_ip, format_network_address, format_subnet_mask
from core.utils import class_type, network_investigation, validate_mask


def main():
    ip_input = input("Enter IP address: ").strip()
    mask_input = input("Enter Subnet Mask: ").strip()

    if not validate_mask(mask_input):
        print("Invalid subnet mask.")
        return

    network_info = network_investigation(ip_input, mask_input)

    print(format_input_ip(ip_input))
    print(format_subnet_mask(mask_input))
    print(format_classful_status(network_info["type_class"]))
    print(format_network_address(network_info["network_address"]))
    print(format_broadcast_address(network_info["broadcast_address"]))
    print(format_num_hosts(network_info["hosts"]))
    print(format_cidr_mask(network_info["cidr"]))
   

if __name__ == "__main__":
    main()