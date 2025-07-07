from PIL import Image
import os

input_dir = "myApp/static/images"
output_dir = "myApp/static/images/webp"

for subdir, dirs, files in os.walk(input_dir):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(subdir, file)
            output_file = os.path.splitext(file)[0] + ".webp"
            output_path = os.path.join(subdir, output_file)

            try:
                img = Image.open(input_path)

                # ✅ Preserve transparency if PNG
                if img.mode in ("RGBA", "LA"):
                    img.save(output_path, "webp", quality=80, lossless=True, transparency=0)
                else:
                    img = img.convert("RGB")
                    img.save(output_path, "webp", quality=80)

                print(f"✅ Converted: {input_path} → {output_path}")
            except Exception as e:
                print(f"⚠️ Error converting {file}: {e}")
