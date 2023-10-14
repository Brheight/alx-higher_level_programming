#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_bytes - Prints info about a Python bytes object
 * @p: PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    string = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);
    printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);

    for (i = 0; i <= size && i < 10; i++)
    {
        printf("%02hhx", string[i]);
        if (i < size && i < 9)
            printf(" ");
    }

    printf("\n");
}

/**
 * print_python_list - Prints info about a Python list object
 * @p: PyObject list object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, allocated, i;
    PyObject *item;

    printf("[*] Python list info\n");

    size = PyList_Size(p);
    allocated = Py_SIZE(list);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
