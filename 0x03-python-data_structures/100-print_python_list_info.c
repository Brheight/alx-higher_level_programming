#include <stdio.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to Python object (a list)
 */
void print_python_list_info(PyObject *p)
{
    int size, i;
    PyObject *item;

    size = PyObject_Length(p); // Get the length of the list

    if (size < 0) {
        PyErr_Print(); // Handle Python error
        return;
    }

    printf("[*] Size of the Python List = %d\n", size);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
