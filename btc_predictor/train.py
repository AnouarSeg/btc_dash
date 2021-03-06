#!usr/bin/python
import numpy as np
import tensorflow as tf
from btc_predictor.datasets import DataReader
from btc_predictor.models import LSTMModel


tf.random.set_seed(78)
np.random.seed(78)

model_params = {
    "input_shape": (29, 1),
    "dropout": 0.4,
    "num_forward": 1,
}

train_params = {
    "TRAIN_SIZE": 1680,
    "VAL_SIZE": 180,
    "WINDOW_SIZE": 16,
    "BATCH_SIZE": 256,
    "EPOCHS": 15,
    "EVALUATION_INTERVAL": 64,
    "VALIDATION_STEPS": 64,
    "WALK_FORWARD": 30,
}

data_file = "btc_predictor/datasets/Bitstamp_BTCUSD_d.csv"

data = DataReader(data_file=data_file)
lstm = LSTMModel(model_args=model_params, train_args=train_params)
lstm.fit(data=data)
rmse, da, mda = lstm.eval(data=data)
print(rmse, da, mda)
lstm.save()