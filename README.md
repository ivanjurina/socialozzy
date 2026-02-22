# SocialOzzy - Instagram Automation

Python application for automating Instagram interactions.

## Features

- **Automated Login**: Securely log in to Instagram
- **Like & Comment**: Automatically like and comment on posts from your feed
- **Follow Accounts**: Follow suggested accounts from the explore page
- **Upload Pictures**: Schedule and upload pictures with custom captions
- **Customizable Comments**: Load comments from external file for easy customization

## Project Structure

```
socialozzy/                  # Root directory (rename ozzy__thecat to this)
├── src/                     # All Python source code
│   ├── __init__.py
│   ├── __main__.py          # Main application entry point
│   ├── config.py            # Configuration management
│   ├── constants.py         # App constants
│   ├── utils.py             # Utility functions
│   ├── auth/
│   │   ├── __init__.py
│   │   └── login.py         # Login functionality
│   ├── actions/
│   │   ├── __init__.py
│   │   ├── like.py          # Like & comment actions
│   │   ├── follow.py        # Follow actions
│   │   └── upload.py        # Upload actions
│   └── driver/
│       ├── __init__.py
│       └── setup.py         # WebDriver configuration
├── images/                  # Place your pictures here
├── comments.txt             # Your custom comments (one per line)
├── .env                     # Environment variables (DO NOT COMMIT)
├── .env.example             # Example environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup


### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or with pip3:

```bash
pip3 install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env` with your information:

```env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
IMAGE_FOLDER=/path/to/your/images
COMMENTS_FILE=./comments.txt
UPLOAD_CAPTION=My awesome post! #hashtag
DEFAULT_COMMENT=Nice post!
HEADLESS=false
TEST_MODE=true
```

### 3. Add Your Images

Place your pictures in the `images/` folder (or the folder specified in `IMAGE_FOLDER`).

### 4. Customize Your Comments

Edit `comments.txt` to add your own comments. Each line will be a separate comment that can be randomly selected:

```txt
# Add your comments here, one per line
# Lines starting with # are ignored

Great post!
Love this! ❤️
Awesome content!
Looking good!
```

## Usage

From the project root directory, run the application:

```bash
python3 -m src
```

Or run it directly:

```bash
python3 src/__main__.py
```

## Configuration

All configuration is managed through environment variables in the `.env` file:

### Required Settings

- `INSTAGRAM_USERNAME`: Your Instagram username
- `INSTAGRAM_PASSWORD`: Your Instagram password
- `IMAGE_FOLDER`: Path to folder containing images to upload

### Optional Settings

- `COMMENTS_FILE`: Path to file with comments (default: `./comments.txt`)
- `UPLOAD_CAPTION`: Default caption for uploads (default: empty)
- `DEFAULT_COMMENT`: Fallback comment if no comments file found (default: "Nice post!")
- `HEADLESS`: Set to `true` to run browser in headless mode (default: `false`)
- `TEST_MODE`: Set to `true` to run actions immediately for testing (default: `true`)

### Rate Limits

The application has built-in rate limits to avoid Instagram's spam detection:

- **Likes**: Max 250 per day, with 1-2 minute intervals
- **Follows**: Max 100 per day, with 2-4 minute intervals
- **Uploads**: 1.5 hour intervals

These can be adjusted in `socialozzy/config.py`.

## Safety Notes

- The application saves screenshots on errors for debugging
- Upload progress is saved in `last_uploaded_index.txt`
- Processed posts are tracked to avoid duplicate interactions
- Random delays are added to mimic human behavior
- Never commit your `.env` file or expose your credentials


### Modifying Comments

Edit the `comments.txt` file. Comments are loaded at runtime, so you can modify them without restarting the application (changes will apply on next comment action).

### Adjusting Timings

Modify the configuration values in `src/config.py`:

- `MAX_LIKES_PER_DAY`
- `MAX_FOLLOWS_PER_DAY`
- `LIKE_INTERVAL_MIN` / `LIKE_INTERVAL_MAX`
- `FOLLOW_INTERVAL_MIN` / `FOLLOW_INTERVAL_MAX`
- `UPLOAD_INTERVAL`

## Troubleshooting

- **Login fails**: Check your credentials in `.env`
- **Upload fails**: Check that `IMAGE_FOLDER` path is correct and contains images
- **No comments**: Check that `COMMENTS_FILE` exists and contains valid comments
- **Screenshots**: Check generated `.png` files for debugging
- **Errors**: Review console output for detailed error messages
- **Python not found**: Use `python3` instead of `python`

## License

This project is for educational purposes only. Use at your own risk and respect Instagram's Terms of Service.

## Credits

Named in honor of Ozzy the cat 🐱
