import os, time

nome = input("qual seu nome? ")

while True:
    senha = input("MAS PRA TER CERTEZA QUAL SUA SENHA?: ")
    if senha == "1234":
        print(f"BEM-VINDO DE VOLTA, {nome}")
        break
    else:
        print("senha errada, tente de novo")

time.sleep(1)
print("\nQuer ouvir musica enquanto trabalha?")
print("[1] Musica sem link")
print("[2] Musica com link")
print("[3] Sem musica")
print("[4] YouTube sem link")
opcao = input("Escolhe: ")

os.system("pkill -9 mpv; tmux kill-server 2>/dev/null; sleep 1")

if opcao == "1":
    os.system("termux-wake-lock; tmux new-session -d -s musica 'mpv --no-video --loop=inf ~/storage/music/'")
    print("Tocando suas musicas do celular...")

elif opcao == "2":
    link = input("Cola o link aqui: ")
    os.system(f"termux-wake-lock; tmux new-session -d -s musica 'mpv --no-video \"{link}\"'")
    print("Tocando seu link...")

elif opcao == "3":
    print("Sem musica entao, bora pro trampo!")

elif opcao == "4":
    print("\nQual estilo?")
    print("[1] Lofi pra trampar")
    print("[2] Phonk")
    print("[3] Pesquisar pelo nome")
    sub = input("Escolhe: ")
    if sub == "1":
        link = "https://www.youtube.com/watch?v=jfKfPfyJRdk"
    elif sub == "2":
        link = "ytdl://ytsearch10:phonk"
    elif sub == "3":
        nome_musica = input("Qual musica? ")
        link = f"ytdl://ytsearch10:{nome_musica}"
    else:
        link = "ytdl://ytsearch10:lofi hip hop"
    os.system(f"termux-wake-lock; tmux new-session -d -s musica 'mpv --no-video --loop=inf \"{link}\"'")
    print("Tocando do YouTube sem abrir nada...")
else:
    print("Nao entendi, seguindo sem musica...")
