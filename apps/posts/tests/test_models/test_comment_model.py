import pytest 
from apps.posts.models import Comment, Post 
from apps.users.models import User 

@pytest.fixture 
def user(db):
    return User.objects.create_user(
        email="test@yahoo.com", 
        password="123456"
    )

@pytest.fixture 
def post(db, user):
    return Post.objects.create(
        author=user,
        text="Test Post Text",
        image="/image/test.jpg",
        video="/video/test.mp4"
    )

@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(
        post=post,
        author=user,
        text="Test comment"
    )
    
@pytest.mark.django_db
def test_create_comment(comment, user, post):
    assert comment.post == post
    assert comment.author == user
    assert comment.text == "Test comment"