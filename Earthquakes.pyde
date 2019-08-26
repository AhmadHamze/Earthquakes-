add_library('pdf')
import csv

#time,latitude,longitude,mag,place 
size(1400,700)
beginRecord(PDF,"Earthquakes.pdf")

shape(loadShape("WorldMap.svg"),0,0,width,height)
noStroke()

with open("EarthquakeData.csv",'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i,li_ne in enumerate(csv_reader):
        graphLong = map(float(li_ne["longitude"]),-180,180,0,width)
        graphLat = map(float(li_ne["latitude"]),-90,90,height,0)
        magnitude = sqrt((float(li_ne["mag"])/2)/PI)
        if i < 3:
            fill(255,0,0,50)
            ellipse(graphLong,graphLat,20*magnitude,20*magnitude)
            fill(0)
            text(li_ne["place"] + "\n" +li_ne["mag"] + "Richter",graphLong-150,graphLat)
        else:
            fill(0,0,255,50)
            ellipse(graphLong,graphLat,5*magnitude,5*magnitude)
    textMode(MODEL)
    textFont(createFont("Times New Roman",20))
    fill(0)
    text("2000 Earthquakes\n2000-2012",700,650)
endRecord()
print "file saved successfully!"
