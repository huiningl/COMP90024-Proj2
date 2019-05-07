from genderizer.genderizer import Genderizer
from naiveBayesClassifier import tokenizer
import genderizer
import naiveBayesClassifier

class GenderDector:

    @staticmethod
    def infer_gender(text=''):
        Genderizer.detect(text=text)