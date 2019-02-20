from allennlp.predictors.predictor import Predictor
import sys


class Correference_Resolver:
    def __init__(self,
                 input_sentence="Paul Allen Tohmas was born on January 21, 1953, in Seattle, Washington, to Kenneth Sam Allen and Edna Faye Allen. Allen attended Lakeside School, a private school in Seattle, where he befriended Bill Gates, two years younger, with whom he shared an enthusiasm for computers. Paul and Bill used a teletype terminal at their high school, Lakeside, to develop their programming skills on several time-sharing computer systems."):

        try:
            self.predictor = Predictor.from_path("models/coref-model-2018.02.05.tar.gz")
            self.dict = (self.predictor.predict(document=input_sentence))
        except Exception as e:
            print('Error in loading model or %s , Exiting', e)
            sys.exit()

    def coreference_resolution(self):
        for k, v in self.dict.items():
            if k == 'document':
                token_Sent = v
            if k == 'clusters':
                dict_list = {}
                for list in v:
                    key = (list[0])
                    value = (list[1:])
                    dict_list[tuple(key)] = value
        dict_list["words"] = token_Sent
        return dict_list


if __name__ == '__main__':
    corref = Correference_Resolver()
    print(corref.coreference_resolution())
