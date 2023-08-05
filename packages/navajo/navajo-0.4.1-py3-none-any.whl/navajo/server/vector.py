import numpy as np

def aggregate_embeddings(embeddings): # TODO improve aggregation methods
    vecs = np.array(embeddings)
    avg = np.mean(vecs, axis=0)
    return (avg / np.linalg.norm(avg)).tolist()

def cosine_sim(vec0, vec1):
    if isinstance(vec0, list):
        vec0 = np.array(vec0)
    if isinstance(vec1, list):
        vec1 = np.array(vec1)
    sim = np.dot(vec0, vec1) / (np.linalg.norm(vec0) * np.linalg.norm(vec1))
    return sim

def unique_elements(lst):
    seen = set()
    unique_lst = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_lst.append(item)

    return unique_lst

def _running_average():
    total = np.zeros_like((yield))
    count = 0

    while True:
        x = yield np.divide(total, count, out=np.zeros_like(total), where=count>0)
        total += x
        count += 1

class VectorRunningAverage(object):
    def __init__(self, size=512):
        self.avg = _running_average()
        next(self.avg)

        zeros = np.zeros(size)
        self.avg.send(zeros)
        self.current = zeros

    def send(self, arr):
        if isinstance(arr, list):
            arr = np.array(arr)
        if arr.size == 0:
            return

        arr = arr.astype(float)
        self.current = self.avg.send(arr).tolist()

    def normalize(self):
        if np.all(self.current == 0):
            return []
        n = self.current / np.linalg.norm(self.current)
        return n.tolist()
