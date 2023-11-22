#include <Python.h>
/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a Python object
 *
 * This function checks if the given Python object is a valid bytes object,
 * and if so, prints information about its size, string representation, and
 * the first 10 bytes.
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first 10 bytes: ");
	fflush(stdout);
	for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; ++i)
	{
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
}
/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to a Python object
 * This function checks if the given Python object is a valid list object,
 * and if so, prints information about the list size, allocated space, and
 * detailed information about each element in the list, including handling
 * nested lists, bytes, floats, ints, and strings.
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %ld: ", i);
		if (PyBytes_Check(element))
		{
			print_python_bytes(element);
		}
		else if (PyFloat_Check(element))
		{
			printf("float\n");
			printf("[.] float object info\n");
			printf("  value: %f\n", PyFloat_AS_DOUBLE(element));
		}
		else if (PyLong_Check(element))
		{
			printf("int\n");
		}
		else if (PyUnicode_Check(element))
			printf("str\n");
		else if (PyList_Check(element) || PyTuple_Check(element))
			printf("list\n");
		else
		{
			printf("[.] %s object info\n", element->ob_type->tp_name);
			printf("  [ERROR] Unknown type\n");
		}
	}
}
/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to a Python object
 *
 * This function checks if the given Python object is a valid float object,
 * and if so, prints information about the float value.
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
}
