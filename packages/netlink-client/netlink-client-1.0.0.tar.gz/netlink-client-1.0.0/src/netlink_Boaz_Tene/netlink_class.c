/*
    Python client for the Netlink interface.
    Copyright (C) 2023 Boaz Tene

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/
#include <Python.h>
#include "netlink_class.h"

static PyObject *netlink_send(NetLink *self, PyObject *args) {
  Py_buffer buffer;

  if (!PyArg_ParseTuple(args, "y*", &buffer)) {
    PyErr_SetString(PyExc_TypeError, "Received invalid argument.");
    return NULL;
  }

  send_nl(self->netlink, (char *) buffer.buf, buffer.len);
  PyBuffer_Release(&buffer);

  Py_RETURN_NONE;
}

static PyObject *netlink_recv(NetLink *self, PyObject *args) {
  int bytes;

  if (!PyArg_ParseTuple(args, "i", &bytes)) {
    PyErr_SetString(PyExc_TypeError, "Received invalid argument.");
    return NULL;
  }

  char *buf = (char *)PyMem_Malloc(bytes);

  recv_nl(self->netlink, buf, bytes);

  PyObject *res = PyBytes_FromString(buf);

  PyMem_Del(buf);

  return res;
}

static PyObject *netlink_close(NetLink *self, PyObject *args) {
  if (self->netlink != NULL) {
    close_nl(self->netlink);
    Py_RETURN_NONE;
  }

  return NULL;
}

static PyObject *NetLink_new(PyTypeObject *type, PyObject *args,
                             PyObject *kwds) {
  NetLink *self;

  self = (NetLink *)type->tp_alloc(type, 0);

  return (PyObject *)self;
}

static void NetLink_dealloc(NetLink *self) {
  if (self->netlink != NULL) {
    free(self->netlink);
  }

  Py_TYPE(self)->tp_free((PyObject *)self);
}

static void NetLink_init(NetLink *self, PyObject *args, PyObject *kwds) {
  if (!PyArg_ParseTuple(args, "i", &self->magic_number))
    return;

  self->netlink = (struct netlink *)malloc(sizeof(struct netlink));

  self->netlink = initialize_netlink(self->netlink, self->magic_number);

  if (self->netlink->sock_fd < 0) {
    PyErr_SetString(PyExc_ConnectionRefusedError,
                    "Couldn't connect to netlink.");
  }

  connect_nl(self->netlink);
}

static PyMemberDef NetLink_members[] = {
    {"__netlink", T_OBJECT_EX, offsetof(NetLink, netlink), 0, "The netlink."},
    {NULL} /* Sentinel */
};

static PyMethodDef NetLink_methods[] = {
    {"send", (PyCFunction)netlink_send, METH_VARARGS,
     "Sends a message.\n@param message The message to send (bytes)."},
    {"recv", (PyCFunction)netlink_recv, METH_VARARGS,
     "recv a message (Will wait until arrival).\n@param max_bytes the max "
     "number of bytes to receive.\nNote that the number of bytes is EOF or "
     "max_bytes."},
    {"close", (PyCFunction)netlink_close, METH_VARARGS,
     "closes the connection."},
    {NULL} /* Sentinel */
};

PyTypeObject NetLinkType = {
    PyVarObject_HEAD_INIT(NULL, 0) "netlink.NetLink", /* tp_name */
    sizeof(NetLink),                                  /* tp_basicsize */
    0,                                                /* tp_itemsize */
    (destructor)NetLink_dealloc,                      /* tp_dealloc */
    0,                                                /* tp_print */
    0,                                                /* tp_getattr */
    0,                                                /* tp_setattr */
    0,                                                /* tp_reserved */
    0,                                                /* tp_repr */
    0,                                                /* tp_as_number */
    0,                                                /* tp_as_sequence */
    0,                                                /* tp_as_mapping */
    0,                                                /* tp_hash  */
    0,                                                /* tp_call */
    0,                                                /* tp_str */
    0,                                                /* tp_getattro */
    0,                                                /* tp_setattro */
    0,                                                /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,                               /* tp_flags */
    "Client implmentation of the netlink kenrel interface.", /* tp_doc */
    0,                                                       /* tp_traverse */
    0,                                                       /* tp_clear */
    0,                      /* tp_richcompare */
    0,                      /* tp_weaklistoffset */
    0,                      /* tp_iter */
    0,                      /* tp_iternext */
    NetLink_methods,        /* tp_methods */
    NetLink_members,        /* tp_members */
    0,                      /* tp_getset */
    0,                      /* tp_base */
    0,                      /* tp_dict */
    0,                      /* tp_descr_get */
    0,                      /* tp_descr_set */
    0,                      /* tp_dictoffset */
    (initproc)NetLink_init, /* tp_init */
    0,                      /* tp_alloc */
    NetLink_new,            /* tp_new */
};
