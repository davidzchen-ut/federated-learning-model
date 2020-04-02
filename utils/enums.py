from enum import Enum


class LearningType(Enum):
    CENTRALIZED = 1
    FEDERATED = 2


class ClientState(Enum):
    STALE = 1
    SENDING = 2
    FINISHED = 3


class AggregationScheme(Enum):
    AVERAGE = 1
    WEIGHTED_AVERAGE = 2
