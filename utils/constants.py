DEFAULT_NETWORK_INIT = 'sending_data'
DEFAULT_NETWORK_INIT_MESSAGE = {
    'message': DEFAULT_NETWORK_INIT
}

DEFAULT_NETWORK_CHUNK = 'network_chunk'
DEFAULT_NETWORK_MESSAGE_CHUNK = {
    'message': DEFAULT_NETWORK_CHUNK
}

DEFAULT_NETWORK_END = 'end_transmission'
DEFAULT_NETWORK_END_MESSAGE = {
    'message': DEFAULT_NETWORK_END
}

DEFAULT_IMAGE_INIT = 'sending_data'
DEFAULT_IMAGE_INIT_MESSAGE = {
    'message': DEFAULT_IMAGE_INIT
}

DEFAULT_IMAGE_CHUNK = 'chunk'
DEFAULT_IMAGE_MESSAGE_CHUNK = {
    'message': DEFAULT_IMAGE_CHUNK
}

DEFAULT_IMAGE_END = 'done'
DEFAULT_IMAGE_END_MESSAGE = {
    'message': DEFAULT_IMAGE_END
}

SEND_CLIENT_DATA = 'begin_sending_data'
SEND_CLIENT_DATA_MESSAGE = {
    'message': SEND_CLIENT_DATA
}

RESET_CLIENT = 'reset_client'
RESET_CLIENT_MESSAGE = {
    'message': RESET_CLIENT
}


SUBSCRIBE_TO_CLUSTER = 'subscribe_to_cluster'

'''
Section for Topics
'''

NEW_CLIENT_INITIALIZATION_TOPIC = 'client_ids'

CLUSTER_TOPIC_NAME = 'cluster_topic_name'
