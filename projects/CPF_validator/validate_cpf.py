def validate_cpf(cpf_number:int):
    if len(str(cpf_number)) == 11:
        return True
    else:
        return False