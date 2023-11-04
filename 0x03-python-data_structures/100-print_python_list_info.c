#include <Python.h>
/**
 * print_python_list_info - print basic info about python
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;
	PyObject *ob;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*]Size of the Python List = %d\n", size);
	printf("[*]Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		ob = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
