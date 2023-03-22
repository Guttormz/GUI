import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3 as sq

conn = sq.connect('personer.db') # Oppretter en database

c = conn.cursor() # Oppretter en cursor

if c.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name='kunde'"): # Sjekker om tabellen post eksisterer
    try: 
        c.execute("DROP TABLE kunde") # Prøver å slette tabellen post
    except:
       sq.OperationalError # Hvis tabellen ikke eksisterer, så vil den ikke bli slettet

c.execute('CREATE TABLE IF NOT EXISTS kunde (kundenummer NUMBER, fornavn TEXT, etternavn TEXT, epost TEXT, telefon NUMBER, postnummer NUMBER)') # Oppretter tabellen post

f = open('randoms.csv', 'r') # Åpner filen randoms.csv i read
for line in f: # Går gjennom hver linje i filen
    c.execute('INSERT INTO kunde VALUES (?,?,?,?,?,?)', (line.split(','))) # Legger til hver linje i tabellen post

c.execute('DELETE FROM kunde WHERE Fornavn = "fname"') # Sletter alle linjer som har "fname" i kolonnen Fornavn

conn.commit() # Lagrer endringene



def søk():

    def search():
        for widget in result_frame.winfo_children(): # Fjerner alle widgets fra result_frame
            widget.destroy() # Fjerner alle widgets fra result_frame

        # Execute the search query and get the results
        query = search_entry.get() # Henter søkeordet fra søkefeltet
        if not query.isdigit(): # Sjekker om søkeordet er et tall
            messagebox.showerror("Error", "Kundenummer kan bare inneholde tall") # Viser en feilmelding
            return # Avslutter funksjonen
        c.execute("SELECT * FROM kunde WHERE kundenummer = ?", (query,)) # Henter alle linjer som har søkeordet i kolonnen kundenummer
        results = c.fetchall() # Lagrer resultatet i en variabel
        c.execute("SELECT * FROM kunde ORDER BY kundenummer DESC LIMIT 1") # Henter kunden med høyest kundenummer
        max = c.fetchall() # Lagrer resultatet i en variabel
        for row in max: # Går gjennom hver linje i variabelen
            next # Går til neste linje

        if int(query) > row[0] or int(query) < 1: # Sjekker om kundenummeret er mellom 1 og det høyeste kundenummeret
            messagebox.showerror("Error", "Kundenummer finnes ikke, kundenummer går fra 1 til " + str(row[0])) # Viser en feilmelding om kundenummeret ikke finnes

        for x, result in enumerate(results): # Går gjennom hver linje i variabelen
            for y, value in enumerate(result): # Går gjennom hver verdi i hver linje
                label = tk.Label(result_frame, text=value) # Lager en label med verdien
                label.grid(row=x, column=y, padx=10, pady=15) # Plasserer labelen i riktig kolonne og rad

    root = tk.Tk() # Oppretter et vindu
    root.geometry("800x550") # Setter størrelsen på vinduet
    search_frame = tk.Frame(root) # Oppretter en ramme
    search_frame.pack(side="top") # Plasserer rammen øverst på skjermen
    root.resizable(False, False) # Gjør det umulig å endre størrelsen på vinduet

    tekst = Canvas(root, width=100, height=100) # Oppretter en canvas
    tekst.create_text(400, 50, text="Søk etter kunde", font=("Arial", 50)) # Legger til teksten "Søk etter kunde" i canvasen

    search_label = tk.Label(search_frame, text="Skriv inn kundenummer:") # Oppretter en label
    search_label.pack(side="left") # Plasserer labelen til venstre for søkefeltet

    search_entry = tk.Entry(search_frame) # Oppretter et søkefelt
    search_entry.pack(side="left", expand=True, fill="x") # Plasserer søkefeltet til høyre for labelen

    search_button = tk.Button(search_frame, text="Search", command=search) # Oppretter en søkeknapp
    search_button.pack(side="left") # Plasserer søkeknappen til høyre for søkefeltet

    result_frame = tk.Frame(root) # Oppretter en ramme
    result_frame.pack(side="top", fill="both", expand=True) # Plasserer rammen under søkefeltet

    tilbake_button = tk.Button(root, text="Tilbake", padx=0, pady=0, font=("Arial", 40), command=lambda: [admin(), root.destroy()]) # Oppretter en tilbakeknapp
    tilbake_button.place(x=590, y=0) # Plasserer tilbakeknappen øverst til høyre på skjermen
    
