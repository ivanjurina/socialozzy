"""Configuration management for SocialOzzy application."""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration from environment variables."""

    # Instagram credentials
    INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

    # Paths
    IMAGE_FOLDER = os.getenv("IMAGE_FOLDER", "./images")
    COMMENTS_FILE = os.getenv("COMMENTS_FILE", "./comments.txt")
    INDEX_FILE = "last_uploaded_index.txt"

    # Content
    UPLOAD_CAPTION = os.getenv("UPLOAD_CAPTION", "")
    DEFAULT_COMMENT = os.getenv("DEFAULT_COMMENT", "Nice post!")

    # Browser settings
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    # Behavior settings
    TEST_MODE = os.getenv("TEST_MODE", "true").lower() == "true"

    # Rate limits (per day)
    MAX_LIKES_PER_DAY = 250
    MAX_FOLLOWS_PER_DAY = 100

    # Timing intervals (in seconds)
    LIKE_INTERVAL_MIN = 60  # 1 minute
    LIKE_INTERVAL_MAX = 120  # 2 minutes
    FOLLOW_INTERVAL_MIN = 120  # 2 minutes
    FOLLOW_INTERVAL_MAX = 240  # 4 minutes
    UPLOAD_INTERVAL = 5400  # 1.5 hours

    # Wait times
    DEFAULT_WAIT_TIMEOUT = 30
    EXTENDED_WAIT_TIMEOUT = 40

    @classmethod
    def load_comments(cls):
        """Load comments from file.

        Returns:
            list: List of comments, or [DEFAULT_COMMENT] if file doesn't exist
        """
        if not os.path.exists(cls.COMMENTS_FILE):
            return [cls.DEFAULT_COMMENT]

        comments = []
        try:
            with open(cls.COMMENTS_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Skip empty lines and comments
                    if line and not line.startswith('#'):
                        comments.append(line)
        except Exception as e:
            print(f"[WARNING] Failed to load comments from {cls.COMMENTS_FILE}: {e}")
            return [cls.DEFAULT_COMMENT]

        return comments if comments else [cls.DEFAULT_COMMENT]

    @classmethod
    def validate(cls):
        """Validate required configuration."""
        if not cls.INSTAGRAM_USERNAME:
            raise ValueError("INSTAGRAM_USERNAME not set in environment variables")
        if not cls.INSTAGRAM_PASSWORD:
            raise ValueError("INSTAGRAM_PASSWORD not set in environment variables")
        if not os.path.exists(cls.IMAGE_FOLDER):
            raise ValueError(f"IMAGE_FOLDER does not exist: {cls.IMAGE_FOLDER}")
