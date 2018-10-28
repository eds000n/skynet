import abc

class MappingAlgorithm(abc.ABC):
    self.time_limit = -1
    self.max_memory = 0
    self.name = ""

    @abc.abstractmethod
    def run(self):
        pass

    def __init__(self, time_limit=-1, name="")
        self.time_limit = time_limit
        self.name = name

class DirectMapping(MappingAlgorithm):
    def run(self):
        start = time.time()
        #input_dataset = ["google", "facebook"]
        #input_dataset = ["google", "facebook", "afsdfadsfad", "affinia group inc", "fremont luxury imports", "advantus capital management", "angeles field partners llc", "assembly & test worldwide l"]
        input_dataset = getDs2()
        labels = getLabels2()
        hashedDS = {}
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for internal_ds in internal_dataset:
            hashedDS[internal_ds]=1
        counter = 0
        for input_ds in input_dataset:
            if input_ds in hashedDS:
                counter +=1
                tp += 1
            else:
                tn += 1
        end = time.time()
        memory = sys.getsizeof(hashedDS)
        [accuracy, precision, recall, f1score]=getMetrics(tp, tn, fp, fn)
        return { 'algorithm': 'directmatch', 'coverage': counter*100.0/len(input_dataset), 'time': end-start , 'memory': memory, 'accuracy': accuracy, 'precision': precision, 'recall': recall, 'f1score': f1score }



