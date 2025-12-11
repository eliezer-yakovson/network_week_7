def validate_ip(ip):
    try:
        octata_1, octata_2, octata_3, octata_4 = ip.split('.')
        if  0 <= int(octata_1) <= 255 and  0 <= int(octata_2) <= 255 and  0 <= int(octata_3) <= 255 and  0 <= int(octata_4) <= 255:
            return True
        return False
    except:
        print("There is a problem with the IP address.")

def validate_mask(mask):
    arr_masc = mask.split('.')
    if len(arr_masc) < 4:
        return False
    if not all(0<= int(octata) <= 255 for octata in arr_masc):
        return False
    arr_mask_bin = [decimal_to_binary(int(octata))for octata in arr_masc]
    mask_bin = ''.join(arr_mask_bin)
    found_zero = False
    for bit in mask_bin:
        if bit == '0':
            found_zero = True
        elif bit == '1' and found_zero:
            return False
    return True

def network_investigation(ip,mask):
    dict_network = {"type_class":"","network_address":"","broadcast_address":"","hosts":"","cidr":""}
    arr_ip = ip.split('.')
    dict_type = {'a':1,'b':2,'c':3}
    dict_dicr = {'a':8,'b':16,'c':24}
    if type(class_type(mask)) is str:
        type_cl = class_type(mask)
        dict_network["type_class"] = type_cl
        net_arr_ip = arr_ip.copy()
        net_arr_ip[dict_type[type_cl]]=0
        dict_network["network_address"] = '.'.join(net_arr_ip)
        bro_arr_ip = arr_ip.copy()
        bro_arr_ip[-1]=255
        dict_network["broadcast_address"] = bro_arr_ip
        dict_network["hosts"] = 255
        dict_network["cidr"] =  dict_dicr[type_cl]
    else:
        dict_network["type_class"] = 'classless'
        octata_index , hosts_number = class_type(mask)
        net_arr_ip = arr_ip.copy()
        net_arr_ip[octata_index -1] = str(int(arr_ip[octata_index -1])  & (256 - hosts_number))
        for i in range(octata_index,4):
            net_arr_ip[i] = '0'
        dict_network["network_address"] = '.'.join(net_arr_ip)
        bro_arr_ip = arr_ip.copy()
        bro_arr_ip[octata_index -1] = str(int(arr_ip[octata_index -1])  | (hosts_number -1))
        for i in range(octata_index,4):
            bro_arr_ip[i] = '255'
        dict_network["broadcast_address"] = '.'.join(bro_arr_ip)
        dict_network["hosts"] = hosts_number -2
        dict_network["cidr"] = Converting_mask_address_to_abinary_string(mask).count('1')
    return dict_network

     


        



#במידה וזה קלאספול זה יחזיר את סוג הקלאס, אחרת זה יחזיר טפל של מיקום האוקטטה ומספר המארחים
def class_type(mask):
    dict_type = {1:'a',2:'b',3:'c'}
    b_mask = Converting_mask_address_to_abinary_string(mask)
    number_ones = b_mask.count('1')
    class_type = dict_type[number_ones // 8 ] 
    hosts_number = pow(2, 8 - (number_ones % 8))
    if number_ones % 8 == 0:
        return class_type
    else:
        return((number_ones // 8)+1,hosts_number )



def Converting_mask_address_to_abinary_string(mask):
    arr_masc = mask.split('.')
    arr_mask_bin = [decimal_to_binary(int(octata))for octata in arr_masc]
    mask_bin = ''.join(arr_mask_bin)
    return mask_bin

def decimal_to_binary(decimal_num):    
    binary = bin(decimal_num)[2:]  
    return binary.zfill(8) 
