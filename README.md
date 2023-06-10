# AI-based-system-for-accident-and-theft-detetction
1.	INTRODUCTION

Road accidents are increasing daily as the number of automobiles rises. An annual global death toll of 1.4 million and an injury toll of 50 million are reported by the WHO. Lack of access to healthcare is the main cause of death at the scene of the accident or the lengthy reaction time during the rescue effort. It has been noted that while emergency assistance will soon be available in locations with high traffic or in cities, it is more challenging to deliver it quickly on highways or in rural areas. It has been noted that delays in medical care cause serious injuries to result in mortality . To decrease the amount of fatalities from traffic accidents, an intelligent accident detection and warning system is required. Once the system identifies an accident, it will notify all emergency services like hospitals, police stations, and so on.


![image](https://github.com/Jess-12/AI-based-system-for-accident-and-theft-detetction/assets/127778661/410b3cc7-9d9d-4e30-9136-c5b1c810e0b8)

Causes of accidents
Along with accident vehicle theft has escalated globally in recent years. To combat vehicle theft, numerous vehicle anti-theft technologies were created and put into use. However, it remains a difficult challenge to address the problem of vehicle theft. Once a car is stolen, the smart system provides a quick tracking system to locate it.
This report puts out the concept of an intelligent AI system for theft and accident detection.
![image](https://github.com/Jess-12/AI-based-system-for-accident-and-theft-detetction/assets/127778661/33d329d7-6165-4f89-ab06-068a2c23cb1e)


Number of theft cases by its kind



1.1	Motivation


•	Every year, numerous people pass away in road accidents. Nothing will ever be valued more highly than a human life. Our motto is "No one will perish in a car accident." Technology has the potential to improve our way of life. As our nation grows every day, we will all need to embrace technology. Therefore, we need to resolve this issue. The IOT idea along with AI is being used in this project to ensure the safety of the victim whose life is in danger due to a road accident.

•	Many vehicles are stolen each day around the world, and the main cause is that the owner is unaware of both the time and place of the theft. So, to "Reduce the amount of automobiles stolen" is our motto. Therefore, a sophisticated system will be implemented to identify the theft and notify the owner of the theft as well as the whereabouts of the car.
.
 
1.2	Objective

The system primarily uses a smart system to prevent accidents and theft . The system comprises 4 features.
1)	Identifying accidents and informing nearby hospitals or the family about the accident's location.

2)	A voice recording device to capture the driver's voice in order to determine the cause of accident.
3)	Face recognition to identify the person who stole the car and mailing the owner a photo of the thief.

2.	Existing Work / Literature Review


2.1.	Smartphone-Based Systems
These systems employ a smartphone's different sensors to identify and warn users of traffic accidents. An accelerometer and GPS data were employed to locate the sites of the accidents. This method does not alert any emergency agencies , it merely detects an accident .Another proposal for an accident detection technique uses a GPS module to pinpoint the accident's location and a mobile message to alert the hospitals. The primary drawback of this paper is that there is just one sensor being used. Therefore, the entire system will malfunction if the sensor is ineffective.
Additionally, it can lead to more false alarms.

A smartphone-based accident detection and reporting system was suggested , For the purpose of identifying car accidents, the G-force value, noise, and speed are used. Noise and gravitational force are extracted using the mobile sensor and accelerometer (microphone). An alert is sent to the emergency number as soon as the accident is discovered. This gadget may overreact when an accident occurs at a low speed because speed is an important component for accident detection.
An Android app for accident notification and identification has been made in another proposal .To find an accident, they have merely utilized a GPS module and an accelerometer mobile sensor.
When the accident is located, it calls the emergency number with a pre-recorded audio message.
 


2.2.	Deep Learning-Based Systems
The proposed system is an intelligent accident detection and rescue system which mimics the cognitive functions of the human mind using the Internet of Things (IoTs) and the Artificial Intelligence system (AI). An IoT kit is developed that detects the accident and collects all accident-related information, such as position, pressure, gravitational force, speed, etc., and sends it to the cloud. In the cloud, once the accident is detected, a deep learning (DL) model is used to validate the output of the IoT module and activate the rescue module. Once the accident is detected by the DL module, all the closest emergency services such as the hospital, police station, mechanics, etc., are notified. Ensemble transfer learning with dynamic weights is used to
minimize the false detection rate. Due to the dataset’s unavailability, a personalized dataset is generated from the various videos available on the Internet. The proposed method is validated by a comparative analysis of ResNet and InceptionResnetV2.

2.3.	8051-Based Theft Detection
The main purpose of this project is to prevent vehicle theft. This functionality is achieved by detecting vehicle status in theft mode and by sending an SMS which is generated automatically. This SMS is then sent to the owner of the vehicle. The owner can then send back the SMS in order to disable the ignition of the vehicle. Thus in this way crimes can be reduced to a great extent as vehicles today are being stolen in large number. How the system works is when a person tries to steal the vehicle, the microcontroller is interrupted and the command is sent to the GSM modem to send SMS. On the receipt of the message, the owner sends back the SMS to the GSM modem.
This is done in order to stop the engine. This GSM modem is interfaced to the microcontroller. This microcontroller on the receipt of the message uses a mechanism that helps to stop the engine. Motor is being used in this project in order to indicate vehicle ON/OFF state. This project was done using a 8051 controller which has a less compatibility and feasibility compared to RassberryPi.

