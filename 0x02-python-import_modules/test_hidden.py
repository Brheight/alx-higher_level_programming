import py_compile
import dis
if __name__ == "__main__":
    compiled_file = open("hidden_4.pyc", 'rb')
    code = compiled_file.read()
print('hid 4 pyc content', dis.dis(code))

