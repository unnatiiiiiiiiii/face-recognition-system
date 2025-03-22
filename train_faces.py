import os
import face_recognition
import pickle

TRAIN_DIR = "train_images"

known_encodings = []
known_names = []

if not os.path.exists(TRAIN_DIR):
    print(f"Error: Training directory '{TRAIN_DIR}' not found!")
    exit()

# Go through each image in the training directory
for person_name in os.listdir(TRAIN_DIR):
    person_folder = os.path.join(TRAIN_DIR, person_name)

    # Check if it's a folder
    if not os.path.isdir(person_folder):
        continue

    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)
        print(f"Processing {image_path}...")  # ✅ Debugging Line

        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(person_name)
            print(f"✅ Successfully encoded {person_name}")
        else:
            print(f"❌ Warning: No face found in {image_path}")

# Save the encodings
data = {"encodings": known_encodings, "names": known_names}
with open("face_encodings.pkl", "wb") as file:
    pickle.dump(data, file)

print("✅ Training complete! Encodings saved to face_encodings.pkl")
