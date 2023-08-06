# real48

That package allows convert data given in `real48` proprietary format to well-formed `float` number.
How to use
```Python
import real48

real48_data = b'\x00\x00\x00\x00\x00\x00'
result = real48.real48_to_float(real48_data)
print(result)
```

Output:
<code>
0.0
</code>