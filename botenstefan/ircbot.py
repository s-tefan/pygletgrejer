#!/usr/bin/python3
# Inspired by Linux Academy.

import socket
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
import json
import random
import re
import googletrans
from googletrans import Translator

import locale
from datetime import date
from datetime import datetime
import time

#locale.setlocale(locale.LC_TIME, "sv_SE") #Svenska datum

server = "irc.efnet.org" # Server
#server = "irc.mzima.net"
#server = "efnet.port80.se" # Server
#server = "irc.underworld.no"
channel = "#basvrak"
botnick = "botstefan" # Your bots nick.
adminname = "S-tefan" #Your IRC nickname.
exitcode = "hejdå " + botnick #Text that we will use for exit

from json.decoder import JSONDecodeError

# Read any reminders saved at last nicely executed quit.
"""
with open('reminders.json', 'r') as f:
  try:
    rem = json.load(f)
    with open('reminders.json','w') as file:
      file.write(json.dumps({}))
  except JSONDecodeError:
    rem = {} 
"""

print("Connecting to " + server)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
print("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick)
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8")) # user information
print("NICK "+ botnick)
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot

# Function for several things regarding a day (the current day).
def day(d): 
  text = ""
  today = date.today()
  t_md = today.strftime("%m%d")
  t_date = today.strftime("%Y%m%d")
  
  if d == "day": # All things about the day.
    # Today's date in neat format.
    prettydate = today.strftime('%A, %-d %B, år %Y')
    text = text + 'Idag är det ' + prettydate + '. '
    # Moon phases
    with open ('mdays.json') as f:
      mdays = json.load(f)
    for key, value in mdays.items():
      if t_date in value:
        text = text + key + ". "
    
  if d == "bday" or d == "day": # Birthdays
    with open('bdays.json') as f:
      bdays = json.load(f)
    if t_md in bdays:
      text = text + "Idag fyller " + ' '.join(bdays[t_md]) + " år. "
    else:
      if d == "bday":
        text = text + "Vi känner ingen som fyller år idag. "
      
  if d == "nday" or d == "day": # Name days
    with open('ndays.json') as f:
      ndays = json.load(f)
    if t_md in ndays:
      text = text + ' och '.join(ndays[t_md]) + " har namnsdag. "
    
  if d == "iday" or d == "day": # International days
    with open('idays.json') as f:
      idays = json.load(f)
    if t_md in idays:
      text = text + ' '.join(idays[t_md]) + " "
    else:
      if d == "iday":
        text = text + "Inget internationellt intressant idag. "
      
  if d == "fday" or d == "day": # Flag days
    with open('fdays.json') as f:
      fdays = json.load(f)

    year = today.strftime('%Y')
    if "****" + t_md in fdays or year + t_md in fdays:
      text = text + "Vi flaggar för " + ' '.join(fdays[t_md]) + ". "
    else:
      if d == "fday":
        text = text + "Idag flaggar vi för att vi vill!"

  if d == "day": # More general the day, in this case week of salaries.
    idag = today.strftime('%-d')
    dagnr = today.isoweekday()
    def loningshelg(): # Check if the 25:th is within this working week
      if int(idag) >= 21 and int(idag) <= 29 and dagnr-5 <= int(idag)-25 and dagnr-1 >= int(idag)-25:
        return True
      else:
        return False
    if dagnr >= 6 and loningshelg(): # Mon-Thu
      text = text + 'Det är löningshelg nu. '
    elif dagnr == 5 and loningshelg(): # Fri
      text = text + 'Löningsfredag! '
    elif loningshelg(): # Sat-Sun
      text = text + 'Varning för kommande löningshelg. '
  # Finally, we return the text produced.
  return(text)

# Water temperatures from around the Swedish coast.
def bathtemp(question):
  from bs4 import BeautifulSoup
  import requests

  urls = ["https://www.havochvatten.se/badplatser-och-badvatten/vattenprov-badtemperatur/vattentemperatur-och-kvalitet-pa-badvatten-pa-sydkusten.html",
          "https://www.havochvatten.se/badplatser-och-badvatten/vattenprov-badtemperatur/vattentemperatur-och-kvalitet-pa-badvatten-pa-vastkusten.html",
          "https://www.havochvatten.se/badplatser-och-badvatten/vattenprov-badtemperatur/vattentemperatur-och-kvalitet-pa-badvatten-pa-ostkusten.html",
          "https://www.havochvatten.se/badplatser-och-badvatten/vattenprov-badtemperatur/vattentemperatur-och-kvalitet-pa-badvatten-pa-norrlandskusten.html"]
  temps = {} # For storing the results
  # First, gather all the data.
  for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')
    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows[1:]:
      place = row.find('td', headers='head11').text.replace('­', '')
      wtemp = row.find('td', headers='head13').text.replace('℃', '')
      temp = row.find('td', headers='head14').text.replace('℃', '')
      temps[place] = [wtemp, temp]

  # Empty string to return if no place matches.
  text = ""
  # Loop to find if a place matches the question.
  for key, val in temps.items():
    if question.lower() in key.lower():
      text = text + key + ': ' + val[0] + '°C (hav), ' + val[1] + '°C (luft). '
  return(text)

#So here we take in the channel name, as part of the function, then send the join command to the IRC network. 
def joinchan(chan): # join channel(s).
  ircsock.send(bytes("JOIN "+ chan +"\n", "UTF-8")) 
  print("JOIN " + chan)
  # After sending the join command, we want to start a loop to continually check for and receive new info from server until we get a message with ‘End of /NAMES list.’. 
  #This will indicate we have successfully joined the channel. The details of how each function works is described in the main function section below. 
  #This is necessary so we don't process the joining message as commands.
  ircmsg = ""
  while ircmsg.find("End of /NAMES list.") == -1: # "NAMES" on ircnet, /NAMES on efnet. Confusing.
    time.sleep(1)
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)
    if 'PING' in ircmsg: #In cased we are being pinged during the channel joining process.
      ping(ircmsg)

