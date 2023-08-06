"""
tk_cbed network suites designed to align and restore CBED data

Author: Ivan Lobato
Email: Ivanlh20@gmail.com
"""
import os
import pathlib
from typing import Tuple

import h5py
import numpy as np
import tensorflow as tf

# Our Unet reduces the size of the image by a factor of 2^4 = 16
# therefore, we need to pad the input image to be a multiple of 16
allow_sizes = 16*np.arange(2, 129, dtype=np.int32)

# The following functions are used to pad the input image to be a multiple of 16
def select_size(n):
    ind = np.argmin(np.abs(allow_sizes - n))
    if allow_sizes[ind] < n:
        return allow_sizes[ind+1]
    else:
        return allow_sizes[ind]

def expand_dimensions(x):
    if x.ndim == 2:
        return np.expand_dims(x, axis=(0, 3))
    elif x.ndim == 3 and x.shape[-1] != 1:
        return np.expand_dims(x, axis=3)
    else:
        return x

def add_extra_rows_or_columns(x):
    ny = select_size(x.shape[1])
    if ny > x.shape[1]:
        v_bg = np.zeros((x.shape[0], ny-x.shape[1], x.shape[2], x.shape[-1]), dtype=x.dtype)
        x = np.concatenate((x, v_bg), axis=1)

    nx = select_size(x.shape[2])
    if nx > x.shape[2]:
        v_bg = np.zeros((x.shape[0], x.shape[1], nx-x.shape[2], x.shape[-1]), dtype=x.dtype)
        x = np.concatenate((x, v_bg), axis=2)

    return x

def remove_extra_rows_or_columns(x, x_i_sh):
    if x_i_sh != x.shape:
        return x[:, :x_i_sh[1], :x_i_sh[2], :]
    else:
        return x

def remove_extra_rows_or_columns_symm(x, x_i_sh):
    if x_i_sh != x.shape:
        nxh = x_i_sh[2]//2 if x_i_sh[2] % 2 == 0 else (x_i_sh[2]-1)//2
        nyh = x_i_sh[1]//2 if x_i_sh[1] % 2 == 0 else (x_i_sh[1]-1)//2
        ix_0 = x.shape[1]//2-nxh
        iy_0 = x.shape[2]//2-nyh
        
        return x[:, ix_0:(ix_0+x.shape[1]), iy_0:(iy_0+x.shape[2]), :]
    else:
        return x

def adjust_output_dimensions(x, x_i_shape):
    ndim = len(x_i_shape)
    if ndim == 2:
        return x.squeeze()
    elif ndim == 3:
        if x_i_shape[-1] == 1:
            return x.squeeze(axis=0)
        else:
            return x.squeeze(axis=-1)  
    else:
        return x

class RC_CBED(tf.keras.Model):
    def __init__(self, model_path):
        super(RC_CBED, self).__init__()
        self.base_model = tf.keras.models.load_model(model_path, compile=False)
        self.base_model.compile()
        
    def call(self, inputs, training=None, mask=None):
        return self.base_model(inputs, training=training, mask=mask)
        
    def summary(self):
        return self.base_model.summary()
    
    def predict(self, x, batch_size=16, verbose=0, steps=None, callbacks=None, max_queue_size=10, workers=1, use_multiprocessing=False):
        x_i_sh = x.shape

        # Expanding dimensions based on the input shape
        x = expand_dimensions(x)

        # Converting to float32 if necessary
        x = x.astype(np.float32)

        x_i_sh_e = x.shape

        # Adding extra row or column if necessary
        x = add_extra_rows_or_columns(x)

        batch_size = min(batch_size, x.shape[0])

        # Model prediction
        x = self.base_model.predict(x, batch_size, verbose, steps, callbacks, max_queue_size, workers, use_multiprocessing)

        # Removing extra row or column if added
        x = remove_extra_rows_or_columns_symm(x, x_i_sh_e)

        # Adjusting output dimensions to match input dimensions
        return adjust_output_dimensions(x, x_i_sh)

