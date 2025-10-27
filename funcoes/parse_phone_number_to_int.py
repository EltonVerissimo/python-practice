def parse_phone_number_to_int(phone_list:list):
    phone_list_to_int = [int(x) for x in phone_list]
    return phone_list_to_int

def validate_if_phone_list_is_int(phone_list:list):
    all_elements_is_int = all(isinstance(item, int) for item in phone_list)
    return all_elements_is_int

phone_list = ["11987654321", "21912345678", "31987654321", "11911223344"]

int_phone_list = parse_phone_number_to_int(phone_list)

if validate_if_phone_list_is_int(int_phone_list):
    print("Todos os números foram convertidos corretamente!")
else:
    print("Houve um erro na conversão dos números!")