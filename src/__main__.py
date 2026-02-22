"""Main application entry point."""
import os
import time
import random

from src.config import Config
from src.driver import create_driver
from src.auth import login
from src.actions import like_post, follow_account, upload_picture


def main():
    """Run the OzzyCat Instagram automation."""
    # Validate configuration
    try:
        Config.validate()
    except ValueError as e:
        print(f"[ERROR] Configuration error: {e}")
        print("[ERROR] Please check your .env file and ensure all required variables are set.")
        return

    # Create driver
    driver = create_driver()

    processed_posts = set()

    try:
        # Login
        login(driver, Config.INSTAGRAM_USERNAME, Config.INSTAGRAM_PASSWORD)

        # Get list of images to upload
        image_files = [
            f for f in os.listdir(Config.IMAGE_FOLDER)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        ]
        image_index = 0

        # Load last upload index if exists
        if os.path.exists(Config.INDEX_FILE):
            try:
                with open(Config.INDEX_FILE, 'r') as f:
                    image_index = int(f.read().strip())
                print(f"[UPLOAD] Resuming from index {image_index} (of {len(image_files)} images)")
            except:
                print("[UPLOAD] Invalid index file – starting from 0")
                image_index = 0

        # Initialize timestamps
        last_like = time.time() - 300
        last_follow = time.time() - 600
        last_upload = time.time()

        # Counters
        like_count = 0
        follow_count = 0
        start_day = time.time()

        print(f"[MAIN] Started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"[MAIN] {len(image_files)} images ready | Upload interval: 1.5h\n")

        # Main loop
        while True:
            now = time.time()

            # Daily reset
            if now - start_day > 86400:
                print("[MAIN] Daily reset")
                like_count = follow_count = 0
                start_day = now

            # Like posts
            like_int = random.randint(Config.LIKE_INTERVAL_MIN, Config.LIKE_INTERVAL_MAX)
            should_like = (
                (now - last_like >= like_int or (Config.TEST_MODE and like_count == 0))
                and like_count < Config.MAX_LIKES_PER_DAY
            )
            if should_like:
                success, processed_posts = like_post(driver, processed_posts)
                if success:
                    like_count += 1
                last_like = now
                print(f"[MAIN] Next like ~{like_int//60} min\n")

            # Follow accounts
            follow_int = random.randint(Config.FOLLOW_INTERVAL_MIN, Config.FOLLOW_INTERVAL_MAX)
            should_follow = (
                (now - last_follow >= follow_int or (Config.TEST_MODE and follow_count == 0))
                and follow_count < Config.MAX_FOLLOWS_PER_DAY
            )
            if should_follow:
                if follow_account(driver):
                    follow_count += 1
                last_follow = now
                print(f"[MAIN] Next follow ~{follow_int//60} min\n")

            # Upload pictures
            if now - last_upload >= Config.UPLOAD_INTERVAL and image_index < len(image_files):
                path = os.path.join(Config.IMAGE_FOLDER, image_files[image_index])
                print(f"[UPLOAD] Attempting file: {image_files[image_index]} (index {image_index})")
                if upload_picture(driver, path):
                    image_index += 1
                    with open(Config.INDEX_FILE, 'w') as f:
                        f.write(str(image_index))
                    print(f"[UPLOAD] Success – saved new index {image_index}")
                last_upload = now
                print("[MAIN] Next upload 1.5h\n")

            # Status update
            time.sleep(15)
            print(f"[STATUS {time.strftime('%H:%M:%S')}] Likes: {like_count} | Follows: {follow_count} | "
                  f"Uploaded: {image_index}/{len(image_files)} | Tracked posts: {len(processed_posts)}")

    except KeyboardInterrupt:
        print("[MAIN] Stopped by user")
    except Exception as e:
        print(f"[MAIN] Crash: {type(e).__name__}: {str(e)}")
        try:
            driver.save_screenshot("crash.png")
        except:
            pass
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
