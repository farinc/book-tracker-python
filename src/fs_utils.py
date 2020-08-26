import os

class FsUtils:

    @classmethod
    def getBatches(cls) -> list:
        batches = []
        for b in os.listdir("./Books"):
            if os.path.isdir("./Books/" +b):
                batches.append(b)
        return batches

    @classmethod
    def getEntriesFromBatch(cls, batchID: int) -> list:
        p = "./Books/batch_{batchID}".format(batchID=batchID)
        entries = []
        for e in os.listdir(p):
            if os.path.isfile(p.join(e)):
                entries.append(e)
        return entries

    @classmethod
    def createBatch(cls, batchID):
        os.mkdir("./Books/batch_{id}/".format(id=batchID))


