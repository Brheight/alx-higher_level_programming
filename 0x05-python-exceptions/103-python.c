#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints some basic info about Python lists.
 * @p: PyObject
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, allocated, i;
    PyObject *item;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Prints some basic info about Python bytes.
 * @p: PyObject
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    if (size < 10)
        printf("  first %ld bytes: ", size);
    else
        printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", str[i] & 0xff);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_float - Prints some basic info about Python float objects.
 * @p: PyObject
 */
void print_python_float(PyObject *p) {
    double value;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AS_DOUBLE(p);
    printf("  value: %f\n", value);
}
