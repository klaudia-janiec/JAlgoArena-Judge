from enum import Enum

class StatusCode(Enum):
    ACCEPTED = 2
    WRONG_ANSWER = 3
    RUNTIME_ERROR = 5
    TIME_LIMIT_EXCEEDED = 6
    MEMORY_LIMIT_EXCEEDED = 7
    OUTPUT_LIMIT_EXCEEDED = 8
    RESTRICTED_CALL = 9
