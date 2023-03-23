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

def lag_kunde():

    def reg():
        fname_entry.get()
        ename_entry.get()
        epost_entry.get()
        telefon_entry.get()
        postnr_entry.get()

        conn = sq.connect('personer.db') # Oppretter en database

        c = conn.cursor() # Oppretter en cursor

        c.execute("SELECT * FROM kunde ORDER BY kundenummer DESC LIMIT 1") # Henter kunden med høyest kundenummer
        max = c.fetchall() # Lagrer resultatet i en variabel
        for row in max: # Går gjennom hver linje i variabelen
                next # Går til neste linje
        tall = int(row[0]) # Lagrer kundenummeret i en variabel
        tall = tall+1

        f = open('randoms.csv', 'a')
        f.write(str(tall) + "," + fname_entry.get() + "," + ename_entry.get() + "," + epost_entry.get() + "," + telefon_entry.get() + "," + postnr_entry.get() + "\n") # Legger til hver linje i tabellen post

        messagebox.showinfo("Registrert", "Kunden er registrert med kundenummer " + str(tall)) # Viser en melding om at kunden er registrert
    
    root = tk.Tk() # Oppretter et vindu
    root.geometry("800x650") # Setter størrelsen på vinduet
    root.resizable(False, False) # Gjør det umulig å endre størrelsen på vinduet

    fname_label = tk.Label(root, text="Fornavn:", font=("Arial", 20)) # Oppretter en label med teksten "Username:"
    fname_entry = tk.Entry(root, font=("Arial", 20)) # Oppretter et brukernavnfelt

    ename_label = tk.Label(root, text="Etternavn:", font=("Arial", 20)) # Oppretter en label med teksten "Password:"
    ename_entry = tk.Entry(root, font=("Arial", 20)) # Oppretter et passordfelt

    epost_label = tk.Label(root, text="Epost:", font=("Arial", 20)) # Oppretter en label med teksten "Password:"
    epost_entry = tk.Entry(root, font=("Arial", 20)) # Oppretter et passordfelt

    telefon_label = tk.Label(root, text="Telefon:", font=("Arial", 20)) # Oppretter en label med teksten "Password:"
    telefon_entry = tk.Entry(root, font=("Arial", 20)) # Oppretter et passordfelt

    postnr_label = tk.Label(root, text="Postnummer:", font=("Arial", 20)) # Oppretter en label med teksten "Password:"
    postnr_entry = tk.Entry(root, font=("Arial", 20)) # Oppretter et passordfelt



    fname_label.pack(pady=10) # Plasserer brukernavnlabelen øverst på skjermen
    fname_entry.pack(pady=5) # Plasserer brukernavnfeltet under brukernavnlabelen

    ename_label.pack(pady=10) # Plasserer passordlabelen under brukernavnfeltet
    ename_entry.pack(pady=5) # Plasserer passordfeltet under passordlabelen

    epost_label.pack(pady=10) # Plasserer passordlabelen under brukernavnfeltet
    epost_entry.pack(pady=5) # Plasserer passordfeltet under passordlabelen

    telefon_label.pack(pady=10) # Plasserer passordlabelen under brukernavnfeltet
    telefon_entry.pack(pady=5) # Plasserer passordfeltet under passordlabelen

    postnr_label.pack(pady=10) # Plasserer passordlabelen under brukernavnfeltet
    postnr_entry.pack(pady=5) # Plasserer passordfeltet under passordlabelen

    registrer = tk.Button(root, text="Registrer", font=("Arial", 20), bg="green", fg="white", command= lambda: reg()) # Oppretter en knapp med teksten "Registrer"
    registrer.pack(pady=10) # Plasserer knappen under postnrfeltet

    tilbake_button = tk.Button(root, text="Tilbake", bg="yellow", fg="white", padx=0, pady=0, font=("Arial", 40), command=lambda: [søk(), root.destroy()]) # Oppretter en tilbakeknapp
    tilbake_button.place(x=590, y=0) # Plasserer tilbakeknappen øverst til høyre på skjermen

