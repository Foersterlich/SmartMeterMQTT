#!/bin/bash

echo "🔧 Starte die Einrichtung des SmartMeter-Systems..."

# Update Paketlisten (optional)
echo "📦 Aktualisiere Paketlisten..."
sudo apt update && sudo apt upgrade -y

# Installiere Python und pip, falls nicht vorhanden
echo "🐍 Installiere Python und pip..."
sudo apt install python3 python3-pip python3-venv -y

# Erstelle ein Virtual Environment
echo "📂 Erstelle ein Virtual Environment..."
python3 -m venv smartmeter_env
source smartmeter_env/bin/activate

# Installiere Abhängigkeiten
echo "📌 Installiere benötigte Python-Bibliotheken..."
pip install -r requirements.txt

# Starte das Python-Programm
echo "🚀 Starte SmartMeterMQTT..."
python smartmeter_mqtt.py

echo "✅ Installation abgeschlossen! Das SmartMeterMQTT-System läuft."
