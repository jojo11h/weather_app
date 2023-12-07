from reportlab.pdfgen import canvas
import json
import os


with open("file.json") as file:
    data = json.load(file)

pdf_file = "weather_report.pdf"
temp_celcius = data['main']['temp']-273.15
weather = data['weather'][0]['description'].split()[-1]
wind = data['wind']['speed'] * 1.609344

c = canvas.Canvas(pdf_file)
c.drawString(100, 800, f"Ville : {data['name']}")
c.drawString(100, 780, f"Temperature : {temp_celcius:.2f} °C")
c.drawString(100, 760, f"Ciel : {weather}")
c.drawString(100, 740, f"Vitesse du vent : {wind:.2f} km/h")


c.save()


os.startfile(pdf_file)
+17345476725
