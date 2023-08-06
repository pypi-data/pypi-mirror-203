class CheckpointCounter:
    from typing import Callable
    def __init__(self, checkpointAmount: int, OnEvent_ReachedCheckpoint: Callable[[int], None] = None):

        self.count = 0
        self.checkpointAmount = checkpointAmount
        self._nextCheckpoint = self._calculateNextCheckpoint()
        self._reachedCheckpoint = False

        self._OnEvent_ReachedCheckpoint = OnEvent_ReachedCheckpoint

    def _calculateNextCheckpoint(self):
        countLeftToNextCheckpoint = self.checkpointAmount - (self.count % self.checkpointAmount)
        return self.count + countLeftToNextCheckpoint

    def _CheckpointControl(self):
        if(self._nextCheckpoint <= self.count):
            self._reachedCheckpoint = True
            self._nextCheckpoint = self._calculateNextCheckpoint()
            if(self._OnEvent_ReachedCheckpoint is not None):
                self._OnEvent_ReachedCheckpoint(self.count)
        return

    def increment(self, count=1):
        self.count += count
        self._CheckpointControl()
        return
    
    def Update(self, newCount:int):
        self.count = newCount
        self._CheckpointControl()

    def HasCheckpoint(self):
        if(self._reachedCheckpoint):
            self._reachedCheckpoint = False
            return True
        return False
        
