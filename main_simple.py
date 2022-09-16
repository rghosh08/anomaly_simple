import numpy as np

class Anomaly():
    '''
        Detect Time Series Anomalies
    '''

    def __init__(self, data):
        '''
            Arg:
                data (list)
        '''
        self.data = data
    
    def baseline(self, param=4.5):
        '''
            Computing upper and lower thresholds
            Arg:
                param (float)
            Returns:
                an object: upper and lower threshold values
        '''
        estimate = np.median(np.log(self.data))
        scale = np.std(np.log(param * np.array(self.data)))
        lower_threshold = estimate -  scale 
        upper_threshold = estimate +  scale

        return {
                'lower_threshold': lower_threshold, 
                'upper_threshold': upper_threshold
            }
        
    def anomaly_decision(self):
        '''
            Making decision whether a point is an anomaly
            Returns:
                a list with False (non-anomaly) or True (anomaly)
        '''
        upper_decision = np.log(self.data) > self.baseline()['upper_threshold'] 
        lower_decision = np.log(self.data) < self.baseline()['lower_threshold']
        decision = [False if upper_decision[i] == False and lower_decision[i] == False else True for i in range(len(self.data))]

        return decision


   