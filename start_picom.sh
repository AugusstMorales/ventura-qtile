#!/bin/bash
# Mata cualquier instancia previa de Picom
pkill -x picom
sleep 0.1  # Pequeña pausa para evitar conflictos
# Inicia Picom con config y log detallado
/usr/bin/picom --config /home/augusstmorales/.config/picom/picom.conf --backend glx --vsync &>> /tmp/picom.log &