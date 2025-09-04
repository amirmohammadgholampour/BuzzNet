import pytest
from apps.posts.models import Post
from apps.users.models import User 

@pytest.fixture 
def user(db):
    user = User.objects.create_user(
        email="test@yahoo.com", 
        password="123456"
    )
    return user 

@pytest.fixture 
def post(db, user):
    post = Post.objects.create(
        author=user,
        text="Test Post Text",
        image="/image/test.jpg",
        video="/video/test.mp4"
    )
    return post
    
@pytest.mark.django_db 
def test_create_post(post):
    assert post.author.email == "test@yahoo.com"
    assert post.text == "Test Post Text" 
    assert post.image == "/image/test.jpg" 
    assert post.video == "/video/test.mp4"