code_meaning = {
    0: "No match for league to train",
    1: "No match for team to train",
    2: "No enough data for training or predicting",
    3: "Error during training",
    4: "No machine learning algorithm found",
    5: "Bad Representation"
}


class MLException(Exception):

    def __init__(self, code):
        super(MLException, self).__init__()
        self.code = code

    def get_code(self):
        return self.code

    def __str__(self):
        return "MLException, CODE ["+str(self.code)+"]: "+code_meaning[self.code]
