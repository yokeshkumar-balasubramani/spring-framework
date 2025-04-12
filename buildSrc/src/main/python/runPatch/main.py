import os
import subprocess

def run_all_patches(patches_dir):
    for root, _, files in os.walk(patches_dir):
        for file in files:
            if file.endswith(".py"):
                patch_path = os.path.join(root, file)
                print(f"🚀 Running patch: {patch_path}")
                subprocess.run(["python3", patch_path], check=True)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    patches_dir = os.path.join(base_dir, "../patches")
    run_all_patches(patches_dir)
