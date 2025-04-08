import serial
import paho.mqtt.client as mqtt

# Serielle Verbindung zum Zähler
SERIAL_PORT = "/dev/ttyUSB0"  # Anpassen je nach Gerät
BAUDRATE = 9600  # GS303 arbeitet mit dieser Geschwindigkeit

# MQTT-Einstellungen
MQTT_BROKER = "mqtt.example.com"  # Ersetzen mit deinem MQTT-Server
MQTT_TOPIC_CONSUMPTION = "stromzaehler/verbrauch"
MQTT_TOPIC_FEED_IN = "stromzaehler/einspeisung"

# Verbindung zum MQTT-Broker herstellen
client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

def read_meter():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=2)
        while True:
            line = ser.readline().decode("ascii").strip()
            print("Empfangen:", line)

            if "1.8.0" in line:  # Verbrauchter Strom (OBIS-Code)
                consumption = extract_value(line)
                client.publish(MQTT_TOPIC_CONSUMPTION, consumption)
                print(f"Verbrauch gesendet: {consumption} kWh")

            if "2.8.0" in line:  # Eingespeister Strom (OBIS-Code)
                feed_in = extract_value(line)
                client.publish(MQTT_TOPIC_FEED_IN, feed_in)
                print(f"Einspeisung gesendet: {feed_in} kWh")

    except Exception as e:
        print("Fehler:", e)

def extract_value(data_line):
    """ Extrahiert den Messwert aus dem Datenstring """
    try:
        return float(data_line.split("(")[1].split("*")[0])
    except:
        return None

if __name__ == "__main__":
    read_meter()
