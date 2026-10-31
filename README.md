# Termux SAM Music System

Termux SAM Music System: sistema completo de música em segundo plano para trabalhar no Termux. Login personalizado, banner SAM, botões de próxima, pausa, anterior e parar, músicas locais e YouTube sem link. Usa MPV, Tmux e YT-DLP leve e otimizado para não travar e não tocar uma música sobre a outra.

## O que ele faz

- Login com nome e senha
- Banner personalizado
- Toca música do celular em segundo plano
- Toca YouTube com link e sem link
- Botões de próxima, pausa, anterior e parar
- Para sozinho quando você dá exit

## Como por seu nome

1. Rode `bash ~/setup.sh`
2. Digite seu nome e crie sua senha
3. Fecha e abre o Termux

## Como instalar

```bash
pkg install mpv yt-dlp tmux socat -y
termux-setup-storage
