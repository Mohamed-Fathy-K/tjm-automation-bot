import os
import time
import subprocess
import pyautogui

def launch_notepad():
    """
    Attempts to launch Notepad.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        subprocess.Popen("notepad.exe")
        time.sleep(1)  # Give time for the app to open
    except FileNotFoundError:
        print("Error: Notepad executable not found.")
    except Exception as e:
        print(f"An unexpected error occurred while launching Notepad: {e}")

def write_post(post, speed=0.05):
    """
    Writes a single post in Notepad.

    Args:
        post (dict): A dictionary with keys 'title' and 'body'.
        speed (float, optional): Delay between each character. Default is 0.05 seconds.
    
    Returns:
        bool: True if writing succeeded, False otherwise.
    """
    try:
        pyautogui.typewrite("Title: " + post['title'] + "\n\n", interval=speed)
        pyautogui.typewrite(post['body'] + "\n\n", interval=speed)
        time.sleep(0.5)  # optional short pause after writing
        return True
    except Exception as e:
        print(f"[Error] Failed to write post: {e}")
        return False
    
def make_directory(folder_name, base_path=None):
    """
    Creates a directory with the given folder name.
    
    Args:
        folder_name (str): Name of the folder to create.
        base_path (str, optional): Base path where the folder will be created.
            Defaults to Desktop of the current user.
    
    Returns:
        str: Full path of the created directory, or None if failed.
    """
    try:
        # Default base path is Desktop
        if base_path is None:
            base_path = os.path.join(os.path.expanduser("~"), "Desktop")
        
        # Full path of the new folder
        full_path = os.path.join(base_path, folder_name)
        
        # Create the directory
        os.makedirs(full_path, exist_ok=True)

        return full_path
    
    except PermissionError:
        print(f"[Error] Permission denied: Cannot create directory at {full_path}")
    except OSError as e:
        print(f"[Error] OS error: {e}")
    except Exception as e:
        print(f"[Error] Unexpected error: {e}")
    
    return None

def save_file(file_name, folder_path=None):
    """
    Saves the currently active Notepad window using Ctrl+S, names the file, and saves it.
    
    Args:
        file_name (str): Name of the file to save (e.g., "example.txt").
        folder_path (str, optional): Folder to save the file in. Defaults to Desktop/tjm-project.
    """
    try:
        # Set default folder_path if not provided
        if folder_path is None:
            folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "tjm-project")
        
        # Ensure the folder exists
        os.makedirs(folder_path, exist_ok=True)
        
        # Full file path with Windows-style backslashes
        full_path = os.path.join(folder_path, file_name)
        full_path = full_path.replace("/", "\\") # '/' is not working in saving window
        
        # Press Ctrl+S to open save dialog
        pyautogui.hotkey('ctrl', 's')
        time.sleep(0.5)
        
        # Type the full path including the file name
        pyautogui.typewrite(full_path, 0.05)
        time.sleep(0.2)
        
        # Press Enter to save
        pyautogui.press('enter')
        time.sleep(0.5)
        
        # Press Alt+F4 to close Notepad
        pyautogui.hotkey('alt', 'f4')
    
    except PermissionError:
        print(f"[Error] Permission denied: Cannot save file at {full_path}")
    except FileNotFoundError:
        print(f"[Error] File path not found: {full_path}")
    except pyautogui.FailSafeException:
        print("[Error] PyAutoGUI fail-safe triggered. Move mouse to a corner to stop script.")
    except Exception as e:
        print(f"[Error] Unexpected error: {e}")
