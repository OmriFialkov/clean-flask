from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# List of image URLs (replacing database)
image_urls = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcuqUINWHLTIq9D-GWb9gyGG3AWQmO2HiA3w&s",
    "https://www.pawlovetreats.com/cdn/shop/articles/pembroke-welsh-corgi-puppy_1000x.jpg?v=1628638716",
    "https://hips.hearstapps.com/goodhousekeeping/assets/17/30/pembroke-welsh-corgi.jpg",
    "https://img.freepik.com/free-photo/portrait-cute-boxer-dog_181624-47633.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlO4erNhFuKmV1TNly5fu8RbSFftERnpUCUg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0qDKYT9QCq6VnNu4Rlo-rCzD5CDpwt4JCBvIJ5dhI1NpNjyE0tQl740Kf5lUWwe8T6UA&usqp=CAU"
]

@app.route("/")
def index():
    try:
        # Database connection and visitor counter are commented out
        # connection = get_db_connection()
        # cursor = connection.cursor()

        # Increment counter
        # cursor.execute("UPDATE visitor_counter SET count = count + 1 WHERE id = 1")
        # connection.commit()

        # Fetch updated count
        # cursor.execute("SELECT count FROM visitor_counter WHERE id = 1")
        # visitor_count = cursor.fetchone()[0]

        # Fetch image URLs from the database
        # cursor.execute("SELECT image_url FROM images")
        # result = cursor.fetchall()
        # connection.close()

        # Transform the result into a list of URLs
        # images = [row[0] for row in result]

        # Pick a random image from the list
        url = random.choice(image_urls) if image_urls else None
        visitor_count = "unknown"  # Fallback visitor count since DB is not used
    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        visitor_count = "unknown"
        url = None

    # Fallback rendering
    if url:
        return render_template("index.html", url=url, visitor_count=visitor_count)
    else:
        return render_template("index.html", url=None, visitor_count=visitor_count, message="No images available.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
