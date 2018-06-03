import twitter
import json


key_file = "twitter.key"


def get_key():
    keys = json.load(open(key_file))
    return keys


class Post(twitter.models.Status):

    def __init__(self):
        self.items = {}
        super().__init__()

    def message(self, message):
        self.items['message'] = message

    def reply_to(self, post_id):
        self.items['reply_id'] = post_id


class combined_api():

    def __init__(self):
        self.keys = get_key()
        self.api = twitter.Api(consumer_key=self.keys['consumer'],
                               consumer_secret=self.keys['consumer_secret'],
                               access_token_key=self.keys['access'],
                               access_token_secret=self.keys['access_secret']
                               )

    def _post(self, content, attachments):
        try:
            self.api.PostUpdate(content)
        except BaseException:
            pass

    def _delete(self, post_id):
        try:
            self.api.DestroyStatus(post_id)
        except BaseException:  # post not found, or whatever
            pass

    def _reply(self, message, post_id, exclude_reply_user_ids=None):
        self.api.PostUpdate(message,
                            in_reply_to_status_id=post_id,
                            exclude_reply_user_ids=exclude_reply_user_ids)  # NOQA

    def _forward(self, post_id):
        self.api.PostRetweet(post_id)

    def _create_post(self, msg, content=None,  content_type=None):
        ''' construct a post from context, media, ...'''
        # TODO: media handling
        self.api.PostMedaMedtadata(media_id, alt_text=None)
