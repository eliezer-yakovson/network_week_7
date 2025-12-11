
from core.utils import class_type, validate_mask


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
   

if __name__ == "__main__":
    main()