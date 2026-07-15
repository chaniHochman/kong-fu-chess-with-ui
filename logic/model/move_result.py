class MoveResult:
    def __init__(self, success: bool, reason: str):
        self.success = success
        self.reason = reason

    # def __bool__(self):
        
    #     return self.success

    # def __repr__(self):
    #     return f"MoveResult(success={self.success}, reason='{self.reason}')"