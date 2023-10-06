import py_compile
import dis

with open('hidden_4.pyc', 'rb') as compiled_file:
    code = compiled_file.read()

names = []

for instruction in dis.get_instructions(code):
    if instruction.opname == 'LOAD_NAME':
        name = instruction.argval
        if not name.startswith('__'):
            names.append(name)

for name in sorted(set(names)):
    print(name)