def ping(text): # respond to server pings.
  ircsock.send(bytes('PONG ' + text.split(':',1)[1] + '\n\r', "UTF-8"))
  print('PONG ' +text.split(':',1)[1])

def channelop(name): #make 'name' op on channel
  ircsock.send(bytes('MODE ' + channel + ' +o ' + name + '\n\r', "UTF-8"))
  
def sendmsg(msg, target=channel): # sends messages to the target, default is channel.
  print("PRIVMSG "+ target +" :"+ msg)
  ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"\n", "UTF-8"))

def doit(name, identity, sentto, message): # act on commands
  global channel
  message = message.strip()
  commandlist = [".hjälp", ".meddela", ".påminn", ".internationella", ".namnsdag", ".födelsedag", ".flaggdag", ".dag", ".vecka", ".mars", ".badtemp", ".översätt"]
  instruction = "Jag kan: " + ', '.join(commandlist) + "."
  target = name # Default: send message in private msg to 'name'.

  # The first word is the command
  command = message.split(' ')[0]
  
  #The help function
  if command == '.hjälp':
    # The default text in case nothing else help related matches.
    text = "Vad vill du ha hjälp med? Skriv '.hjälp [.kommando]' för mer hjälp. Kommandon jag kan: " + ', '.join(commandlist) + "."
    # If there is another word, check if that word is a correct command.
    if ' ' in message:
      helpwith = message.split(' ',1)[1].strip()
      if helpwith == '.hjälp':
        text = "Skriv: '.hjälp [.kommando]' för mer hjälp. Kommandon jag kan: " + ', '.join(commandlist) + "."
      elif helpwith == '.meddela':
        text = "Skriv: '.meddela [mottagare] [meddelande]' för att använda meddelandetjänsten. Mottagare kan vara person-nick eller kanal."
      elif helpwith == '.påminn':
        text = "Skriv: '.påminn [mottagare] [meddelande]' för att använda påminnelsetjänsten. Om mottagare är person, får person reda på det nästa gång hen säger något i kanalen. Om mottagare är kanalen, så påminns det så fort någon säger något i kanalen."
      elif helpwith == '.internationella':
        text = "En lista över internationella dagar. Skriv bara '.internationella' för att få dagens internationella dagar."
      elif helpwith == '.namnsdag':
        text = "Skriv '.namnsdag' för att få dagens namnsdagar."
      elif helpwith == '.födelsedag':
        text = "Skriv '.födelsedag' för att få veta om någon vi känner fyller år idag."
      elif helpwith == '.flaggdag':
        text = "Skriv '.flaggdag' för att få reda på varför vi flaggar idag."
      elif helpwith == '.dag':
        text = "Skriv '.dag' för att få reda på ganska mycket om idag."
      elif helpwith == '.vecka':
        text = "Skriv '.vecka' för att få reda på vilken vecka det är."
      elif helpwith == '.mars':
        text = "Skriv '.mars' för att få reda på vilken mars 2020 det är."
      elif helpwith == '.badtemp':
        text = "Skriv '.badtemp [ort]' för att få badtemperatur för orten. Skriver du t.ex. 'berg' så får du temperaturer för både Varberg och Falkenberg. Datakälla: Havs- och Vattenmyndigheten, https://www.havochvatten.se/badplatser-och-badvatten.html"
      elif helpwith == '.översätt':
        text = "Skriv '.översätt' följt av texten du vill översätta. Om du vill välja språk, så gör du på följande sätt: '.översätt (da)' för att översätta efterföljande text till danska. '.översätt (fi:sv) för att översätta efterföljande text från finska till svenska. Skriv '.översätt .språk' för att få en lista över tillgängliga språk."
        
  # Other commands
  elif command == '.flaggdag':
    text = day("fday")
    if sentto == channel:
      target = channel
  elif command == '.födelsedag':
    text = day("bday")
    if sentto == channel:
      target = channel
  elif command == '.namnsdag':
    text = day("nday")
    if sentto == channel:
      target = channel
  elif command == '.internationella':
    text = day("iday")
    if sentto == channel:
      target = channel
  elif command == '.dag':
    text = day("day")
    if sentto == channel:
      target = channel
  elif command == '.vecka':
    today = date.today()
    v = today.strftime('%V')
    text = 'Det är vecka ' + v + '.'
    if sentto == channel:
      target = channel
  elif command == '.mars':
    today = date.today()
    d0 = date(2020, 2, 29)
    delta = today - d0
    text = 'Idag är det ' + today.strftime('%A, ') + str(delta.days) + ' mars, år 2020.'
    if sentto == channel:
      target = channel
  elif command == '.badtemp': # Bath temperatures.
    if len(message.split(' ')) >= 2: # If a place is specified.
      if sentto == channel:
        target = channel
      place = message.split(' ')[1]
      text = bathtemp(place)      
      if text == '': # If there is no matching place.
        text = "Hittade ingen badplats eller ort med '" + place + "' i. Försök igen."
        target = name
    else: # If no place is spacified.
      text = "Skriv '.badtemp [ort]' för att få badtemperatur för orten."
      target = name

  elif command == '.översätt': # Translations
    translator = Translator()
    all_lang = googletrans.LANGUAGES.keys()
    if len(message.split(' ')) > 2 and re.match('\(.*\)', message.split(' ')[1]): # If there is at least three words and the second word is in parenthesis
      languages = message.split(' ')[1][1:-1].split(':') # Makes a list of one or two language codes.
      srctext = message.split(' ',2)[2] # The text to translate
      if len(languages) == 1 and languages[0] in all_lang: # There is only one language, check if it is valid.
        destlang = languages[0]
        text = translator.translate(srctext, dest=destlang).text
        if sentto == channel:
          target = channel
      elif len(languages) == 2 and languages[0] in all_lang and languages[1] in all_lang: # There are two languages, check if they are valid.
        srclang = languages[0]
        destlang = languages[1]
        text = translator.translate(srctext, dest=destlang, src=srclang).text
        if sentto == channel:
          target = channel
      elif len(languages) > 2 and all (l in all_lang for l in languages): # A game of "Chinese whispers"
        temp = srctext
        for i,l in enumerate(languages[:-1]): # Check if all language codes are valid.
          temp = translator.translate(temp, src=languages[i], dest=languages[i+1]).text
        text = temp
        if sentto == channel:
          target = channel
      else: # The languages are not valid.
        target = name
        text = "Giltiga språkkoder: " + ', '.join(all_lang) + '.'
    elif len(message.split(' ')) > 1 and message.split(' ')[1] == '.språk': # To get all available languages
      text = ', '.join(all_lang) + '.'
    elif len(message.split(' ')) > 1: # If no languages are provided
      srctext = message.split(' ',1)[1]
      text = translator.translate(srctext).text
      if sentto == channel:
        target = channel
    else:
      text = "Skriv '.översätt' följt av texten du vill översätta. Om du vill välja språk, så gör du på följande sätt: '.översätt (da)' för att översätta efterföljande text till danska. '.översätt (fi:sv) för att översätta efterföljande text från finska till svenska. Skriv '.översätt .språk' för att få en lista över tillgängliga språk."

  #Check for the longer commands ... But first if 
  elif len(message) <= 1 or len(message.split(' ')) < 3:
    text = "Syntax error. Försök igen. " + instruction
  else: # We have something here, it might be a valid action.

    # Tell someone something ...
    if command == '.meddela':
      target = message.split(' ')[1]
      text = message.split(' ',2)[2]
    elif command == '.påminn': # Save a reminder for someone, to tell when they says something in the channel.
      target = message.split(' ')[1]
      text = message.split(' ',2)[2]
      global rem
      # First, fix the reminder
      remind_person = target
      reminder = text + " (hälsar " + name + ")"
      # Then, the confirmation message
      target = name
      text = "Jag ska påminna " + remind_person + " att '" + reminder + "' nästa gång hen säger något i " + channel + "."
      if remind_person == channel: # If a channel shall be reminded
        text = "Jag ska påminna att '" + reminder + "' nästa gång någon säger något i " + channel + "."
      # If person has no reminders, att them to dictionary.
      if remind_person not in rem.keys():
        rem[remind_person] = [reminder]
      else: # If person has reminders, just add another one.
        rem[remind_person].append(reminder)
        
    else: # If the command is unknown to the bot.
      text = instruction
  sendmsg(text, target)
  
