from typing import Any, List, Dict, Optional, Tuple

import numpy

import xarray
from deprecated.classic import deprecated
from drb.core import DrbNode
from drb.exceptions.core import DrbNotImplementationException, DrbException

from drb.drivers.grib.grib_common import DrbGribAbstractNode, \
    DrbGribSimpleValueNode
import drb.topics.resolver as resolver


class DrbGribDimNode(DrbGribAbstractNode):
    """
    This node is used to have one or many children of DrbNode but no value.

    Parameters:
        parent (DrbNode): The node parent.
        dims dimensions (dict like).
    """
    def __init__(self, parent: DrbNode, dims):
        super().__init__(parent, name='dimensions')

        self.parent: DrbNode = parent
        self._children: List[DrbNode] = []
        self._available_impl.clear()
        for key in dims.keys():
            self._children.append(DrbGribSimpleValueNode(self, key, dims[key]))

    @property
    @deprecated(version='1.2.0',
                reason='Usage of the bracket is recommended')
    @resolver.resolve_children
    def children(self) -> List[DrbNode]:
        return self._children

    def get_impl(self, impl: type, **kwargs) -> Any:
        raise DrbNotImplementationException(f'no {impl} implementation found')


class DrbGribCoordNode(DrbGribAbstractNode):
    """
    This node is used to have one or many children of DrbNode but no value.

    Parameters:
        parent (DrbNode): The node parent.
        data_set_coord (DatasetCoordinates): dataset from xarray.
    """
    def __init__(self, parent: DrbNode,
                 data_set_coord: xarray.core.coordinates.DatasetCoordinates):
        super().__init__(parent, name='coordinates')
        self._data_set_coord = data_set_coord
        self.parent: DrbNode = parent
        self._children = None
        self._available_impl = [
            xarray.core.coordinates.DatasetCoordinates
        ]
        self.value = self._data_set_coord

    @property
    @deprecated(version='1.2.0',
                reason='Usage of the bracket is recommended')
    @resolver.resolve_children
    def children(self) -> List[DrbNode]:
        if self._children is None:
            self._children = []
            for key in self._data_set_coord.keys():
                self._children.append(DrbGribArrayNode(
                    self,
                    key,
                    self._data_set_coord[key]))
        return self._children

    def get_impl(self, impl: type, **kwargs) -> Any:
        if self.has_impl(impl):
            return self._data_set_coord
        raise DrbNotImplementationException(f'no {impl} implementation found')


class DrbGribArrayNode(DrbGribAbstractNode):
    """
    This node is used to have one or many children of DrbNode but no value.

    Parameters:
        parent (DrbNode): The node parent.
        name (str): the name of the data.
    """
    def __init__(self, parent: DrbNode,
                 name: str,
                 data_array: xarray.DataArray):
        super().__init__(parent, name=name)
        self._data_array = data_array
        self.parent: DrbNode = parent
        self.name = name
        self._attribute = None
        self._available_impl = [
            numpy.ndarray,
            xarray.DataArray
        ]
        self.value = data_array.all()
        self.__init_attributes()

    def __init_attributes(self):
        for key in self._data_array.attrs:
            self @= (key, self._data_array.attrs[key])

    @property
    @deprecated(version='1.2.0',
                reason='Usage of the bracket is recommended')
    @resolver.resolve_children
    def children(self) -> List[DrbNode]:
        return []

    def get_impl(self, impl: type, **kwargs) -> Any:
        if isinstance(self._data_array, impl):
            return self._data_array
        if impl == numpy.ndarray:
            return self._data_array.to_numpy()
        raise DrbNotImplementationException(f'no {impl} implementation found')
