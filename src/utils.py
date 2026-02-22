"""Utility functions for the OzzyCat application."""
import re


def remove_emojis(text):
    """Remove emojis from text.

    Args:
        text: String potentially containing emojis

    Returns:
        String with emojis removed and stripped
    """
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # Transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # Flags
        u"\U00002702-\U000027B0"  # Dingbats
        u"\U000024C2-\U0001F251"  # Enclosed characters
        u"\U0001f926-\U0001f937"  # Supplemental symbols
        u"\U00010000-\U0010ffff"  # Other
        u"\u200d"  # Zero-width joiner
        u"\u2640-\u2642"  # Gender symbols
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text).strip()
