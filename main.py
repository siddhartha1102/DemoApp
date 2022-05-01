import streamlit as st
import pandas as pd
st.title("D Siddhartha")
from PIL import Image
image = Image.open('Image.jpg')
st.image(image,width=300 )
st.subheader('''Address:
B6-204, L&T South City, Arekere Mico Layout, Bangalore – 560076
Phone: +91 7760517242,\n
 Email: siddharthadronamraju@gmail.com
''')

with st.expander("Objective "):
    st.write("""
Final Year MCA (Master of Computer application) student seeking an Entry-level position in 
the field of information technology with emphasis on Product Development and Research
    """)
with st.expander("Proficency "):
    st.header("Languages")
    st.write("Python, C, C++, Familiar with Arduino script, Java, Java-script,")

    st.header("DBMS")
    st.write("Oracle 10g, MySQL")

    st.header("Tools And platforms")
    st.write("Arduino IDE, Familiar with ESP 8266, Raspberry Pi")
with st.expander("Education"):
    st.table(pd.read_excel("qualifications.xlsx").astype(str),engine='openpyxl',)
with st.expander("Blogs"):
    st.header("Python Blog")
    st.write('https://mypythonprograms11.blogspot.com/')

with st.expander("Projects "):

    st.header("E-Rozgar")
    st.write('''Recruiters are the source of resources, Jobseekers can 
    find and apply for the job as per their requirements. Companies can place 
    their vacancy profile on the site and can also search job seekers' resumes. 
    In this we have integrated in-app chat 
    wich uses the publish-subscribe architecture PubNub -JavaScript API.''')



    st.header("Voice based Home Automation")
    st.write("""The home automation system is designed to operate devices non-smart devices with Voice Commands
Components of the system: Google assistant, Pub Nub service, IFTTT, Raspberry Pi and a relay board.""")

    st.subheader("Voice Command Processing ")
    st.caption("""Google assistant app on android device receives voice commands and translates them to text commands. The commands in text format are interpreted by IFTTT cloud service using predefined applets.
 Applets in IFTTT send this message to Publisher/Subscriber service (Pub Nub) to subscribed entities.""")
    st.caption("""The Python app on Raspberry Pi subscribes for the messages from PubNub and waits for the messages 
Messages received from Pub-Nub are interpreted by Raspberry Pi """)
    st.caption("The Python program on Raspberry Pi receives the message and drives relays connected to GPIO pins as per the command.")
    st.subheader("Intrusion Detection")
    st.caption("""Photo sensors trigger an intrusion detection event. The Python app on Raspberry Pi sends SMS to the registered mobile using a cloud-based SMS service provider.
The program was developed using Python for execution on Raspberry pi""")

    st.header("Gesture controlled media player")
    st.write('''The gesture control system is used to control media player functions 
    (play or pause a video, change the volume,
     forward and rewind.) The media player can be running on any Windows host.''')
    st.write('''Components of the system: A windows laptop with a media player, Ultrasonic Sensors to detect motion via range detection, Arduino board to receive sensor input from sensors and send commands to laptop via serial interface. ''')

    st.subheader("Software for Gesture Control Project ")
    st.caption('Arduino script was developed to receive sensor input and perform media player control using a python library.')
    st.caption('The distance information from Arduino is collected by a Python Program which converts the data into keyboard click actions for media player control. ')
    st.caption('A utility on the laptop listens on the laptop COM port and emulates key board actions for media player control. ')

    st.subheader("Functional Description")
    st.caption('''Place your hand in front of the Ultrasonic Sensor. One sensor is used for start / stop gesture detection (toggle). A second sensor is used for volume increase or decrease based on time of response from the sensor.''')
    st.caption('''Based on gesture event, relevant media control on the computer is performed.''')

with st.expander("Achievements"):
    l=["Won first place for demonstrating Voice based home automation at St. Joseph College",
"Won third place for demonstrating Voice based home automation at Vijaya College",
"Won first place for demonstrating Voice based home automation at Oxford College",
"Won Second prize for demonstrating Home Automation at the district level Science Fair organized by Karnataka Vigyan Parishad",
"Won Second prize in the electronics circuit analysis competition at Oxford college",
"Won Second Prize in “Pick and Speak” inter-college competition organized by St Joseph College. ",
"Participated in Web Page Development Workshop organized by WordPress ",
"Active participant in multiple science and technology fairs"]
    for m in l:
        st.caption(m)
