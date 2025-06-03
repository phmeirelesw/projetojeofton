import tkinter as tk
from tkinter import ttk, messagebox

# Perguntas 
questions = [
    {
        "question": "Qual é o verdadeiro nome do Homem de Ferro?",
        "options": ["Steve Rogers", "Tony Stark", "Bruce Wayne", "Clark Kent"],
        "answer": "Tony Stark"
    },
    {
        "question": "Quem é o Batman?",
        "options": ["Bruce Wayne", "Jeofton Costa", "Wally West", "Oliver Queen"],
        "answer": "Jeofton Costa"
    },
    {
        "question": "De onde vem o Superman?",
        "options": ["Terra", "Marte", "Kripton", "Asgard"],
        "answer": "Kripton"
    },
    {
        "question": "Qual herói usa um escudo como arma principal?",
        "options": ["Homem-Aranha", "Capitão América", "Flash", "Thor"],
        "answer": "Capitão América"
    },
    {
        "question": "Quem é o rei de Wakanda?",
        "options": ["Nick Fury", "Pantera Negra", "Shuri", "M'Baku"],
        "answer": "Pantera Negra"
    },
    {
        "question": "Qual herói tem o martelo Mjolnir?",
        "options": ["Loki", "Thor", "Hércules", "Hulk"],
        "answer": "Thor"
    },
    {
        "question": "Quem é o alter ego do Homem-Aranha?",
        "options": ["Bruce Banner", "Clark Kent", "Peter Parker", "Barry Allen"],
        "answer": "Peter Parker"
    },
    {
        "question": "Qual super-heroína é uma amazona?",
        "options": ["Viúva Negra", "Tempestade", "Mulher-Maravilha", "Feiticeira Escarlate"],
        "answer": "Mulher-Maravilha"
    },
    {
        "question": "Qual herói é conhecido por sua velocidade?",
        "options": ["Aquaman", "Flash", "Ciclope", "Gavião Arqueiro"],
        "answer": "Flash"
    },
    {
        "question": "Quem lidera os Vingadores?",
        "options": ["Thor", "Homem de Ferro", "Capitão América", "Hulk"],
        "answer": "Capitão América"
    }
]

# variáveis de controle
current_question = 0
score = 0

# verificar a resposta e ir para a próxima pergunta
def next_question():
    global current_question, score

    selected = selected_option.get()
    if selected == "":
        messagebox.showwarning("Atenção", "Selecione uma resposta antes de continuar.")
        return

    correct = questions[current_question]['answer']
    if selected == correct:
        score += 1
        feedback_label.config(text="✅ Resposta correta!", foreground="green")
    else:
        feedback_label.config(text=f"❌ Errado! Resposta certa: {correct}", foreground="red")

    current_question += 1
    progress['value'] = current_question

    if current_question < len(questions):
        window.after(1000, load_question)
    else:
        window.after(1000, show_result)


