import os
from setuptools import setup, find_packages

# Function to create folder structure
def setup_folders():
    folders = [
        "CodeWithLove",  # Root project folder
        "CodeWithLove/my_package",  # Package folder
    ]
    files = [
        "CodeWithLove/my_package/__init__.py",  # Init file
        "CodeWithLove/my_package/main.py",  # Main file
        "CodeWithLove/README.md",  # README file
        "CodeWithLove/LICENSE",  # License file
    ]
    
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create files
    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                if "README.md" in file:
                    f.write("# Code With Love\n\nCode with love using Python.")
                elif "LICENSE" in file:
                    f.write("MIT License")  # Replace with your license text
                elif "__init__.py" in file:
                    f.write("")  # Leave __init__.py empty
                elif "main.py" in file:
                    f.write("""\
def main():
    print("Welcome to Code With Love!")
    
if __name__ == "__main__":
    main()
""")
                else:
                    f.write("# Placeholder content")

# Set up folders before running setup
setup_folders()

# Standard setup configuration
setup(
    name="CodeWithLove",
    version="0.1.0",
    author="Null Void",
    author_email="jundelmalazarte348@gmail.com",
    description="Code with love using Python",
    long_description=open("CodeWithLove/README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jundel-Malazarte/Code-With-Love-Using-Python",
    packages=find_packages(where="CodeWithLove"),
    package_dir={"": "CodeWithLove"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'code-with-love=CodeWithLove.my_package.main:main',  # Adds a command-line tool
        ],
    },
)
