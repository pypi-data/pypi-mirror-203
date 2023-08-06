#define PY_SSIZE_T_CLEAN
#include <Python.h>

float real48_to_float(unsigned char* real48_data) {
    unsigned char bytes[6];
    float result;
    int i;

    /* Copy the 6 bytes of the real48 data into a local array */
    for (i = 0; i < 6; i++) {
        bytes[i] = real48_data[i];
    }

    /* Convert the real48 data to a float */
    bytes[5] &= 0x7F;
    result = (float)((bytes[0] << 8) | bytes[1]);
    result += (float)((bytes[2] << 8) | bytes[3]) / 65536.0;
    result += (float)((bytes[4] << 8) | bytes[5]) / 4294967296.0;
    if (real48_data[5] & 0x80) {
        result = -result;
    }

    return result;
}

static PyObject* real48_to_float_wrapper(PyObject* self, PyObject* args) {
    unsigned char* real48_data;
    Py_ssize_t data_len;
    float result;

    /* Parse the input arguments */
    if (!PyArg_ParseTuple(args, "y#", &real48_data, &data_len)) {
        return NULL;
    }

    /* Call the real48_to_float function */
    result = real48_to_float(real48_data);

    /* Build the result as a Python float object */
    return PyFloat_FromDouble((double)result);
}

static PyMethodDef real48_methods[] = {
    {"real48_to_float", real48_to_float_wrapper, METH_VARARGS, "Converts a real48 value to a float."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef real48_module = {
    PyModuleDef_HEAD_INIT,
    "real48",
    NULL,
    -1,
    real48_methods
};

PyMODINIT_FUNC PyInit_real48(void) {
    return PyModule_Create(&real48_module);
}