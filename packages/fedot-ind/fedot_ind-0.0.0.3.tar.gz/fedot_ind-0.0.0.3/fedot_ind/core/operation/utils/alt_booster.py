from fedot.api.main import Fedot


class OneStageBooster:
    def __init__(self, true_target, base_predict, features):
        self.true_target = true_target
        self.base_predict = base_predict
        self.features = features
        self.model = None
        self.model_hyperparams = dict(problem='regression', seed=42,
                                      timeout=5, max_depth=10,
                                      max_arity=4, cv_folds=2,
                                      logging_level=20, n_jobs=2)

    def fit(self):
        self.model = Fedot(**self.model_hyperparams)
        diff_target = self.true_target - self.base_predict
        self.model.fit(self.features, diff_target)

    def predict(self, features):
        return self.model.predict(features)

    def score(self, predict, target):
        ...