def slett_kunde():
    def sikker():
        kunde = kundenr_entry.get()
        ask = tk.messagebox.askquestion("Sikker?", "Er du sikker på at du vil slette kunde " + str(kunde) + "?", icon='warning')
        if ask == 'yes':
            with open('randoms.csv', 'r') as f:
                lines = f.readlines()

            with open('randoms.csv', 'w') as f:
                for number, line in enumerate(lines):
                    if number not in [int(kunde)]:
                        f.write(line)
        else:
            pass

    root = tk.Tk() # Oppretter et vindu
    root.geometry("800x650") # Setter størrelsen på vinduet
    root.resizable(False, False) # Gjør det umulig å endre størrelsen på vinduet

    kundenr_label = tk.Label(root, text="Skriv inn kundenummer på den du vil slette", font=("Arial", 20)) # Oppretter en label med teksten "Username:"
    kundenr_entry = tk.Entry(root, font=("Arial", 20)) # Oppretter et brukernavnfelt

    kundenr_label.pack(pady=10) # Plasserer brukernavnlabelen øverst på skjermen
    kundenr_entry.pack(pady=5) # Plasserer brukernavnfeltet under brukernavnlabelen

    registrer = tk.Button(root, text="Slett", font=("Arial", 20), bg="red", fg="white", command= lambda: sikker()) # Oppretter en knapp med teksten "Slett"
    registrer.pack(pady=10) # Plasserer knappen under postnrfeltet

    tilbake_button = tk.Button(root, text="Tilbake", bg="yellow", fg="white", padx=0, pady=0, font=("Arial", 40), command=lambda: [søk(), root.destroy()]) # Oppretter en tilbakeknapp
    tilbake_button.place(x=590, y=0) # Plasserer tilbakeknappen øverst til høyre på skjermen

def søk():
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

    tilbake_button = tk.Button(root, text="Tilbake", bg="yellow", fg="white", padx=0, pady=0, font=("Arial", 40), command=lambda: [admin(), root.destroy()]) # Oppretter en tilbakeknapp
    tilbake_button.place(x=590, y=0) # Plasserer tilbakeknappen øverst til høyre på skjermen

    lage_button = tk.Button(root, text="Lag ny kunde", padx=0, pady=0, font=("Arial", 40), command=lambda: [lag_kunde(), root.destroy()]) # Oppretter en lag ny kunde knapp
    lage_button.place(x=260, y=300) # Plasserer lag ny kunde knappen øverst til venstre på skjermen

    slette_button = tk.Button(root, text="Slett en kunde", padx=0, pady=0, font=("Arial", 40), command=lambda: [slett_kunde(), root.destroy()]) # Oppretter en lag ny kunde knapp
    slette_button.place(x=250, y=420) # Plasserer lag ny kunde knappen øverst til venstre på skjermen

def admin(): 

    def logout():
        root.destroy() # Lukker vinduet
        hovedside() # Åpner hovedsiden

    root = tk.Tk() # Oppretter et vindu
    root.geometry("800x900") # Setter størrelsen på vinduet
    root.resizable(False, False) # Gjør det umulig å endre størrelsen på vinduet

    logout_button = tk.Button(root, text="Logout", padx=0, pady=0, font=("Arial", 50), command=lambda: [logout(), root.destroy()]) # Oppretter en logoutknapp
    logout_button.place(x=550, y=0) # Plasserer logoutknappen øverst til høyre på skjermen

    sok_button = tk.Button(root, text="Søk", padx=0, pady=0, font=("Arial", 50), command=lambda: [søk(), root.destroy()]) # Oppretter en søkeknapp
    sok_button.place(x=300, y=0) # Plasserer søkeknappen i midten på toppen av skjermen

    avslutt_button = tk.Button(root, text="Avslutt", bg="red", fg="white", padx=0, pady=0, font=("Arial", 50), command=root.destroy) # Oppretter en avsluttknapp
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

    avslutt_button = tk.Button(root, text="Avslutt", bg="red", fg="white", padx=0, pady=0, font=("Arial", 50), command=root.destroy) # Oppretter en avsluttknapp
    avslutt_button.place(x=540, y=770) # Plasserer avsluttknappen nederst til høyre på skjermen

    root.mainloop() # Starter hovedløkken

hovedside()