def admin(): 

    def logout():
        root.destroy() # Lukker vinduet
        hovedside() # Åpner hovedsiden

    root = tk.Tk() # Oppretter et vindu
    root.geometry("800x900") # Setter størrelsen på vinduet
    root.resizable(False, False) # Gjør det umulig å endre størrelsen på vinduet

    login_button = tk.Button(root, text="Logout", padx=0, pady=0, font=("Arial", 50), command=lambda: [logout(), root.destroy()]) # Oppretter en logoutknapp
    login_button.place(x=550, y=0) # Plasserer logoutknappen øverst til høyre på skjermen

    sok_button = tk.Button(root, text="Søk", padx=0, pady=0, font=("Arial", 50), command=lambda: [søk(), root.destroy()]) # Oppretter en søkeknapp
    sok_button.place(x=300, y=0) # Plasserer søkeknappen i midten på toppen av skjermen

    avslutt_button = tk.Button(root, text="Avslutt", padx=0, pady=0, font=("Arial", 50), command=root.destroy) # Oppretter en avsluttknapp
    avslutt_button.place(x=540, y=770) # Plasserer avsluttknappen nederst til høyre på skjermen

def log():
    def login():
        username = username_entry.get() # Henter brukernavnet fra brukernavnfeltet
        password = password_entry.get() # Henter passordet fra passordfeltet

        if username == "admin" and password == "admin": # Sjekker om brukernavnet og passordet er lik admin
            messagebox.showinfo("Login successful", "Welcome " + username + "!") # Viser en velkomstmelding
            root.destroy() # Lukker vinduet
            admin() # Åpner adminmenyen
        else:
            messagebox.showerror("Login failed", "Invalid username or password.") # Viser en feilmelding om brukernavnet eller passordet er feil

    root = tk.Tk() # Oppretter et vindu
    root.geometry("800x900") # Setter størrelsen på vinduet
    root.resizable(False, False) # Gjør det umulig å endre størrelsen på vinduet

    username_label = tk.Label(root, text="Username:", font=("Arial", 40)) # Oppretter en label med teksten "Username:"
    password_label = tk.Label(root, text="Password:", font=("Arial", 40)) # Oppretter en label med teksten "Password:"
    username_entry = tk.Entry(root, font=("Arial", 40)) # Oppretter et brukernavnfelt
    password_entry = tk.Entry(root, show="*", font=("Arial", 40)) # Oppretter et passordfelt
    login_button = tk.Button(root, text="Login", bg="green", fg="white", command=login, font=("Arial", 40)) # Oppretter en loginknapp

    username_label.pack(pady=10) # Plasserer brukernavnlabelen øverst på skjermen
    username_entry.pack(pady=5) # Plasserer brukernavnfeltet under brukernavnlabelen
    password_label.pack(pady=10) # Plasserer passordlabelen under brukernavnfeltet
    password_entry.pack(pady=5) # Plasserer passordfeltet under passordlabelen
    login_button.pack(pady=10) # Plasserer loginknappen under passordfeltet
    return username_entry # Returnerer brukernavnfeltet

def hovedside():
    root = tk.Tk() # Oppretter et vindu
    root.geometry("800x900") # Setter størrelsen på vinduet
    root.resizable(False, False) # Gjør det umulig å endre størrelsen på vinduet

    login_button = tk.Button(root, bg="green", fg="white", text="Login", padx=0, pady=0, font=("Arial", 50), command=lambda: [log(), root.destroy()]) # Oppretter en loginknapp
    login_button.place(x=300, y=0) # Plasserer loginknappen øverst i midten på skjermen

    avslutt_button = tk.Button(root, text="Avslutt", padx=0, pady=0, font=("Arial", 50), command=root.destroy) # Oppretter en avsluttknapp
    avslutt_button.place(x=540, y=770) # Plasserer avsluttknappen nederst til høyre på skjermen

    root.mainloop() # Starter hovedløkken

hovedside()