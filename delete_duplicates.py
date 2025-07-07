import os

root_dir = "myApp/static/images"
deleted = 0

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            base_name = os.path.splitext(file)[0]
            webp_file = base_name + ".webp"
            webp_path = os.path.join(subdir, webp_file)

            if os.path.exists(webp_path):
                original_path = os.path.join(subdir, file)
                os.remove(original_path)
                deleted += 1
                print(f"🗑️ Deleted: {original_path}")

print(f"\n✅ Done! Deleted {deleted} original image(s) that have a matching .webp.")
