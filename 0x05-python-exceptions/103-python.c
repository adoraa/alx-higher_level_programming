#include <Python.h>
#include <stdio.h>
/**
 * print_python_bytes - prints information about a Python bytes object
 * @p: PyObject pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	for (1 = 0; i < size; i++)
		printf("%02x ", (unsigned char)bytes->ob_sval[i]);
	printf("\n");
	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
		printf("%02x\n", (unsigned char)(((char *)p)[i]);
}

/**
 * print_python_list - prints information about a Python list object
 * @p: PyObject pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, i;
	PyObject *element;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
		printf("  [ERROR] Invalid List Object\n");
	ssize = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	pprintf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		ielement = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}

/**
 * print_python_float - prints information about a Python float object
 * @p: PyObject pointer to the Python float object
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *f = (PyFloatObject *)p;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
		printf("  [ERROR] Invalid Float Object\n");
	printf("  value: %lf\n", f->ob_fval);
}
