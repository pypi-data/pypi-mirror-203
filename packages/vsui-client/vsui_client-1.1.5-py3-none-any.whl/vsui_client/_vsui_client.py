import socketio
from typing import Any, Callable
import logging
from matplotlib import pyplot as plt
import io
import sys
import base64
import time

from vsui_client._log import _vsui_logger

sio = socketio.Client()
task_id = None
# target log for where intercepted logs should be forwarded to
logging_target = None
timeout_count = 0

# https://stackoverflow.com/a/51981833
def vsui_process() -> Callable:
    ''' Decorator for functions that should be run as a vsui task 
        This decorator will catch any exceptions and send a message to the server
        returns the decorator
    '''
    def decorator(func) -> Any:
        def wrapper(*args, **kwargs):
            _vsui_logger.info(f'running {func.__name__} as vsui process')
            r = None
            try:
                r = func(*args, **kwargs)
            except (SystemExit, Exception) as e:
                _vsui_logger.exception(f'exception caught: {e}')
                safe_emit('exception', {'task_id' : task_id, 'exception' : str(e)})
                r = disconnect()
                # print to the standart error stream
                print(f'process {func.__name__} failed, exception: {e}', file=sys.stderr)
                raise SystemExit(1)
            finally:
                _vsui_logger.info(f'finished running {func.__name__} as vsui process')
                return r
        return wrapper
    return decorator

def safe_emit(event, data):
    ''' emit a socketio event with exception handling '''
    global timeout_count
    try:
        sio.emit(event, data)
        timeout_count = 0
    except:
        timeout_count += 1
        if timeout_count == 5:
            _vsui_logger.exception('socketio timeout')
            safe_emit('exception', {'task_id' : task_id, 'exception' : 'socketio timeout'})
            disconnect()
            time.sleep(1)
            sys.exit(1)

def connect(HOST : str = 'localhost', PORT : str = '8000') -> None:
    ''' initiate a socketio session with a server '''
    sio.connect('http://' + HOST + ':' + PORT, headers={'type':'app', 'id': task_id})
    _vsui_logger.info(f'connected to {HOST}:{PORT} with sid {sio.sid}')

def disconnect() -> None:
    ''' disconnect the socketio session '''
    sio.disconnect()
    _vsui_logger.info('disconnected')

# struct: { 'name' : 'type' }
# send a new task to be added to the server's task manager
def set_task_id(id : str) -> None:
    ''' set the id of this task '''
    global task_id
    task_id = id

def set_logging_target(key: str) -> None:
    global logging_target
    logging_target = {'element_key' : key}

# edit one of the elements in the task, this allows data updating
def edit_element(element_uid : str, value : Any) -> None:
    ''' Edit the target display element, images must be base 64 encoded '''
    safe_emit('edit_element', {'task_id' : task_id, 'element_key' : element_uid, 'value' : value})

# mark the task as completed
def deactivate_task() -> None:
    ''' deactivate the current task '''
    safe_emit('deactivate_task', task_id)

def notify(txt : str, type : str) -> None:
    ''' send a popup to the client '''
    safe_emit('notify', {'txt':txt, 'type':type})

def logging_intercept(msg) -> None:
    ''' forward logs to the target display element '''
    if logging_target is not None:
        edit_element(logging_target['element_key'],msg)
    else:
        logging.error('No logging target set.')

# http://naoko.github.io/intercept-python-logging/
class RequestHandler(logging.Handler):
    def emit(self, record):
        ''' Intercept logs '''
        logging_intercept(record.getMessage())

def encode_image(
    arr,
    title: str = '',
    format : str = 'jpg',
    figsize: tuple = (8, 8),
    cmap: str = "gray"
):
    fig = plt.figure(figsize=figsize)
    plt.imshow(arr, cmap=cmap)
    plt.suptitle(title, fontsize=16)
    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format=format)
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()
    return my_base64_jpgData