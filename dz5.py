from colorama import init
import colorama
import inspect

init()

text = "_"
repeated_text = text * 100
print(repeated_text)

def inspect_colorama():
    print("Інспекція бібліотеки colorama:")

    attributes = dir(colorama)

    for attr in attributes:

        obj = getattr(colorama, attr)

        if inspect.isfunction(obj):
            print(f"Функція: {attr}")

        elif inspect.isclass(obj):
            print(f"Клас: {attr}")

        else:
            print(f"Атрибут/Константа: {attr}")

inspect_colorama()

text = "_"
repeated_text = text * 100
print(repeated_text)

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))
print(inspect.getmodule(colorama))
print(inspect.getmodule(list))

module_functions = dir(colorama)
print(dir(colorama))