def main():
  #joinchan(channel) #Does not work properly on ircnet to join immediately.
  #Start infinite loop to continually check for and receive new info from server. This ensures our connection stays open. 
  while 1:
    time.sleep(0.5)
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)
    now = datetime.now()
    today = date.today()
    time.sleep(0.5)
    
    #Here we check if the information we received was a PRIVMSG. PRIVMSG is how standard messages in the channel (and direct messages to the bot) will come in. 
    #Most of the processing of messages will be in this section.
    # Check that it is a message of some kind, and not some info from the server.
    if ' ' in ircmsg and ircmsg.split(' ')[1] == "PRIVMSG":

      #Messages come in from from IRC in the format of ":[Nick]!~[hostname]@[IP Address] PRIVMSG [channel] :[message]”
      #We need to split and parse it to analyze each part individually.
      name = ircmsg.split('!',1)[0][1:] # Who sent.
      identity = ircmsg.split('!',1)[1].split(' ',1)[0] # Identity of the sender.
      sentto = ircmsg.split(' ')[2] #For checking if it was a private message or sent to the channel
      message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1] # The message sent.

      #Now that we have the name information, we check if the name is less than 17 characters. Usernames (at least for Freenode) are limited to 16 characters. 
      #So with this check we make sure we’re not responding to an invalid user or some other message.
      if len(name) < 17:

        # Check for reminders when someone says something in the channel.
        # Personal reminders
        global rem
        if sentto == channel and name in rem.keys(): # Check if 'name' has any reminders.
          remlist = rem.pop(name)
          for item in remlist:
            time.sleep(1)
            sendmsg(name + ': ' + item)
        # General reminders to the channel
        if sentto == channel and channel in rem.keys():
          remlist = rem.pop(channel)
          for item in remlist:
            time.sleep(1)
            sendmsg("Till den som ser det: " + item)

        # Coffe. To be further developed.
        if sentto == channel and 'kaffe' in message.lower() and random.choice([True, False]):
          h = today.strftime('%H')
          if int(h) > 17:
            text = name + ': Det är för sent för kaffe nu.'
          else:
            text = name + ': Ja! Kaffe!'
          time.sleep(random.randint(1,8)/3)
          sendmsg(text)

        # 13:37
        t = now.strftime("%H:%M")
        if t == '13:37':
          text = "leet!"
          sendmsg(text)
          
        #Admin can ask the bot to join the channel
        if name == adminname and sentto == botnick and 'joina' == message:
          joinchan(channel)

        if ('omhu' == message.lower().strip() or 'hor unge' in message.lower() or 'hor ungar' in message.lower()) and sentto == channel:
          oplist = ['~stefan@78-72-137-31-no71.tbcn.telia.com', '~luxia@158.174.17.240', '~emilie@78-72-51-77-no232.tbcn.telia.com',
                    'elgreso@31.7.187.215', '~mort@yama.ita.chalmers.se', '~edman@158.174.17.240', '~cd@cykranosh.com',
                    '~sama@158.174.17.240', '~cos@liua.netizen.se', '~mikaelj@c83-248-173-75.bredband.comhem.se', 'luxia@158.174.17.240',
                    'sama@158.174.17.240', 'edman@158.174.17.240']
          if identity in oplist:
            channelop(name)
          else:
            sendmsg('Nej, inte du, ' + name + '.')

        # Greeting
        hellolist = ['hej', 'hello', 'hallå', 'tjenare', 'morrn', 'tjipp', 'hejsan', 'howdy', 'goddag', 'haj']
        if any(hello in message.lower() for hello in hellolist) and botnick in message:
          if sentto == botnick:
            time.sleep(random.randint(1,8)/3)
            sendmsg("Hej på dig, " + name + "!", name)
          else:
            time.sleep(random.randint(1,8)/3)
            sendmsg(name + ": " + "Hej på dig!")

        #Look to see if the name of the person sending the message matches the admin name we defined earlier. 
        #We also make sure the message matches the exit code above. The exit code and the message must be EXACTLY the same. 
        #This way the admin can still type the exit code with extra text to explain it or talk about it to other users and it won’t cause the bot to quit. 
        #The only adjustment we're making is to trim off any whitespace at the end of the message. So if the message matches, but has an extra space at the end, it will still work.
        if name.lower() == adminname.lower() and message.rstrip().lower() == exitcode:
          #If we do get sent the exit code, then send a message (no target defined, so to the channel) saying we’ll do it, but making clear we’re sad to leave.
          sendmsg("OK. Hejdå. :'(")
          #Send the quit command to the IRC server so it knows we’re disconnecting.
          ircsock.send(bytes("QUIT Hejdå!\n", "UTF-8"))
          print("Nice quit.")
          with open('reminders.json','w') as file: # Save the reminders until next time.
            file.write(json.dumps(rem, sort_keys=True, indent=2, ensure_ascii=False))
          return

        if "corona" in message.lower() or "covid" in message.lower():
          doit(name, identity, sentto, ".mars")
        
        if message[0] == '.' and len(message) > 1 and not(message[1] =='.'): # The commands start with '.', but not with '..'
          doit(name, identity, sentto, message)
        elif sentto == botnick: # Whenever someone sends anything not known to the bot.
          text = "Skriv '.hjälp' för att få reda på vad jag kan."
          sendmsg(text, name)

    #If the message is not a PRIVMSG it still might need some response.
    else:
      #Check if the information we received was a PING request. If so, we call the ping() function we defined earlier so we respond with a PONG.
      if 'PING' in ircmsg:
        ping(ircmsg)
      if ' ' in ircmsg and ircmsg.split(' ')[1] == "MODE":
        if ircmsg.split(' ')[2] == channel and '+o' in ircmsg.split(' ')[3] and botnick in ircmsg.split(' ',4)[4]: # Bot was opped!
          #:luxia!~luxia@158.174.17.240 MODE #basvrak +o botenanna
          #:luxia!~luxia@158.174.17.240 MODE #basvrak +ooo botenanna S-tefan gres
          name = ircmsg.split('!',1)[0][1:] # Who did it.
          text = name + ': Tack för bullen!'
          sendmsg(text)

#Finally, now that the main function is defined, we need some code to get it started.
main()
