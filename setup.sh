#!/data/data/com.termux/files/usr/bin/bash
clear
echo "Vamos deixar seu Termux com seu nome!"
read -p "Qual seu nome? " MEUNOME
read -p "Cria uma senha pra você: " MINHASENHA
sed -i "s/1234/$MINHASENHA/g" ~/banner.py
sed -i "s/♥SAM♥/♥$MEUNOME♥/g" ~/banner.sh
echo "Pronto, $MEUNOME! Fecha e abre o Termux de novo."
