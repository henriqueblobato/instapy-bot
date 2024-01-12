import sys

from dotenv import load_dotenv

from instapy import InstaPy, smart_run
import os

SESSION_FILE = "session.pkl"


def run_bot(u, p):
    # session = load_session()
    # if session is None:

    # session = InstaPy(username=u, password=p, nogui=True, want_check_browser=False)
    session = InstaPy(
        username=u,
        password=p,
        # nogui=True,
        headless_browser=True,
        multi_logs=True,
        want_check_browser=False,
    )
    # session.login()
    with smart_run(session):
        session.set_do_like(enabled=True, percentage=70)
        # session.set_do_comment(enabled=True, percentage=25)
        # session.set_comments(["Awesome", "Really Cool", "I like your stuff"])

        # session.set_quota_supervisor(
        #     enabled=True,
        #     sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
        #     sleepyhead=True,
        #     stochastic_flow=True,
        #     notify_me=True,
        #     peak_likes_hourly=50,
        #     peak_likes_daily=500,
        #     peak_comments_hourly=20,
        #     peak_comments_daily=150,
        #     peak_follows_hourly=40,
        #     peak_follows_daily=None,
        #     peak_unfollows_hourly=30,
        #     peak_unfollows_daily=300,
        #     peak_server_calls_hourly=None,
        #     peak_server_calls_daily=4000,
        # )
        #
        # session.set_delimit_liking(enabled=True, max_likes=1000, min_likes=10)
        #
        # session.set_delimit_commenting(enabled=True, max_comments=50, min_comments=3)
        #
        # session.set_relationship_bounds(
        #     enabled=True,
        #     potency_ratio=1.5,
        #     delimit_by_numbers=True,
        #     max_followers=8000,
        #     max_following=4000,
        #     min_followers=100,
        #     min_following=50,
        #     min_posts=5,
        #     max_posts=500,
        # )
        #
        # session.set_action_delays(
        #     enabled=True,
        #     like=3,
        #     comment=5,
        #     follow=4,
        #     unfollow=20,
        #     story=8,
        #     randomize=True,
        #     random_range_from=70,
        #     random_range_to=140,
        # )
        #
        # session.set_skip_users(
        #     skip_private=True,
        #     private_percentage=100,
        #     skip_no_profile_pic=True,
        #     no_profile_pic_percentage=100,
        #     skip_business=True,
        #     skip_non_business=False,
        #     business_percentage=0,
        #     skip_bio_keyword=[],
        #     mandatory_bio_keywords=[],
        #     skip_public=False,
        #     public_percentage=0,
        # )
        #
        # session.set_ignore_users(["random_user", "another_username"])
        #
        # hashtags = session.target_list("hashtags.txt")
        # session.like_by_tags(hashtags, amount=10)
        #
        # users = session.target_list("users.txt")
        # session.follow_user_followers(users, amount=10, randomize=False)
        #
        # session.join_pods(topic='entertainment', engagement_mode='no_comments')


def get_credentials():
    return {
        "username": sys.argv[1],
        "password": sys.argv[2]
    }


if __name__ == "__main__":
    load_dotenv()
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD_B64')

    if not any([username, password]):
        raise SystemExit("No username or password provided!")

    creds = get_credentials()

    print(f"User: {creds['username']}")
    run_bot(*creds)
