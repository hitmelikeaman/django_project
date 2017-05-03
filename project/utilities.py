import decimal

COEFFICIENT_OF_PRIORITY = 1
COEFFICIENT_OF_MINORITY = 0.01
COEFFICIENTS_FL = [0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07]


def parse_for_checked(request):
    checked = {}

    for k, v in request.POST.items():
        if k != 'csrfmiddlewaretoken':
            checked[k] = v
    checked.pop('action')
    return [int(x) for x in checked.keys()]


def apply_priorities(vals_list, checked):
    list_of_lists = [list(lst) for lst in vals_list]
    checked_shifted = [x+2 for x in checked]
    for lst in list_of_lists:
        for elem in range(len(lst)):
            if type(lst[elem]) != str:
                if elem in checked_shifted:
                    lst[elem] *= decimal.Decimal(COEFFICIENT_OF_PRIORITY)
                else:
                    lst[elem] *= decimal.Decimal(COEFFICIENT_OF_MINORITY)

    for x in range(13):
        for lst in list_of_lists:
            lst[x+2] *= decimal.Decimal(COEFFICIENTS_FL[x])
    return list_of_lists


def form_result(prioritised_vals_list):

    final_list_of_lists = []

    for lst in prioritised_vals_list:
        final_coef = sum(lst[2:])
        final_info = (final_coef, lst[1])
        final_list_of_lists.append(final_info)

    final_list_of_lists.sort(key=lambda x: x[0], reverse=True)
    print(final_list_of_lists)
    return final_list_of_lists
