import time
import pyperclip

data = pyperclip.paste() + " (PASTE (Strg+v)) "
print(data)

small_lst = [rf"\x0{number}" for number in range(0, 10)]
big_lst = [rf"\x{number}" for number in range(10, 101)]
all = small_lst+big_lst
new_key = ""
try:
    ordinal = ord(new_key)

except TypeError:
    pass

print(ordinal)

if r"\x" in rf"{new_key}":
    print("ja")