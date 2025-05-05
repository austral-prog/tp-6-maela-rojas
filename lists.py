def remove_elements(list_to_remove_elements):
    nueva_lista = list_to_remove_elements[:]
    if len(nueva_lista) > 5:
        del nueva_lista[5]
    if len(nueva_lista) > 4:
        del nueva_lista[4]
    if len(nueva_lista) > 0:
        del nueva_lista[0]
    return nueva_lista


def add_elements(list_to_add_elements):
    nueva_lista = list_to_add_elements[:]
    nueva_lista.insert(0, 'Pink')
    nueva_lista.append('Yellow')
    return nueva_lista


def is_empty(list_to_check):
    return not list_to_check

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
        return list_to_compare1[2] == list_to_compare2[2]
    return False


def list_of_lists(list_of_lists_to_modify):
    modified_list = []
    sublista1 = list_of_lists_to_modify[0][:2]
    modified_list.append(sublista1)
    sublista2 = list_of_lists_to_modify[1][1:4]
    modified_list.append(sublista2)
    sublista3 = list_of_lists_to_modify[2][-2:]
    modified_list.append(sublista3)
    return modified_list
