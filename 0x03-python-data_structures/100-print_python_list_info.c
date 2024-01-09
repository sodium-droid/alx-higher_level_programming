#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - prints python list info
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
    long int , size = PyList_Size(p);
    PyListObject *obj = (PyListObject *)p;
    
    printf("[*] size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", obj->allocated);
    for (i = 0; i < size; i++)
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
}
