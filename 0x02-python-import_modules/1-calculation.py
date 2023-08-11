#!/usr/bin/python3
import calculator_1 as calc
a = 10
b = 5
sum_result = calc.add(a, b)
diff_result = calc.sub(a, b)
product_result = calc.mul(a, b)
div_result = calc.div(a, b)

print("{:d} + {:d} = {:d}".format(a, b, sum_result))
print("{:d} - {:d} = {:d}".format(a, b, diff_result))
print("{:d} * {:d} = {:d}".format(a, b, product_result))
print("{:d} / {:d} = {:d}".format(a, b, div_result))
