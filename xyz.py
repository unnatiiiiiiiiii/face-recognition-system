import pickle

with open("face_encodings.pkl", "rb") as file:
    data = pickle.load(file)

print(data)  # This will show the actual content
