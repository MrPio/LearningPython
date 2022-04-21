import decimal

numbers = [123, 58, 5, 989, 156]
print(max(numbers))

width = 20
precision = 9
value = decimal.Decimal("12.3456751482185148514895914859196589595295295362953956296529853")
print(f"result: {value:{width}.{2}}")
