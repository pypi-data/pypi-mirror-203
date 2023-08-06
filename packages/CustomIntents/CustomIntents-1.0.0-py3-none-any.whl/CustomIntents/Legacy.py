import json
import os
import pickle
import random
from collections import OrderedDict
from pathlib import Path
from time import perf_counter

import keras
import numpy as np
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import nltk
from nltk.stem import WordNetLemmatizer

from keras_preprocessing.image import img_to_array
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, MaxPooling2D, Flatten, \
    Conv2D, GlobalAveragePooling2D, Activation
from tensorflow.python.keras import layers
from tensorflow.python.keras.optimizer_v2.gradient_descent import SGD
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.optimizer_v2.adam import Adam
from tensorflow.python.keras.optimizer_v2.adamax import Adamax
from tensorflow.python.keras.optimizer_v2.adagrad import Adagrad
from tensorflow.python.keras.metrics import Precision, Recall, BinaryAccuracy

from random import random

import wandb
from wandb.keras import WandbCallback
import matplotlib.pyplot as plt

import imghdr
import cv2.load_config_py2
import cv2
import csv

from threading import Thread

from functools import wraps

from collections import Counter

from CustomIntents.Pfunction import Pfunctions


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result

    return timeit_wrapper


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class VideoStream:

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # Return the latest frame
        return self.frame

    def stop(self):
        self.stopped = True


