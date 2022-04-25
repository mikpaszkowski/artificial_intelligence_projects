
class RegressionMetric:

    def __init__(self, r2_score_val, MSE, MAE, ME, MPD, EVC):
        self.r2_score = r2_score_val
        self.MSE = MSE
        self.MAE = MAE
        self.ME = ME
        self.MPD = MPD
        self.EVC = EVC