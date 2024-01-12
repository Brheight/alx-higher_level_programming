import py_compile
import dis
if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as compiled_file:
        code = compiled_file.read()

    index = 0
    names = set()
    print('first', code)
    while index < len(code):
        opcode = code[index]
        index += 1
        print('sewc', opcode)
        if opcode >= dis.HAVE_ARGUMENT:
            arg = code[index] + code[index + 1] * 256
            index += 2

            if opcode == dis.opmap['LOAD_NAME']:
                name = code[index:index + arg].decode('utf-8')
                if not name.startswith('__'):
                    names.add(name)

        # Skip variable-length opcodes (e.g., jumps)
        if opcode >= dis.HAVE_ARGUMENT:
            index += 2

    for name in sorted(names):
        print(name)