class R_CBED(tf.keras.Model):
    def __init__(self, model_path):
        super(R_CBED, self).__init__()
        self.base_model = tf.keras.models.load_model(model_path, compile=False)
        self.base_model.compile()
        
    def call(self, inputs, training=None, mask=None):
        return self.base_model(inputs, training=training, mask=mask)
        
    def summary(self):
        return self.base_model.summary()
    
    def predict(self, x, batch_size=16, verbose=0, steps=None, callbacks=None, max_queue_size=10, workers=1, use_multiprocessing=False):
        x_i_sh = x.shape

        # Expanding dimensions based on the input shape
        x = expand_dimensions(x)

        # Converting to float32 if necessary
        x = x.astype(np.float32)

        x_i_sh_e = x.shape

        # Adding extra row or column if necessary
        x = add_extra_rows_or_columns(x)

        batch_size = min(batch_size, x.shape[0])

        # Model prediction
        x = self.base_model.predict(x, batch_size, verbose, steps, callbacks, max_queue_size, workers, use_multiprocessing)

        # Removing extra row or column if added
        x = remove_extra_rows_or_columns(x, x_i_sh_e)

        # Adjusting output dimensions to match input dimensions
        return adjust_output_dimensions(x, x_i_sh)


def load_network(model_name: str = 'rc_cbed'):
    """
    Load one of the tk_cbed neural network models.

    :param model_name: A string representing the name of the model.
    :return: A tensorflow.keras.Model object.
    """
    if os.path.isdir(model_name):
        model_path = pathlib.Path(model_name).resolve()
    else: 
        model_name = model_name.lower()
        model_path = pathlib.Path(__file__).resolve().parent / 'models' / model_name

    if 'rc_cbed' in os.path.basename(model_path).lower():
        model = RC_CBED(model_path)
    elif 'r_cbed' in os.path.basename(model_path).lower():
        model = R_CBED(model_path)
    elif 'c_cbed' in os.path.basename(model_path).lower():
        model = tf.keras.models.load_model(model_path, compile=False)
        model.compile()
    else:
        raise ValueError('Unknown model type.')

    return model

def load_sim_test_data(file_name: str = 'rc_cbed') -> Tuple[np.ndarray, np.ndarray]:
    """
    Load test data for r_em neural network.

    :param model_name: A string representing the name of the model.
    :return: A tuple containing two numpy arrays representing the input (x) and output (y) data.
    """
    if os.path.isfile(file_name):
        path = pathlib.Path(file_name).resolve()
    else:
        file_name = file_name.lower()
        path = pathlib.Path(__file__).resolve().parent / 'test_data' / 'cbed.h5'

    with h5py.File(path, 'r') as h5file:
        x = np.asarray(h5file['x'][:], dtype=np.float32).transpose(0, 3, 2, 1)
        
        if 'c_cbed' == file_name:
            y = np.asarray(h5file['y_dr'][:], dtype=np.float32)
        else:
            y = np.asarray(h5file['y'][:], dtype=np.float32).transpose(0, 3, 2, 1)
            y = y[..., 0] if 'r_cbed' == file_name else y[..., 1]
            y = y[..., np.newaxis]  
              
    return x, y

def load_exp_test_data(file_name: str = 'exp_hrstem') -> Tuple[np.ndarray, np.ndarray]:
    """
    Load test data for r_em neural network.

    :param model_name: A string representing the name of the model.
    :return: A tuple containing two numpy arrays representing the input (x) and output (y) data.
    """

    if os.path.isfile(file_name):
        path = pathlib.Path(file_name).resolve()
    else:
        file_name = file_name.lower()
        path = pathlib.Path(__file__).resolve().parent / 'test_data' / f'{file_name}.h5'

    with h5py.File(path, 'r') as f:
        x = f['x'][:]
        if x.ndim == 4:
            x = np.asarray(x, dtype=np.float32).transpose(0, 3, 2, 1)
        else:
            x = np.asarray(x, dtype=np.float32).transpose(1, 0)
    
    return x