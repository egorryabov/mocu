v1 = {
    'value': [1, 2, 3]
}

v2 = {
    'value': [4, 5, 6]
}

combined = {
    'value': v1['value'] + v2['value']
}

print(combined['value'])  # Output: [1, 2, 3, 4, 5, 6]
