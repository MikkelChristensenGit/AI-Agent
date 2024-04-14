from llama_index.core.tools import FunctionTool
import os

note_file = os.path.join("data", "notes.txt")  # Constructing the path to the notes.txt file.

def save_note(note):
    """
    Function to save a note to a text file.
    Args:
    - note: The note to be saved.
    Returns:
    - str: Confirmation message indicating the note is saved.
    """
  
    if not os.path.exists(note_file): # Check if the notes.txt file exists.
        open(note_file, "w") # If not, create the file.

    with open(note_file, "a") as f: # Open the file in append mode.
        f.writelines([note + "\n"]) # Write the note to the file followed by a newline character.
    
    return "note saved" # Return a confirmation message indicating the note is saved.

note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user",
)
# Creating a FunctionTool object named "note_saver" with save_note function as its action,
# and providing a description for the tool.
