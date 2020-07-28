from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from .models import Tweet
# Create your tests here.
User = get_user_model()


class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="someuser", password='somepassword')
        Tweet.objects.create(content="my first tweet", user=self.user)
        Tweet.objects.create(content="my first tweet", user=self.user)
        Tweet.objects.create(content="my first tweet", user=self.user)
        self.currentCount = Tweet.objects.all().count()

    def test_tweet_created(self):
        tweet_obj = Tweet.objects.create(content="my second tweet", user=self.user)
        self.assertEqual(tweet_obj.id, 4)
        self.assertEqual(tweet_obj.user, self.user)
        # self.assertEqual(1, 2)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/api/tweets/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        print(response.json())

    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/", {"id":1, "action":"like"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 1)
        print(response.json())
        # self.assertEqual(len(response.json()), 3)

    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/", {"id":2, "action":"like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/tweets/action/", {"id":2, "action":"unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 0)
        print(response.json())
        # self.assertEqual(len(response.json()), 3)

    def test_action_retweet(self):
        client = self.get_client()
        current_count = self.currentCount
        response = client.post("/api/tweets/action/", {"id":2, "action":"retweet"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_tweet_id = data.get('id')
        self.assertNotEqual(2, new_tweet_id)
        self.assertEqual(current_count + 1, new_tweet_id)