import requests
import json

class WhatsAppAPI:
    def __init__(self, api_key: str, phone_number_id: int or str, api_version: str = 'v16.0', API_URL: str = 'https://graph.facebook.com')->None:
        self.api_key: str = api_key
        self.phone_number_id: int = phone_number_id
        self.headers: dict = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {api_key}'
        }
        self.API_URL: str = API_URL
        self.api_version: str = api_version
        self.fixed_payload = {
            "messaging_product": "whatsapp",
        }

    def send_text_message(self, phone_number: str, message: str):
        url = f'{self.API_URL}/{self.api_version}/{self.phone_number_id}/messages'
        payload = json.dumps({
            **self.fixed_payload,
            "recipient_type": "individual",
            "to": phone_number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message
            }
        })
        response = requests.post(
            url,
            headers=self.headers,
            data=payload
        )
        return response.status_code
    
    def send_reply_to_text_message(self, phone_number: str, message: str, message_id: str):
        url = f'{self.API_URL}/{self.api_version}/{self.phone_number_id}/messages'
        payload = json.dumps({
            **self.fixed_payload,
            "recipient_type": "individual",
            "to": phone_number,
            "context": {
                "message_id": message_id
            },
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message
            }
        })
        response = requests.post(
            url,
            headers=self.headers,
            data=payload
        )
        return response.status_code
