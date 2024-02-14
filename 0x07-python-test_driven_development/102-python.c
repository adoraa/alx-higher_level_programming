#include <Python.h>
/**
 * print_python_string - prints information about a Python string object
 * @p: Pointer to a Python object (string)
 */
void print_python_string(PyObject *p)
{
    if (PyUnicode_Check(p))
    {
        printf("[.] string object info\n");
        if (PyUnicode_IS_COMPACT_ASCII(p))
            printf("  type: compact ascii\n");
        else if (PyUnicode_IS_COMPACT(p))
            printf("  type: compact unicode object\n");
        else
            printf("  type: compact bytes object\n");

        printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
        printf("  value: %ls\n", PyUnicode_AS_UNICODE(p));
    }
    else
    {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
    }
}
