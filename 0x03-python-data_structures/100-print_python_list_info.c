#include <Python.h>
/**
 * print_python_list_info - print basic info about python
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;
	PyObject *ob;

	size = Pysize(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*]Size of the Python List = %d\n", size);
	printf("[*]Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