class ChatBot:

    def __init__(self, intents, intent_methods, model_name="assistant_model", threshold=0.25, w_and_b=False,
                 tensorboard=False):
        nltk.download('punkt', quiet=True)
        nltk.download('wordnet', quiet=True)
        self.model = None
        self.words = None
        self.classes = None
        self.hist = None
        self.intents = intents
        self.intent_methods = intent_methods
        self.model_name = model_name
        self.model_threshold = threshold
        self.w_and_b = w_and_b
        if intents.endswith(".json"):
            self.load_json_intents(intents)

        self.lemmatizer = WordNetLemmatizer()
        if w_and_b:
            wandb.init(project=model_name)
        if tensorboard:
            pass

    def load_json_intents(self, intents: str):
        self.intents = json.loads(open(intents).read())

    def train_model(self, epoch=None, batch_size=5, learning_rate=None, ignore_letters=None, timeIt=True,
                    model_type='s1', validation_split=0, optimizer=None, accuracy_and_loss_plot=True):
        start_time = perf_counter()

        # ckeing for right types of input
        # validation split
        if type(validation_split) is not int:
            print(f"{bcolors.FAIL}validation split should be an int ! \n"
                  f"it will defualt to 0{bcolors.ENDC}")
            validation_split = 0
        else:
            if validation_split < 0 or validation_split >= 1:
                print(f"{bcolors.FAIL}validation split should be beetwen 0 and 1\n"
                      f"it will defualt to 0 {bcolors.ENDC}")
        # ignore letters
        if type(ignore_letters) is not list:
            print(f"{bcolors.FAIL}ignore letters should be a list of letters you want to ignore\n"
                  f"it will set to defualt (['!', '?', ',', '.']){bcolors.ENDC}")
        # batch size
        if type(batch_size) is not int:
            print(f"{bcolors.FAIL}batch size should be an int\n"
                  f"it will set to defualt (5){bcolors.ENDC}")
        # timeIt
        if type(timeIt) is not bool:
            print(f"{bcolors.FAIL}timeIt should be a bool\n"
                  f"it will set to defualt (True)")
        # accuracy and loss plot
        if type(accuracy_and_loss_plot) is not bool:
            print(f"{bcolors.FAIL}accuracy_and_loss_plot should be a bool\n"
                  f"it will set to defualt (True)")

        # defualt optimizer
        if optimizer is None:
            optimizer = "Adam"
        # defualt learning_rate
        learning_rate_is_defualt = False
        if type(learning_rate) is int and learning_rate is not None:
            print(f"{bcolors.FAIL}learning rate should be an int\n"
                  f"it will defualt to defualt learning rate of the selected mdel{bcolors.ENDC}")
            learning_rate = None
        if learning_rate is None:
            learning_rate_is_defualt = True
            if model_type == "m2" or model_type == "s2" or model_type == "l1":
                learning_rate = 0.005
            elif model_type == "m3" or model_type == "s5" or model_type == "s4" or model_type == "s3":
                learning_rate = 0.001
            elif model_type == "l2":
                learning_rate = 0.0005
            elif model_type == "l3":
                learning_rate = 0.00025
            elif model_type == "l4":
                learning_rate = 0.0002
            elif model_type == "l5" or model_type == "l5f" or model_type == "xl1" or model_type == "xl2":
                learning_rate = 0.0001
            else:
                learning_rate = 0.01
        if learning_rate_is_defualt and optimizer == "Adamgrad":
            learning_rate = learning_rate * 50

        # defualt epoch
        if type(epoch) is not int and epoch is not None:
            print(f"{bcolors.FAIL}epochs should be an int\n"
                  f"it will defualt to defualt epoch of the selected mdel{bcolors.ENDC}")
            epoch = None
        if epoch is None:
            if model_type == "l1" or model_type == "xs2" or model_type == "s1" or model_type == "s2" or model_type == "s3" or model_type == "m1" or model_type == "m2":
                epoch = 200
            elif model_type == "xl2":
                epoch = 700
            elif model_type == "l3" or model_type == "l5f":
                epoch = 1000
            elif model_type == "l4" or model_type == "l5":
                epoch = 2000
            else:
                epoch = 500

        if ignore_letters is None:
            ignore_letters = ['!', '?', ',', '.']
        self.words = []
        self.classes = []
        documents = []

        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                word = nltk.word_tokenize(pattern)
                self.words.extend(word)
                documents.append((word, intent['tag']))
                if intent['tag'] not in self.classes:
                    self.classes.append(intent['tag'])

        self.words = [self.lemmatizer.lemmatize(w.lower()) for w in self.words if w not in ignore_letters]
        self.words = sorted(list(set(self.words)))

        self.classes = sorted(list(set(self.classes)))

        training = []
        output_empty = [0] * len(self.classes)

        for doc in documents:
            bag = []
            word_patterns = doc[0]
            word_patterns = [self.lemmatizer.lemmatize(word.lower()) for word in word_patterns]
            for word in self.words:
                bag.append(1) if word in word_patterns else bag.append(0)

            output_row = list(output_empty)
            output_row[self.classes.index(doc[1])] = 1
            training.append([bag, output_row])

        random.shuffle(training)
        training = np.array(training, dtype=object)

        train_x = list(training[:, 0])
        train_y = list(training[:, 1])

        print(f"model type = {model_type}")
        # defining layers start

        # xs1 model
        if model_type == "xs1":
            self.model = Sequential()
            self.model.add(Dense(32, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(16, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # xs2 model
        elif model_type == "xs2":
            self.model = Sequential()
            self.model.add(Dense(64, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(32, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # s1 model
        elif model_type == "s1":
            self.model = Sequential()
            self.model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # s2 model
        elif model_type == "s2":
            self.model = Sequential()
            self.model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(32, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # s3 model
        elif model_type == "s3":
            self.model = Sequential()
            self.model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # s4 model
        elif model_type == "s4":
            self.model = Sequential()
            self.model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(32, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(16, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # s5 model
        elif model_type == "s5":
            self.model = Sequential()
            self.model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(32, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # m1 model
        elif model_type == "m1":
            self.model = Sequential()
            self.model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # m2 model
        elif model_type == "m2":
            self.model = Sequential()
            self.model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # m3 model
        elif model_type == "m3":
            self.model = Sequential()
            self.model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(32, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # l1 model
        elif model_type == "l1":
            self.model = Sequential()
            self.model.add(Dense(512, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(256, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # l2 model
        elif model_type == "l2":
            self.model = Sequential()
            self.model.add(Dense(512, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(256, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # l3 model
        elif model_type == "l3":
            self.model = Sequential()
            self.model.add(Dense(512, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(256, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(32, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # l4 model
        elif model_type == "l4":
            self.model = Sequential()
            self.model.add(Dense(512, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(256, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(32, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(16, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # l5 model
        elif model_type == "l5" or model_type == "l5f":
            self.model = Sequential()
            self.model.add(Dense(512, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(256, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # xl1 model
        elif model_type == "xl1":
            self.model = Sequential()
            self.model.add(Dense(1024, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(512, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(256, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # xl2 model
        elif model_type == "xl2":
            self.model = Sequential()
            self.model.add(Dense(1024, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(512, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(256, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # xl3 model
        elif model_type == "xl3":
            self.model = Sequential()
            self.model.add(Dense(1024, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(512, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(256, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(32, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # undifined model
        else:
            print(f"{bcolors.FAIL}model {model_type} is undifinde\n"
                  f"it will defuat to s1 {bcolors.ENDC}")
            self.model = Sequential()
            self.model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(64, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(len(train_y[0]), activation='softmax'))
        # defining layers end

        # callbacks define
        call_back_list = []
        # wheight and biases config
        if self.w_and_b:
            wandb.config = {
                "learning_rate": learning_rate,
                "epochs": epoch,
                "batch_size": batch_size
            }
            call_back_list.append(WandbCallback())

        # training start
        # SGD optimizer
        if optimizer == "SGD":
            opt = SGD(learning_rate=learning_rate, decay=1e-6, momentum=0.9, nesterov=True)
        # Adama optimizer
        elif optimizer == "Adam":
            opt = Adam(learning_rate=learning_rate)
        # Adamax optimizer
        elif optimizer == "Adamx":
            opt = Adamax(learning_rate=learning_rate)
        # Adagrad optimizer
        elif optimizer == "Adagrad":
            opt = Adagrad(learning_rate=learning_rate)
        else:
            print(f"{bcolors.FAIL}the optimizer {optimizer} is unknown \n"
                  f"it will defualt to Adam optimizer{bcolors.ENDC}")
            opt = Adam(learning_rate=learning_rate)

        # printing summery
        print(self.model.summary())
        print(f"learning rate : {learning_rate}")
        print(f"epoch : {epoch}")
        print(f"validation split : {validation_split}")
        print(f"batch size : {batch_size}")
        print(f"optimizer : {optimizer}")

        self.model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
        self.hist = self.model.fit(np.array(train_x), np.array(train_y), epochs=epoch, batch_size=batch_size,
                                   verbose=1, validation_split=validation_split, callbacks=call_back_list)
        # training ends
        # training info plot
        if accuracy_and_loss_plot:
            history_dict = self.hist.history
            f_acc = history_dict['accuracy']
            f_loss = history_dict['loss']
            f_epochs = range(1, len(f_acc) + 1)
            plt.plot(f_epochs, f_loss, "b", label="Training los")
            f_val_acc = None
            if validation_split != 0:
                f_val_acc = history_dict['val_accuracy']
                f_val_loss = history_dict['val_loss']
                plt.plot(f_epochs, f_val_loss, 'r', label="Validation loss")
                plt.title('Training and validation loss')
            else:
                plt.title('Training loss')
            plt.xlabel('Epochs')
            plt.ylabel('Loss')
            plt.grid()
            plt.legend()
            plt.show()
            plt.plot(f_epochs, f_acc, 'b', label="Training acc")
            if validation_split != 0:
                plt.plot(f_epochs, f_val_acc, 'r', label="Validation acc")
                plt.title("Training and validation accuracy")
            else:
                plt.title("Training accuracy")
            plt.xlabel('Epochs')
            plt.ylabel('Accuracy')
            plt.grid()
            plt.legend(loc="lower right")
            plt.show()
        # time
        if timeIt:
            print(f"training time in sec : {perf_counter() - start_time}")
            print(f"training time in min : {(perf_counter() - start_time) / 60}")
            print(f"training time in hour : {(perf_counter() - start_time) / 3600}")

    def save_model(self, model_name=None):
        if model_name is None:
            self.model.save(f"{self.model_name}.h5", self.hist)
            pickle.dump(self.words, open(f'{self.model_name}_words.pkl', 'wb'))
            pickle.dump(self.classes, open(f'{self.model_name}_classes.pkl', 'wb'))
        else:
            self.model.save(f"{model_name}.h5", self.hist)
            pickle.dump(self.words, open(f'{model_name}_words.pkl', 'wb'))
            pickle.dump(self.classes, open(f'{model_name}_classes.pkl', 'wb'))

    def load_model(self, model_name=None):
        if model_name is None:
            self.words = pickle.load(open(f'{self.model_name}_words.pkl', 'rb'))
            self.classes = pickle.load(open(f'{self.model_name}_classes.pkl', 'rb'))
            self.model = load_model(f'{self.model_name}.h5')
        else:
            self.words = pickle.load(open(f'{model_name}_words.pkl', 'rb'))
            self.classes = pickle.load(open(f'{model_name}_classes.pkl', 'rb'))
            self.model = load_model(f'{model_name}.h5')

    def _clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    def _bag_of_words(self, sentence, words):
        sentence_words = self._clean_up_sentence(sentence)
        bag = [0] * len(words)
        for s in sentence_words:
            for i, word in enumerate(words):
                if word == s:
                    bag[i] = 1
        return np.array(bag)

    def _predict_class(self, sentence, threshold=None):
        if threshold is None:
            threshold = self.model_threshold
        p = self._bag_of_words(sentence, self.words)
        res = self.model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = threshold
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({'intent': self.classes[r[0]], 'probability': str(r[1])})
        return return_list

    def _get_response(self, ints, intents_json):
        try:
            tag = ints[0]['intent']
            list_of_intents = intents_json['intents']
            for i in list_of_intents:
                if i['tag'] == tag:
                    result = random.choice(i['responses'])
                    break
        except IndexError:
            result = "I don't understand!"
        return result

    def _get_tag(self, ints, intents_json):
        result = None
        try:
            tag = ints[0]['intent']
            list_of_intents = intents_json['intents']
            for i in list_of_intents:
                if i['tag'] == tag:
                    result = (i['tag'])
                    break
        except IndexError:
            result = "I don't understand!"
        return result

    def summery(self):
        return self.model.summary()

    def request_tag(self, message, debug_mode=False, threshold=None):
        if debug_mode:
            print(f"message = {message}")
            ints = self._predict_class(message, threshold=threshold)
            print(f"ints = {ints}")
            res = self._get_tag(ints, self.intents)
            print(f"res = {res}")
        else:
            ints = self._predict_class(message, threshold=threshold)
            res = self._get_tag(ints, self.intents)
        return res

    def request_response(self, message, debug_mode=False, threshold=None):
        if debug_mode:
            print(f"message = {message}")
            ints = self._predict_class(message, threshold=threshold)
            print(f"ints = {ints}")
            res = self._get_response(ints, self.intents)
            print(f"res = {res}")
        else:
            ints = self._predict_class(message, threshold=threshold)
            res = self._get_response(ints, self.intents)
        return res

    def get_tag_by_id(self, id):
        pass

    def request_method(self, message):
        pass

    def request(self, message, threshold=None):
        ints = self._predict_class(message, threshold=threshold)

        if ints[0]['intent'] in self.intent_methods.keys():
            self.intent_methods[ints[0]['intent']]()
        else:
            return self._get_response(ints, self.intents)


class JsonIntents:
    def __init__(self, json_file_adrees):
        self.json_file_adress = json_file_adrees
        self.json_file = None
        if json_file_adrees.endswith(".json"):
            self.load_json_intents(json_file_adrees)

    def load_json_intents(self, json_file_adress):
        self.json_file = json.loads(open(json_file_adress).read())

    def add_pattern_app(self, tag=None):
        if tag is None:
            intents = self.json_file
            counter = 0

            for tag in (intents["intents"]):
                while True:
                    new_term = input(intents["intents"][counter]["tag"] + " : ")
                    if new_term.upper() == "D":
                        break
                    elif any(str(obj).lower() == new_term.lower() for obj in intents["intents"][counter]["patterns"]):
                        print("it exist ! ")
                    elif new_term.isspace() or new_term == "":
                        print("type a valid intent ! ")
                    else:
                        intents["intents"][counter]["patterns"] = list(intents["intents"][counter]["patterns"]).__add__(
                            [new_term])
                        print("added")
                counter += 1

            out_file = open(self.json_file_adress, "w")
            json.dump(intents, out_file)
            out_file.close()
            print("intents updated ! ")
            self.load_json_intents(self.json_file_adress)
        else:
            intents = self.json_file
            tag_counter = 0
            for i in (intents["intents"]):
                if intents["intents"][tag_counter]["tag"] == tag:
                    break
                else:
                    tag_counter += 1

            while True:
                new_term = input(intents["intents"][tag_counter]["tag"] + " : ")
                if new_term.upper() == "D":
                    break
                elif any(str(obj).lower() == new_term.lower() for obj in intents["intents"][tag_counter]["patterns"]):
                    print("it exist ! ")
                elif new_term.isspace() or new_term == "":
                    print("type a valid intent ! ")
                else:
                    intents["intents"][tag_counter]["patterns"] = list(
                        intents["intents"][tag_counter]["patterns"]).__add__([new_term])
                    print("added")

            out_file = open(self.json_file_adress, "w")
            json.dump(intents, out_file)
            out_file.close()
            print("intents updated ! ")
            self.load_json_intents(self.json_file_adress)

    def delete_duplicate_app(self):
        intents = self.json_file
        counter = 0

        for tag in (intents["intents"]):
            intents["intents"][counter]["patterns"] = list(
                OrderedDict.fromkeys(intents["intents"][counter]["patterns"]))
            counter += 1

        out_file = open(self.json_file_adress, "w")
        json.dump(intents, out_file)
        out_file.close()
        self.load_json_intents(self.json_file_adress)

    def add_tag_app(self, tag=None, responses=None):
        if tag is None and responses is None:
            json_file = self.json_file
            new_tag = input("what should the tag say ? ")
            responses = []
            while True:
                new_response = input("add a response for it : (d for done) ")
                if new_response.lower() == "d":
                    break
                else:
                    responses.append(new_response)
            json_file["intents"] = list(json_file["intents"]).__add__(
                [{"tag": [new_tag], "patterns": [], "responses": responses}])
            out_file = open(self.json_file_adress, "w")
            json.dump(json_file, out_file)
            out_file.close()
            print("new tag added !")
            self.load_json_intents(self.json_file_adress)
        elif tag is None:
            json_file = self.json_file
            new_tag = input("what should the tag say ? ")
            json_file["intents"] = list(json_file["intents"]).__add__(
                [{"tag": [new_tag], "patterns": [], "responses": responses}])
            out_file = open(self.json_file_adress, "w")
            json.dump(json_file, out_file)
            out_file.close()
            print("new tag added !")
            self.load_json_intents(self.json_file_adress)
        elif responses is None:
            json_file = self.json_file
            new_tag = tag
            responses = []
            while True:
                new_response = input("add a response for it : (d for done) ")
                if new_response.lower() == "d":
                    break
                else:
                    responses.append(new_response)
            json_file["intents"] = list(json_file["intents"]).__add__(
                [{"tag": [new_tag], "patterns": [], "responses": responses}])
            out_file = open(self.json_file_adress, "w")
            json.dump(json_file, out_file)
            out_file.close()
            print("new tag added !")
            self.load_json_intents(self.json_file_adress)
        else:
            json_file = self.json_file
            new_tag = tag
            json_file["intents"] = list(json_file["intents"]).__add__(
                [{"tag": [new_tag], "patterns": [], "responses": responses}])
            out_file = open(self.json_file_adress, "w")
            json.dump(json_file, out_file)
            out_file.close()
            print("new tag added !")
            self.load_json_intents(self.json_file_adress)


class BinaryImageClassificate:
    def __init__(self, data_folder="data", model_name="imageclassification_model", first_class="1", second_class="2"):
        self.optimizer = None
        self.acc = None
        self.re = None
        self.pre = None
        self.first_class = first_class
        self.second_class = second_class
        self.tensorboard_callback = None
        self.logdir = None
        self.model = None
        self.batch = None
        self.test = None
        self.val = None
        self.train = None
        self.test_size = None
        self.val_size = None
        self.train_size = None
        self.data_iterator = None
        self.hist = None
        self.data_folder = data_folder
        self.name = model_name
        self.data = None
        self.oom_avoider()

    def remove_dogy_images(self):
        data_dir = self.data_folder
        image_exts = ['jpeg', 'jpg', 'bmp', 'png']
        for image_class in os.listdir(data_dir):
            for image in os.listdir(os.path.join(data_dir, image_class)):
                image_path = os.path.join(data_dir, image_class, image)
                try:
                    img = cv2.imread(image_path)
                    tip = imghdr.what(image_path)
                    if tip not in image_exts:
                        print('Image not in ext list {}'.format(image_path))
                        os.remove(image_path)
                except Exception as e:
                    print('Issue with image {}'.format(image_path))
                    os.remove(image_path)

    def load_data(self):
        self.data = tf.keras.utils.image_dataset_from_directory(self.data_folder)
        self.data_iterator = self.data.as_numpy_iterator()
        self.batch = self.data_iterator.next()
        print(f"{bcolors.OKGREEN}loading data succsesfuly{bcolors.ENDC}")

    def scale_data(self, model_type="s1"):
        self.data = self.data.map(lambda x, y: (x / 255, y))
        print(f"{bcolors.OKGREEN}scaling data succsesfuly{bcolors.ENDC}")

    def augmanet_data(self, model_type="s1"):
        if "a" in model_type:
            data_augmentation = Sequential([
                tf.keras.layers.RandomFlip(mode="horizontal"),
                tf.keras.layers.RandomRotation((-0.3, 0.3)),
                tf.keras.layers.RandomZoom(height_factor=(-0.1, 0.1)),
                tf.keras.layers.RandomBrightness(factor=0.2)
            ])
            self.data = self.data.map(lambda x, y: (data_augmentation(x, training=True), y),
                                      num_parallel_calls=tf.data.AUTOTUNE)
            print(f"{bcolors.OKGREEN}augmenting data succsesfuly{bcolors.ENDC}")

    def split_data(self):
        self.train_size = int(len(self.data) * .8)
        self.val_size = int(len(self.data) * .2)
        self.test_size = int(len(self.data) * .0)
        self.train = self.data.take(self.train_size)
        self.val = self.data.skip(self.train_size).take(self.val_size)
        self.test = self.data.skip(self.train_size + self.val_size).take(self.test_size)
        print(f"{bcolors.OKGREEN}spliting data succsesfuly{bcolors.ENDC}")

    def prefetching_data(self):
        self.train = self.train.prefetch(tf.data.AUTOTUNE)
        self.val = self.val.prefetch(tf.data.AUTOTUNE)
        self.test = self.test.prefetch(tf.data.AUTOTUNE)
        print(f"{bcolors.OKGREEN}prefetching data succsesfuly{bcolors.ENDC}")

    @staticmethod
    def make_small_Xception_model(input_shape, num_classes=2):
        inputs = keras.Input(shape=input_shape)

        x = tf.compat.v1.keras.layers.Rescaling(1.0 / 255)(inputs)
        x = Conv2D(128, 3, strides=2, padding="same")(x)
        x = tf.compat.v1.keras.layers.BatchNormalization()(x)
        x = Activation("relu")(x)

        previous_block_activision = x
        for size in [256, 512, 728]:
            x = Activation("relu")(x)
            x = layers.SeparableConv2D(size, 3, padding="same")(x)
            x = tf.compat.v1.keras.layers.BatchNormalization()(x)
            x = Activation("relu")(x)
            x = layers.SeparableConv2D(size, 3, padding="same")(x)
            x = tf.compat.v1.keras.layers.BatchNormalization()(x)
            x = MaxPooling2D(3, strides=2, padding="same")(x)
            # residual
            residual = Conv2D(size, 1, strides=2, padding="same")(previous_block_activision)
            x = layers.add([x, residual])
            previous_block_activision = x

        x = layers.SeparableConv2D(1024, 3, padding="same")(x)
        x = tf.compat.v1.keras.layers.BatchNormalization()(x)
        x = Activation("relu")(x)
        x = GlobalAveragePooling2D()(x)
        if num_classes == 2:
            activision = "sigmoid"
            units = 1
        else:
            activision = "softmax"
            units = num_classes
        x = Dropout(0.5)(x)
        outputs = Dense(units, activation=activision)(x)
        return keras.Model(inputs, outputs)

    def build_model(self, optimizer, model_type="s1"):
        print(f"model type : {model_type}")
        succsesful = False
        if model_type == "s1" or model_type == "s1a":
            self.model = Sequential()
            self.model.add(Conv2D(16, (3, 3), 1, activation='relu', input_shape=(256, 256, 3)))
            self.model.add(MaxPooling2D())
            self.model.add(Conv2D(32, (3, 3), 1, activation='relu'))
            self.model.add(MaxPooling2D())
            self.model.add(Conv2D(16, (3, 3), 1, activation='relu'))
            self.model.add(MaxPooling2D())
            self.model.add(Flatten())
            self.model.add(Dense(256, activation='relu'))
            self.model.add(Dense(1, activation='sigmoid'))
            succsesful = True

        elif model_type == "s2":
            self.model = Sequential()
            self.model.add(Conv2D(16, (3, 3), 1, activation='relu', input_shape=(256, 256, 3)))
            self.model.add(MaxPooling2D())
            self.model.add(Conv2D(32, (3, 3), 1, activation='relu'))
            self.model.add(MaxPooling2D())
            self.model.add(Conv2D(32, (3, 3), 1, activation='relu'))
            self.model.add(MaxPooling2D())
            self.model.add(Flatten())
            self.model.add(Dense(256, activation='relu'))
            self.model.add(Dense(1, activation='sigmoid'))
            succsesful = True

        elif model_type == "s3":
            self.model = Sequential()
            self.model.add(Conv2D(32, (3, 3), 1, activation='relu', input_shape=(256, 256, 3)))
            self.model.add(MaxPooling2D())
            self.model.add(Conv2D(32, (3, 3), 1, activation='relu'))
            self.model.add(MaxPooling2D())
            self.model.add(Conv2D(64, (3, 3), 1, activation='relu'))
            self.model.add(MaxPooling2D())
            self.model.add(Dropout(0.4))
            self.model.add(Flatten())
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dense(1, activation='sigmoid'))
            succsesful = True

        elif model_type == "m1":
            self.model = Sequential()
            self.model.add(Conv2D(32, (3, 3), 1, padding="same", activation='relu', input_shape=(256, 256, 3)))
            self.model.add(Conv2D(32, (3, 3), 1, activation='relu'))
            self.model.add(MaxPooling2D())
            self.model.add(Dropout(0.25))
            self.model.add(Conv2D(64, (3, 3), 1, padding="same", activation='relu'))
            self.model.add(Conv2D(64, (3, 3), 1, activation='relu'))
            self.model.add(MaxPooling2D())
            self.model.add(Dropout(0.25))
            self.model.add(Flatten())
            self.model.add(Dense(512, activation='relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(1, activation='sigmoid'))
            succsesful = True
        elif model_type == "x1":
            self.model = self.make_small_Xception_model(input_shape=(256, 256, 3), num_classes=2)
        else:
            print(f"{bcolors.FAIL}model {model_type} is undifinde\n"
                  f"it will defuat to s1 {bcolors.ENDC}")
            self.build_model(model_type="s1", optimizer=optimizer)
            succsesful = False

        if succsesful:
            print(self.model.summary())

        self.model.compile(optimizer=optimizer, loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])

    @staticmethod
    def build_optimizer(learning_rate=0.00001, optimizer_type="adam"):
        opt = None
        if optimizer_type.lower() == "adam":
            opt = Adam(learning_rate=learning_rate)
        return opt

    def seting_logdir(self):
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        if self.logdir is None:
            if Path('new_folder').is_dir():
                self.logdir = "logs"
            else:
                path = os.path.join(parent_dir, "logs")
                os.mkdir(path)
                self.logdir = "logs"
        else:
            if Path(self.logdir).is_dir():
                pass
            else:
                path = os.path.join(parent_dir, self.logdir)
                os.mkdir(path)

    def train_model(self, epochs=20, model_type="s1", logdir=None, optimizer_type="adam", learning_rate=0.00001,
                    class_weight=None, prefetching=False, plot_model=True):
        if type(epochs) is not int:
            print(f"{bcolors.FAIL}epochs should be an int\n"
                  f"it will defualt to 20{bcolors.ENDC}")
            epochs = 20
        self.oom_avoider()
        self.remove_dogy_images()
        self.load_data()
        self.scale_data(model_type=model_type)
        self.augmanet_data(model_type=model_type)
        self.split_data()
        if prefetching:
            self.prefetching_data()
        self.logdir = logdir
        self.seting_logdir()
        self.optimizer = self.build_optimizer(optimizer_type=optimizer_type, learning_rate=learning_rate)
        self.build_model(model_type=model_type, optimizer=self.optimizer)
        if plot_model:
            tf.keras.utils.plot_model(self.model, show_shapes=True, show_layer_activations=True)
        self.tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=self.logdir)
        self.hist = self.model.fit(self.train, epochs=epochs, validation_data=self.val,
                                   callbacks=[self.tensorboard_callback], class_weight=class_weight)
        self.plot_acc()
        self.plot_loss()

    def plot_loss(self):
        fig = plt.figure()
        plt.plot(self.hist.history['loss'], color='teal', label='loss')
        plt.plot(self.hist.history['val_loss'], color='orange', label='val_loss')
        fig.suptitle('Loss', fontsize=20)
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()

    def plot_acc(self):
        fig = plt.figure()
        plt.plot(self.hist.history['accuracy'], color='teal', label='accuracy')
        plt.plot(self.hist.history['val_accuracy'], color='orange', label='val_accuracy')
        fig.suptitle('Accuracy', fontsize=20)
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()

    def save_model(self, model_file_name=None):
        if model_file_name is None:
            model_file_name = self.name
        self.model.save(f"{model_file_name}.h5")

    def load_model(self, name="imageclassification_model"):
        self.model = load_model(f"{name}.h5")

    @staticmethod
    def oom_avoider():
        gpus = tf.config.experimental.list_physical_devices("GPU")
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)

    def predict_from_files_path(self, image_file_path):
        img = cv2.imread(image_file_path)
        resize = tf.image.resize(img, (256, 256))
        yhat = self.model.predict(np.expand_dims(resize / 255, 0))
        if yhat > 0.5:
            return self.first_class
        else:
            return self.second_class

    def predict_from_imshow(self, img):
        resize = tf.image.resize(img, (256, 256))
        yhat = self.model.predict(np.expand_dims(resize / 255, 0))
        if yhat > 0.5:
            return self.first_class
        else:
            return self.second_class

    def evaluate_model(self):
        self.pre = Precision()
        self.re = Recall()
        self.acc = BinaryAccuracy()
        for batch in self.test.as_numpy_iterator():
            X, y = batch
            yhat = self.model.predict(X)
            self.pre.update_state(y, yhat)
            self.re.update_state(y, yhat)
            self.acc.update_state(y, yhat)
        return [self.pre.result(), self.re.result(), self.acc.result()]

    def realtime_prediction(self):
        # Variables declarations
        frame_count = 0
        last = 0
        font = cv2.FONT_HERSHEY_TRIPLEX
        font_color = (255, 255, 255)
        vs = VideoStream(src=0).start()
        while True:
            frame = vs.read()
            frame_count += 1

            # Only run every 10 frames
            if frame_count % 10 == 0:
                prediction = self.predict_from_imshow(frame)
                # Change the text position depending on your camera resolution
                cv2.putText(frame, prediction, (20, 400), font, 1, font_color)

                if frame_count > 20:
                    fps = vs.stream.get(cv2.CAP_PROP_FPS)
                    fps_text = "fps: " + str(np.round(fps, 2))
                    cv2.putText(frame, fps_text, (460, 460), font, 1, font_color)

                cv2.imshow("Frame", frame)
                last += 1

                # if the 'q' key is pressed, stop the loop
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        # cleanup everything
        vs.stop()
        cv2.destroyAllWindows()
        print("Done")

    def realtime_face_prediction(self):
        detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
        camera = cv2.VideoCapture(0)
        # keep looping
        while True:
            # grab the current frame
            (grabbed, frame) = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frameClone = frame.copy()
            rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                                              minNeighbors=5, minSize=(10, 10),
                                              flags=cv2.CASCADE_SCALE_IMAGE)
            # loop over the face bounding boxes
            for (fX, fY, fW, fH) in rects:
                # extract the ROI of the face from the grayscale image,
                # resize it to a fixed 28x28 pixels, and then prepare the
                # ROI for classification via the CNN
                roi = frame[fY:fY + fH, fX:fX + fW]
                roi = cv2.resize(roi, (256, 256))
                roi = roi.astype("float") / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                prediction = str(self.model.predict(roi))
                label = prediction
                cv2.putText(frameClone, label, (fX, fY - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                              (0, 0, 255), 2)
            # show our detected faces along with smiling/not smiling labels
            cv2.imshow("Face", frameClone)
            # if the 'q' key is pressed, stop the loop
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        # cleanup the camera and close any open windows
        camera.release()
        cv2.destroyAllWindows()


class PLinearRegression:

    def __init__(self, data=None, x_axes1=None, y_axes1=None, model_name="test model"):
        self.y_avarage = None
        self.x_avarage = None
        self.data = data
        self.x_axes1 = x_axes1
        self.y_axes1 = y_axes1
        self.name = model_name
        self.result_a = None
        self.result_b = None

    def prepare_data(self):
        if self.data is None:
            self.data = np.array([self.x_axes1, self.y_axes1])

    def getting_avarages(self):
        self.x_avarage = np.sum(a=self.data[0]) / (len(self.data[0]))
        self.y_avarage = np.sum(a=self.data[1]) / (len(self.data[1]))

    def counting_up_down(self, a):
        uper = 0
        lower = 0
        for i in range(len(self.data[0])):
            x = self.data[0, i]
            if x < self.x_avarage:
                predicted_y = (a * x) + self.y_avarage - (a * self.x_avarage)
                actual_y = self.data[1, i]
                if predicted_y > actual_y:
                    uper += 1
                elif predicted_y < actual_y:
                    lower += 1
        result = None
        # 0 mean lower is more
        # 1 mean equal
        # 2 mean uper is more
        if lower > uper:
            result = 0
        elif lower == uper:
            result = 1
        else:
            result = 2
        return result, uper, lower

    def plot_input_data(self):
        plt.scatter(self.data[0], self.data[1])
        plt.grid()
        plt.show()

    def plot_prediction(self):
        plt.scatter(self.data[0], self.data[1])
        plt.grid()
        x_min = np.amin(self.data[0])
        x_max = np.amax(self.data[0])
        x = np.linspace(x_min, x_max, 100)
        y = (x * self.result_a) + self.result_b
        plt.plot(x, y, color="red")
        plt.show()

    def save_model_to_csv(self, file_dir="test_model.csv"):
        model_dict = [{"a": self.result_a, "b": self.result_b}]
        with open(file_dir, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["a", "b"])
            writer.writeheader()
            writer.writerows(model_dict)

    def load_model_from_csv(self, file_dir="test_model.csv"):
        with open(file_dir, "r") as csvfile:
            csvfile = csv.reader(csvfile)
            counter = 0
            for lines in csvfile:
                counter += 1
                if counter == 3:
                    self.result_a = float(lines[0])
                    self.result_b = float(lines[1])
                    print("model loaded succsesfully")
                    print(f"Line info : {self.result_a} X + {self.result_b}")

    def make_prediction(self, x):
        result = x * self.result_a + self.result_b
        return result

    @timeit
    def algorythm_1(self, start_step=None, verbose=1, training_steps=10000, version1_1=False, plot_result=True):
        if start_step is None:
            start_step = 0.1
        step = start_step
        a = 1
        for _ in range(training_steps):
            self.counting_up_down(a=a)
            result, uper, lower = self.counting_up_down(a=a)
            if lower > uper:
                a -= step
            elif lower == uper:
                break
            elif lower < uper:
                a += step
            if verbose == 1:
                print(f"uper : {uper}")
                print(f"lower : {lower}")
                print(f"a : {a}")
                print(f"result : {result}")
                print("-----------------")
            if version1_1:
                step *= 0.999
        self.result_a = a
        self.result_b = self.y_avarage - (a * self.x_avarage)
        print(f"a = {self.result_a}\n"
              f"b = {self.result_b}")
        if plot_result:
            self.plot_prediction()

    @timeit
    def algorythm_2(self, training_step=10000, learning_rate=0.01, verbose=1, plot_result=True):
        x = np.array(self.data[0])
        y = np.array(self.data[1])
        n_samples = len(x)
        weight = 0
        bias = 0

        for _ in range(training_step):
            y_pred = np.dot(x, weight) + bias

            dw = np.dot(x.T, (y_pred - y)) / n_samples * 2
            db = np.sum(y_pred - y) / n_samples * 2

            weight = weight - learning_rate * dw
            bias = bias - learning_rate * db
            if verbose == 1:
                print(f"a : {weight}")
                print(f"b : {bias}")
                print("-----------------")
        self.result_a = float(weight)
        self.result_b = float(bias)
        print(f"a = {self.result_a}\n"
              f"b = {self.result_b}")
        if plot_result:
            self.plot_prediction()

    def train_model(self, algorythm="1", training_steps=10000, start_step=None, verbose=1, plot_input_data=True,
                    learning_rate=0.01, plot_result=True):
        self.prepare_data()
        if plot_input_data:
            self.plot_input_data()
        self.getting_avarages()
        if algorythm == "1" or algorythm == "1.1":
            version1_1 = False
            if algorythm == "1.1":
                version1_1 = True
            self.algorythm_1(start_step=start_step, verbose=verbose,
                             training_steps=training_steps,
                             version1_1=version1_1, plot_result=plot_result)
            return self.result_a, self.result_b
        elif algorythm == "2":
            self.algorythm_2(training_step=training_steps, learning_rate=learning_rate, plot_result=plot_result)
        else:
            print(f"{bcolors.FAIL}this algorythm is not defiined !{bcolors.ENDC}")
            return

    @staticmethod
    def data_creator_scatter(a, b, noise_range, x_range, data_number):
        x_axes1 = []
        for _ in range(data_number):
            i = random() * x_range
            x_axes1.append(i)

        x_axes1 = np.array(x_axes1)
        y_axes1 = (x_axes1 * a) + b

        for i in range(len(y_axes1)):
            y_axes1[i] = y_axes1[i] + ((random() - 0.5) * noise_range)
        return np.array([x_axes, y_axes])


class PKNN:

    def __init__(self, k=3):
        self.y_train = None
        self.x_train = None
        self.k = k

    def fit(self,x ,y):
        self.x_train = x
        self.y_train = y

    def predict(self, x):
        predictions = [self._predict(curent_x) for curent_x in x]
        return predictions

    def _predict(self, x):
        # fasele
        distances = [Pfunctions.ecualidean_distance(x, x_train1) for x_train1 in self.x_train]
        # nazdik tarin k
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        # majority vote
        most_common = Counter(k_nearest_labels).most_common()
        return most_common
