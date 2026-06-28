import tkinter as tk
from tkinter import ttk 
import json
import os
from datetime import datetime

class LibraryApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Self-Improvement Katalog")
        self.window.geometry("800x600")
#---------------------------------Variable 
        self.data = {}
        self.current_category = "Bücher"
        self.current_item = None
#---------------------------------UI
        self.load_data() #Funktionsaufruf
        self.create_ui() #Funktionsaufruf

    def load_data(self): #1. Funktion
    #hier lädt man die JSON Datei
        self.file_path = "library_data.json"
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding ='utf-8') as file:
                self.data = json.load(file)

        else: 
            self.data = {
                "Bücher" : [],
                "Tagesreflexion": [],
                "Kleine Erfolge": []
            }
            self.save_data()
    
    def save_data(self):#2.Funktion: Speichert (schreibt)die Variable in JSON_Datei
        self.file_path = "library_data.json"
        with open(self.file_path,'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=2)

    def create_ui(self): #2.Funktion
    #hier wird die das Fenster gezeichnet
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_books = ttk.Frame(self.notebook)
        self.tab_reflection = ttk.Frame(self.notebook)
        self.tab_wins = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_books, text="Bücher")
        self.notebook.add(self.tab_reflection, text="Tagesreflexion")
        self.notebook.add(self.tab_wins, text="Kleine Erfolge")

        title_label = tk.Label( #----------------Bücher
            self.tab_books,
            text= "Meine Bücher",
            font= ("Arial", 16, "bold")
        )
        title_label.pack(pady=10)

        self.books_listbox = tk.Listbox(self.tab_books)
        self.books_listbox.pack(fill="both", expand=True, padx=10, pady= 10)

        add_button = tk.Button(#-----------------Button für Bücher
            self.tab_books,
            text= "Neues Buch gelesen? Hier eintragen",
            command=self.add_book_item
        )
        add_button.pack(pady=5)

        title_label = tk.Label(# ---------------------Kleine Erfolge
            self.tab_wins,
            text= "Kleine Erfolge",
            font= ("Arial",16,"bold")
        )
        title_label.pack(pady=10)

        self.wins_listbox = tk.Listbox(self.tab_wins)
        self.wins_listbox.pack(fill= "both", expand=True, padx=10, pady= 10)

        add_button = tk.Button(#------------------------Button für Kleine Erfolge
            self.tab_wins,
            text= "Kleine Erfolge gehabt? Hier eintragen",
            command= self.add_win_item
        )
        add_button.pack(pady=5)

        title_label = tk.Label(#----------------------Tagesreflexion
            self.tab_reflection,
            text= "Reflexion des Tages",
            font= ("Arial",16,"bold")
        )
        title_label.pack(pady=10)

        self.reflection_listbox = tk.Listbox(self.tab_reflection)
        self.reflection_listbox.pack(fill= "both", expand=True, padx= 10, pady=10)

        add_button = tk.Button(#-------------------------Button für Tagesreflexion
            self.tab_reflection,
            text= "Tagesreflexion für heute hier eintragen",
            command= self.add_reflection_item
        )
        add_button.pack(pady=5)

    def add_book_item(self):
        add_window = tk.Toplevel(self.window)
        add_window.title("Neues Buch hinzufügen")
        add_window.geometry("400x300")

        tk.Label(add_window, text="Buchtitel:").pack(pady=5)
        titel_entry = tk.Entry(add_window, width=40)
        titel_entry.pack(pady=5)

        tk.Label(add_window, text="Autor:").pack(pady=5)
        autor_entry = tk.Entry(add_window, width=40)
        autor_entry.pack(pady=5)

        tk.Label(add_window, text="Datum:").pack(pady=5)
        datum_entry = tk.Entry(add_window, width=40)
        datum_entry.pack(pady=5)

        tk.Label(add_window, text="Zusammenfassung:").pack(pady=5)
        zusammenfassung_entry = tk.Entry(add_window, width=40)
        zusammenfassung_entry.pack(pady=5)

        tk.Label(add_window, text="Erkenntnis:").pack(pady=5)
        erkenntnis_entry = tk.Entry(add_window, width=40)
        erkenntnis_entry.pack(pady=5)

        def save_book():
            book_data = {
                "titel": titel_entry.get(),
                "autor": autor_entry.get(),
                "datum": datum_entry.get(),
                "zusammenfassung": zusammenfassung_entry.get(),
                "erkenntnis": erkenntnis_entry.get()
            }
            self.data["Bücher"].append(book_data)
            self.save_data()
            add_window.destroy()
    
        save_button = tk.Button(add_window, text="Speichern",command=save_book)
        save_button.pack(pady=10)

    
    def add_wins_item(self):
        add_window = tk.Toplevel(self.window)
        add_window.title("Kleine Erfolge hinzufügen")
        add_window.geometry("400x300")

        tk.Label(add_window, text="Beschreibung").pack(pady=5)
        beschreibung_entry = tk.Entry(add_window, width=40)
        beschreibung_entry.pack(pady=5)

        tk.Label(add_window, text="Datum:").pack(pady=5)
        datum_entry = tk.Entry(add_window, width=40)
        datum_entry.pack(pady=5)

        tk.Label(add_window, text="Konkretes Ergebnis:").pack(pady=5)
        ergebnis_entry = tk.Entry(add_window, width=40)
        ergebnis_entry.pack(pady=5)

        def save_wins():
            wins_data = {
                "beschreibung": beschreibung_entry.get(),
                "datum": datum_entry.get(),
                "ergebnis": ergebnis_entry.get()
            }
            self.data["Kleine Erfolge"].append(wins_data)
            self.save_data()
            add_window.destroy()
    
        save_button = tk.Button(add_window, text="Speichern",command=save_wins)
        save_button.pack(pady=10)

    def add_reflection_item(self):
        add_window = tk.Toplevel(self.window)
        add_window.title("Tagesreflexion hinzufügen")
        add_window.geometry("400x300")

        tk.Label(add_window, text="Reflexionstitel:").pack(pady=5)
        reflexionstitel_entry = tk.Entry(add_window, width=40)
        reflexionstitel_entry.pack(pady=5)

        tk.Label(add_window, text="Datum:").pack(pady=5)
        datum_entry = tk.Entry(add_window, width=40)
        datum_entry.pack(pady=5)

        tk.Label(add_window, text="Ausgangslage:").pack(pady=5)
        ausgangslage_entry = tk.Entry(add_window, width=40)
        ausgangslage_entry.pack(pady=5)

        tk.Label(add_window, text="Inhalt:").pack(pady=5)
        inhalt_entry = tk.Entry(add_window, width=40)
        inhalt_entry.pack(pady=5)

        tk.Label(add_window, text="erkenntnis").pack(pady=5)
        erkenntnis_entry = tk.Entry(add_window, width=40)
        erkenntnis_entry.pack(pady=5)


        def save_reflection():
            reflexion_data = {
                "reflexionstitel": reflexionstitel_entry.get(),
                "ausgangslage": ausgangslage_entry.get(),
                "datum": datum_entry.get(),
                "inhalt":inhalt_entry.get(),
                "erkenntnis":erkenntnis_entry.get()
            }
            self.data["Tagesreflexion"].append(reflexion_data)
            self.save_data()
            add_window.destroy()
    
        save_button = tk.Button(add_window, text="Speichern",command=save_reflection)
        save_button.pack(pady=10)

    def load_books_in_listbox(self):
        self.books_listbox.delete(0, tk.END)
        for book in self.data["Bücher"]:
            self.books_listbox.insert(tk.END, book["titel"])

    def load_reflections_in_listbox(self):
        self.reflection_listbox.delete(0, tk.END)
        for reflection in self.data["Tagesreflexion"]:
            self.reflection_listbox.insert(tk.END, reflection["reflexionstitel"])

    def load_wins_in_listbox(self):
        self.wins_listbox.delete(0, tk.END)
        for wins in self.data["Kleine Erfolge"]:
            self.reflection_listbox.insert(tk.END, wins["datum"])
