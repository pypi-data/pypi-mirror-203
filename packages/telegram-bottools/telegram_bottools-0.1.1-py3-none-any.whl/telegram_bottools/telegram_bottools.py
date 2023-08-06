import requests

def send_message(chat_id, token, message, parse_mode='html'):
    """Send message to Telegram BOT

    Args:
        chat_id (int): chat_id number: -111111
        token [str]: Token to HTTP API: 11111111:AAAAAAAAA
        message (str): Message 
        parse_mode (str, optional): [Message format 'html' or 'markdown']. Defaults to 'html'.

    Returns:
        str : Response Status Code
    """
    data = {'chat_id':chat_id, 'text':message, 'parse_mode':parse_mode}
    response = requests.post('https://api.telegram.org/bot' + token + '/sendMessage', data)

    return response.status_code


def send_image(chat_id, token, image_url):
    """Send message to Telegram BOT

    Args:
        chat_id (int): chat_id number: -111111
        token [str]: Token to HTTP API: 11111111:AAAAAAAAA
        image_url (str): Image url

    Returns:
        str : Response Status Code
    """
    data = {'chat_id':chat_id, 'photo':image_url}
    response = requests.post('https://api.telegram.org/bot' + token + '/sendPhoto', data)

    return response.status_code


def send_document(chat_id, token, document_url, file_description, parse_mode='html'):
    """Send message to Telegram BOT

    Args:
        chat_id (int): chat_id number: -111111
        token [str]: Token to HTTP API: 11111111:AAAAAAAAA
        document_url (str): Document url
        file_description (str): File Description
        parse_mode (str): (Default=html) Use html or markdown

    Returns:
        str : Response Status Code
    """
    data = {'chat_id':chat_id, 'document':document_url, 'caption':file_description, 'parse_mode':parse_mode}
    response = requests.post('https://api.telegram.org/bot' + token + '/sendDocument', data)

    return response.status_code