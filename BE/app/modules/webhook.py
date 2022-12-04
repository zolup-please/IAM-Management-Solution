import requests

class Webhook:
    def __init__(self, data: dict):
        self.WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
        self.data = data

    def send(self):
        result = requests.post(self.WEBHOOK_URL, json = self.data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return err
        else:
            return {"status code":result.status_code}
        

if __name__ == '__main__':
    import os

    from dotenv import load_dotenv

    load_dotenv()

    # How to use webhook module
    fake_data = {
        "content" : "message content",
        "embeds" : [
            {
                "title" : "embed title",
                "description" : "text in embed"
            }
        ]
    }

    hook = Webhook(fake_data)
    hook.send()