3.	Topic of the work


•	System Design / Architecture


Accident and Alert System

![image](https://github.com/Jess-12/AI-based-system-for-accident-and-theft-detetction/assets/127778661/d1d48189-cf26-48a5-a9db-b19c80cc959f)

Block diagram for accident and alert System

Theft Detection

![image](https://github.com/Jess-12/AI-based-system-for-accident-and-theft-detetction/assets/127778661/c1194976-2c26-467a-9724-5fec10a42e4b)

 Block diagram for 
 
Theft detectionFace Recognition

![image](https://github.com/Jess-12/AI-based-system-for-accident-and-theft-detetction/assets/127778661/2b840a78-1fbf-4765-9743-170ba22bbc1d)

Methodology for Face Recognition


•	Working Principle


Accident Detection and Alert System
•	When the system gets started GPS gets initialized which receives the signal from the satellite and transfer the latitude and longitude value to the receiver.
•	GSM receives the message and then it gets started through which the message is been send to emergency server numbers.
 
•	While travelling if the accident occurs then it is been sensed by the vibration sensor, which gives indication to the system to send the alert message to the nearby ambulance, police station and insurance office numbers given in the program.
•	A threshold value is been set to which if the value goes beyond the threshold value then the alert message is been send.
•	The System will even have a voice recording system to record the voice which gets initialized when the vehicle starts. The recording system record the sound to know the mode of accident

Theft Detection and Alert System
•	When the system gets started GPS gets initialized which receives the signal from the satellite and transfer the latitude and longitude value to the receiver.
•	GSM(Twilio Api) receives the message and then it gets started through which the message is been sendto the owner.
•	The camera module in the system identifies the owner , if the recognized person is not the owner or friends/family members then the face is captured and mailed or messaged to the owner.
•	If the automobile is stolen then the current location of the vehicle is sent to the owner.


•	Expected Results
•	The system will identify the accident and provide neighbouring hospitals or family members the accident's location on Google Maps through SMS so that the injured person can receive care as soon as possible.
•	The system contains a voice recorder which will capture audio in order to determine the cause of accident.
•	The system will even be able to tell if the car is stolen or not, and if it is, it will notify the owner the car's current location on Google Maps through SMS so that they can monitor it.
•	The system features a camera module that can recognize faces and determine whether they belong to the owner or not. If the automobile is taken, the owner will receive a mail or SMS message with the image of the criminal.
 
•	Results

•	Simulations :

•	In order to preview the outcomes prior to implementing the circuit in real life, a simulation was carried out using Proteus software. This approach allowed for an evaluation of the results in a virtual environment before proceeding with the actual circuit integration. By utilizing Proteus software, the necessary assessments and adjustments could be made effectively, ensuring a smoother and more efficient implementation process.


•	Simulations results:

•	In the simulation, we utilized a Raspberry Pi and an MCP3208, which functions as an Analog-to-Digital Converter (ADC). This ADC was connected to a potentiometer, enabling the instant modification of voltage values. This setup played a crucial role in the crash detection process. By incorporating three potentiometers, we simulated the behavior of an ADXL335 accelerometer within the simulation software. This configuration allowed us to mimic the response of a physical accelerometer and analyze its performance in detecting crashes effectively.

![image](https://github.com/Jess-12/AI-based-system-for-accident-and-theft-detetction/assets/127778661/8a739193-ab7d-4777-92cb-caa6a3b9a2d6)

Simulation for Accident Detection

•	Hardware Implementation:

1)	ADXL 335
•	The ADXL335 is a low-cost, three-axis accelerometer sensor. It is designed to measure acceleration in three dimensions. The sensor outputs an analog voltage proportional to the acceleration along each of the X, Y, and Z axes.
•	The basic working principle of the ADXL335 is based on the deflection of the cantilever beams in response to acceleration. When the sensor is subjected to acceleration in a particular direction, the proof mass moves in that direction, causing the cantilever beams to deflect. The deflection of the beams changes the distance between the sensing electrodes, which changes the capacitance between them.
•	The change in capacitance is proportional to the acceleration.
•	The analog output signals from the sensor are amplified and filtered by the signal conditioning circuitry and then converted to digital signals using an analog-to-digital converter (ADC). The digital signals can then be processed by a microcontroller.

Working

![image](https://github.com/Jess-12/AI-based-system-for-accident-and-theft-detetction/assets/127778661/80ce8dae-c11b-4011-be81-8216527ba3f1)

Working of ADXL335

Mcp3208(ADC)

•	The MCP3208 is an 8-channel, 12-bit analog-to-digital converter (ADC). It is designed to convert analog signals into digital signals for use in digital devices, such as microcontrollers and computers.

![image](https://github.com/Jess-12/AI-based-system-for-accident-and-theft-detetction/assets/127778661/279fffc8-e7d7-45b4-a6ab-bc5245aa3072)
- Communication flow

2)	GPS module

•	The GPS module is a device that receives signals from multiple satellites to determine its precise location on Earth.
•		It consists of a GPS receiver, an antenna to capture satellite signals, and associated circuitry to process the received data.



GPS module and its parts
•	The module's UART (Universal Asynchronous Receiver-Transmitter) pins, such as TX (transmit) and RX (receive), are connected to the Raspberry Pi's UART pins, allowing data transmission between the raspberry pi and GPS module.
•	The transmitter of the raspberry pi is connected to receiver of GPS module and vice versa.
