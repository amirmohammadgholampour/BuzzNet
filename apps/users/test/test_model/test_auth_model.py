import pytest 
from apps.users.models import User 

@pytest.fixture
def user_a(db):
    return User.objects.create_user(
        email="user_a@test.com",
        password="password123",
        username="user_a",
        full_name="User A"
    )

@pytest.fixture
def user_b(db):
    return User.objects.create_user(
        email="user_b@test.com",
        password="password456",
        username="user_b",
        full_name="User B"
    )
    
@pytest.mark.django_db
def test_user_creation(user_a):
    """
    =============
    User A is created;
    =============
    """
    assert user_a.username == "user_a"
    assert user_a.email == "user_a@test.com"
    assert user_a.check_password("password123")


@pytest.mark.django_db
def test_user_following(user_a, user_b):
    """
    =============
    User A is not following to User B;
    =============
    """
    assert not user_a.is_following(user_b)

    """
    =============
    User A is started following to User B;
    =============
    """
    user_a.follow(user_b)
    assert user_a.is_following(user_b)
    assert user_b.following.filter(id=user_a.id).exists() == False

    """
    =============
    User A is stop following User B;
    =============
    """
    user_a.unfollow(user_b)
    assert not user_a.is_following(user_b)
