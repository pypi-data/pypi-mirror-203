import azure.functions as func
import typeguard

from warpzone.enums.topicenum import Topic
from warpzone.function import integrations


class OutputProcessor:
    """Post-processing output binding"""

    return_type = None

    def process(self, value):
        return value


class MessageOutput(OutputProcessor):
    def __init__(self, topic: Topic):
        typeguard.check_type(topic, Topic)
        self.topic = topic


class DataMessageOutput(MessageOutput):
    def process(self, data_msg):
        integrations.send_data(data_msg, self.topic)


class EventMessageOutput(MessageOutput):
    def process(self, event_msg):
        integrations.send_event(event_msg, self.topic)


class HttpOutput(OutputProcessor):
    return_type = func.HttpResponse

    def process(self, resp):
        return resp


class NoneOutput(OutputProcessor):
    pass
