#!/bin/python3
import subprocess
import os

def remove_gtk_assets():
    try:
        # Get the user's home directory
        user_home = os.path.expanduser("~")
        
        # Define the paths to the assets directory and gtk.css file
        assets_path = os.path.join(user_home, '.config/gtk-4.0/assets/')
        gtk_css_path = os.path.join(user_home, '.config/gtk-4.0/gtk.css')
        
        # Remove the assets directory
        subprocess.run(['rm', '-rf', assets_path], check=True)
        print(f"Removed {assets_path} successfully.")
        
        # Remove the gtk.css file
        subprocess.run(['rm', '-rf', gtk_css_path], check=True)
        print(f"Removed {gtk_css_path} successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    remove_gtk_assets()