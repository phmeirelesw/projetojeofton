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

# Carrega nova pergunta
def load_question():
    selected_option.set("")
    feedback_label.config(text="")
    question = questions[current_question]
    question_label.config(text=f"{current_question + 1}. {question['question']}")
    for i in range(4):
        options[i].config(text=question["options"][i], value=question["options"][i])

# Mostra resultado final
def show_result():
    for widget in main_frame.winfo_children():
        widget.destroy()

    result = f"Você acertou {score} de {len(questions)} perguntas!"
    final_label = ttk.Label(main_frame, text=result, font=("Poppins", 16))
    final_label.pack(pady=20)

    btn_sair = ttk.Button(main_frame, text="Sair", command=window.destroy)
    btn_sair.pack()

# Criar janela
window = tk.Tk()
window.title("Quiz de Super-Heróis")
window.geometry("500x400")
window.resizable(False, False)

# Estilo moderno
style = ttk.Style(window)
style.theme_use("clam")
style.configure("TLabel", font=("Poppins", 12))
style.configure("TRadiobutton", font=("Poppins", 11))
style.configure("TButton", font=("Poppins", 12), padding=6)

# Frame principal
main_frame = ttk.Frame(window, padding=20)
main_frame.pack(expand=True, fill="both")

# Pergunta
question_label = ttk.Label(main_frame, text="", wraplength=450, anchor="center", font=("Poppins", 14, "bold"))
question_label.pack(pady=15)

# Opções
selected_option = tk.StringVar()
options = []
for i in range(4):
    rb = ttk.Radiobutton(main_frame, text="", variable=selected_option, value="")
    rb.pack(anchor="w", pady=2)
    options.append(rb)

# Feedback
feedback_label = ttk.Label(main_frame, text="", font=("Poppins", 11))
feedback_label.pack(pady=10)

# Botão próxima
btn_next = ttk.Button(main_frame, text="Próxima", command=next_question)
btn_next.pack(pady=10)

# Estilo da barra de progresso verde
style.configure("green.Horizontal.TProgressbar", troughcolor="white", background="green")

# Barra de progresso
progress = ttk.Progressbar(
    main_frame,
    length=400,
    mode="determinate",
    maximum=len(questions),
    style="green.Horizontal.TProgressbar"
)
progress.pack(pady=10)

# Iniciar
load_question()
window.mainloop()
