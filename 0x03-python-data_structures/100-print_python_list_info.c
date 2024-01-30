#include <Python.h>
/**
 * print_python_list_info - prints information about Python lists
 * @p: PyObject pointer to the Python list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t l_size, l_alloc, i;
	PyObject *l_item;

	list = (PyListObject *)p;
	l_size = PyList_Size(p);
	l_alloc = list->allocated;

	printf("[*] Size of the Python List = %ld\n", l_size);
	printf("[*] Allocated = %ld\n", l_alloc);
	for (i = 0; i < l_size; i++)
	{
		l_item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(l_item)->tp_name);
	}
}
