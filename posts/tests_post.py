import pytest
from django.contrib.auth import get_user_model
from .models import Post

@pytest.mark.django_db
def test_post_model():
    user = get_user_model().objects.create_user(
        username="testuser",
        email="test@email.com",
        password="secret"
    )
    post = Post.objects.create(
        author=user,
        title="A good title",
        body="Nice body content"
    )

    assert post.author.username == "testuser"
    assert post.title == "A good title"
    assert post.body == "Nice body content"
    assert str(post) == "A good title"