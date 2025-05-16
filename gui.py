import tkinter as tk
from tkinter import ttk
import subprocess
import threading

def run_fact_check():
    url = url_entry.get().strip()
    if not url:
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, "Please enter a valid URL.")
        return

    # Start progress bar
    progress_label.config(text="Processing... please wait.")
    progress_bar.start()
    window.update()

    try:
        scrape_proc = subprocess.Popen(['python3', 'webScrape.py', url], stdout=subprocess.PIPE)
        api_proc = subprocess.Popen(['python3', 'testAPI.py'], stdin=scrape_proc.stdout, stdout=subprocess.PIPE)
        output, _ = api_proc.communicate()

        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, output.decode('utf-8'))

    except Exception as e:
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, f"Error: {str(e)}")

    # Stop progress bar
    progress_bar.stop()
    progress_label.config(text="Done.")

def start_fact_check_thread():
    threading.Thread(target=run_fact_check).start()

# Set up window
window = tk.Tk()
window.title("News Fact Checker")
window.geometry("600x450")

# URL Entry
url_label = tk.Label(window, text="Enter Article URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(window, width=80)
url_entry.pack(pady=5)

# Check Button
check_button = tk.Button(window, text="Check Article", command=start_fact_check_thread)
check_button.pack(pady=10)

# Progress Bar
progress_bar = ttk.Progressbar(window, mode='indeterminate')
progress_bar.pack(pady=5, fill='x', padx=10)

# Progress Label
progress_label = tk.Label(window, text="")
progress_label.pack()

# Output Box
result_box = tk.Text(window, wrap="word", height=15)
result_box.pack(padx=10, pady=10, fill="both", expand=True)

# Start GUI
window.mainloop()
