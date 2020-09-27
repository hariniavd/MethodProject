""" Module to remove nested array and append values to a single list.
"""


def remove_nested_loop(nested_list):
    """ Takes a nested list as a argument, and appends the values to single list.
    """
    final_list = []

    if not isinstance(nested_list, list):
        return False

    for value in nested_list:
        if isinstance(value, list):
            final_list.extend(remove_nested_loop(value))
        else:
            final_list.append(value)

    return final_list


# Example
# nested_list = [1, 2, [3, 'jb', [5, [6, 8, 8]], 'tv', 5, [7]], 7, 8, [9, [10, 11, [5, 8, [8, 6]]]]]
# final_list = remove_nested_loop(nested_list)
# print(final_list)
