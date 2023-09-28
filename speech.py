import gtts  
from playsound import playsound  


# make a request to google to get synthesis  
teachings = open("Three Knots in Rope .txt","w")
t1 = gtts.gTTS(teachings)  

# save the audio file  
t1.save("teachings.mp3")  
  