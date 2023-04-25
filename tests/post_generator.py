from django.contrib.auth.models import User
from user.models import Blog, UserSettings

from faker import Faker


fake = Faker()

# User.objects.filter(first_name='Test', last_name='Test').delete()
def generate_users_and_posts():
    name = 'test'

    for i in range(100):
        username = name + str(i)

        user = User.objects.create_user(
            username=username,
            password='test12345',
            first_name='Test',
            last_name='Test'
        )

        UserSettings.objects.create(user_id=username)

        body = [
            Blog(content=fake.text(), user=user) for _ in range(20)
        ]
        Blog.objects.bulk_create(body)
    
    print("Done")
