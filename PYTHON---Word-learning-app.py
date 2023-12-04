import tkinter as tk

# Function to load content (just a placeholder)
def load_content():
    # In a real app, this function would fetch data/content
    # For demonstration, let's assume content is loaded into a list
    content_list = [
        "Geography: Learn about different continents",
        "Culture: Explore traditions from around the world",
        "Language: Basics of various languages",
        "History: Notable historical events"
    ]
    return content_list

def show_content(content):
    # Function to display content on the GUI
    label.config(text=content)

def next_content():
    # Function to move to the next content
    global content_index
    content_index = (content_index + 1) % len(contents)
    show_content(contents[content_index])

# Create the main window
root = tk.Tk()
root.title("World Learning App")

# Initial content loading
contents = load_content()
content_index = 0
show_content(contents[content_index])

# Create UI elements
label = tk.Label(root, text="", wraplength=300)
label.pack(pady=20)

next_button = tk.Button(root, text="Next", command=next_content)
next_button.pack()

# Start the app
root.mainloop()
