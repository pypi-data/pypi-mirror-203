# oo interface for vsui client, idea is to allow better control over enabling/disabling

from typing import Union
import logging
from abc import ABC, abstractmethod
import vsui_client._vsui_client as _vsui_client

class VSUIClient(ABC):
    ''' Baseclass wrapper for vsui_client that allows for better control over enabling/disabling '''
    _handler = None
    @abstractmethod
    def connect(self, host : str = 'localhost', port : str = '8000') -> None:
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        pass
    
    @abstractmethod
    def edit_element(self, element_uid: str, value: Union[dict, str]) -> None:
        pass

    @abstractmethod
    def deactivate_task(self) -> None:
        pass

    @abstractmethod
    def notify(self, txt : str, type : str) -> None:
        pass

    @abstractmethod
    def set_task_id(self, id : str) -> None:
        pass

    @abstractmethod
    def set_logging_target(self, key : str) -> None:
        pass

    @abstractmethod
    def encode_image(
        self,
        arr,
        title: str = '',
        format : str = 'jpg',
        figsize: tuple = (8, 8),
        cmap: str = "gray"
    ) -> str:
        pass

    @abstractmethod
    def get_handler(self) -> logging.Handler:
        pass

class VSUIEnabled():
    ''' OO interface for vsui client, when vsui is enabled '''
    def connect(self, host : str = 'localhost', port : str = '8000') -> None:
        ''' Initiate a connection to the server om the given host and port. 
        Args:
            host (str): The host to connect to. Defaults to 'localhost'.
            port (str): The port to connect to. Defaults to '8000'.
        '''
        return _vsui_client.connect(host, port)
    
    def disconnect(self) -> None:
        ''' Disconnect from the server.'''
        return _vsui_client.disconnect()
    
    def edit_element(self, element_uid: str, value: Union[dict, str]) -> None:
        ''' Edit a ui element for the task on the server that corresponds to this process.
        Args:
            element_uid (str): The uid of the element to edit.
            value: The new value of the element. Can be a string or a dict.
                This should follow the api definition for the element type.
        '''
        return _vsui_client.edit_element(element_uid=element_uid, value=value)
    
    def deactivate_task(self) -> None:
        ''' Deactivate the task on the server that corresponds to this process.'''
        return _vsui_client.deactivate_task()

    def notify(self, txt : str, type : str) -> None:
        ''' Send a notification to the server. This will show as a toast to the user.'''
        return _vsui_client.notify(txt, type)

    def set_task_id(self, id : str) -> None:
        ''' Set the task id for the task on the server that corresponds to this process.'''
        return _vsui_client.set_task_id(id)
    
    def set_logging_target(self, key : str) -> None:
        ''' Set the logging target for the task on the server that corresponds to this process.'''
        return _vsui_client.set_logging_target(key)

    def encode_image(
        self,
        arr,
        title: str = '',
        format : str = 'jpg',
        figsize: tuple = (8, 8),
        cmap: str = "gray"
    ) -> str:
        ''' Encode an image to a base64 string.
        Args:
            arr (np.ndarray): The image to encode.
            title (str, optional): The title of the image. Defaults to ''.
            format (str, optional): The format to encode the image as. Defaults to 'jpg'.
            figsize (tuple, optional): The size of the image. Defaults to (8, 8).
            cmap (str, optional): The colormap to use. Defaults to "gray".
        Returns:
            str: The encoded image.
        '''
        return _vsui_client.encode_image(
            arr=arr,
            title=title,
            format=format,
            figsize=figsize,
            cmap=cmap
        )
    
    def get_handler(self) -> logging.Handler:
        ''' Provides access to the logging handler singleton.'''
        if self._handler is None:
            self._handler = _vsui_client.RequestHandler()
        return self._handler

class VSUIDisabled():
    ''' OO interface for vsui client, when vsui is disabled '''
    def connect(self, host : str = 'localhost', port : str = '8000') -> None:
        ''' do nothing - not in UI mode '''
        pass
    
    def disconnect(self) -> None:
        ''' do nothing - not in UI mode '''
        pass

    def edit_element(self, element_uid: str, value: Union[dict, str]) -> None:
        ''' do nothing - not in UI mode '''
        pass

    def deactivate_task(self) -> None:
        ''' do nothing - not in UI mode '''
        pass

    def notify(self, txt : str, type : str) -> None:
        ''' do nothing - not in UI mode '''
        pass

    def set_task_id(self, id : str) -> None:
        ''' do nothing - not in UI mode '''
        pass

    def set_logging_target(self, key : str) -> None:
        ''' do nothing - not in UI mode '''
        pass

    def encode_image(
        self,
        arr,
        title: str = '',
        format : str = 'jpg',
        figsize: tuple = (8, 8),
        cmap: str = "gray"
    ) -> str:
        ''' do nothing - not in UI mode '''
        pass

    def get_handler(self) -> logging.Handler:
        ''' return null handler - not in UI mode '''
        if self._handler is None:
            self._handler = logging.NullHandler()
        return self._handler