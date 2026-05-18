import os

folder = r"C:\Users\mpsor\OneDrive\Desktop\python_test\Task 2"  
prefix = "Hawaii_Trip"

files = sorted([f for f in os.listdir(folder) if not f.startswith('.')])

for i, filename in enumerate(files, start=1):
    extension = os.path.splitext(filename)[1]       
    new_name = f"{prefix}_{i:02d}{extension}"          
    os.rename(
        os.path.join(folder, filename),
        os.path.join(folder, new_name)
    )
    print(f"Renamed: {filename} → {new_name}")

print("Done!")