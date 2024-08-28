#include <PCM.h>
#include "pika.h"
#include "pi.h"
#include "chu.h"
#include "sparking.h"

//const int repro_pin = 11;
const int button_pin = 4;
const int spark1_pin = 5;
const int spark2_pin = 6;
const int spark3_pin = 7;
const int orange_pin = 8;

void lampOn();

void setup()
{
  pinMode(button_pin, INPUT);
  pinMode(spark1_pin, OUTPUT);
  pinMode(spark2_pin, OUTPUT);
  pinMode(spark3_pin, OUTPUT);
  pinMode(orange_pin, OUTPUT);
  lampOn();
}

void pikachu_speech();

void loop()
{
  auto button_state = digitalRead(button_pin);
  if (button_state == HIGH)
  {
    pikachu_speech();
  }
}

void pika_pi();
void pika_chu();
void sparking();

void pikachu_speech()
{
  pika_pi();
  delay(1265-801);
  pika_chu();
  delay(3378-2067);
  sparking();
}

void playOnce(unsigned char const *data, int length)
{
  startPlayback(data, length);
  delay(length/8);
  stopPlayback();
}

void lampOn() { digitalWrite(orange_pin, LOW); }
void lampOff() { digitalWrite(orange_pin, HIGH); }

void pika()
{
  auto len = sizeof(PIKA_WAV);
  startPlayback(PIKA_WAV, len);

  auto startTime = millis();
  for(auto t = 0; t < len/8; t = millis() - startTime) {
    auto speaking = (34 < t && t < 106) || (214 < t && t < 311);
    if(speaking) {
      lampOff(); 
    } else {
      lampOn();
    }
    delay(5);
  }
  stopPlayback();
  lampOn();
}

void pi()
{
  lampOff();
  playOnce(PI_WAV, sizeof(PI_WAV));
  lampOn();
}

void chu()
{
  lampOff();   
  playOnce(CHU_WAV, sizeof(CHU_WAV)); 
  lampOn();
}

void spark()
{
  auto len = sizeof(SPARKING_WAV);
  startPlayback(SPARKING_WAV, len);
  lampOff();

  auto startTime = millis();
  for(auto t = 0; t < len/8; t = millis() - startTime) {
    auto color = (t / 100) % 3;
    digitalWrite(spark1_pin, color == 0 ? HIGH : LOW);
    digitalWrite(spark2_pin, color == 1 ? HIGH : LOW);
    digitalWrite(spark3_pin, color == 2 ? HIGH : LOW);
    delay(5);
  }
  
  
  
  stopPlayback();
  digitalWrite(spark1_pin, LOW);
  digitalWrite(spark2_pin, LOW);
  digitalWrite(spark3_pin, LOW);
  lampOn();
}

void pika_pi()
{
  pika();
  delay(522-360);
  pi();
}

void pika_chu()
{
  pika();
  delay(1800-1625);
  chu();
}

void sparking()
{
  pika();
  delay(3869-3773);
  for(int i = 0; i < 8; i++) spark();
  delay(7860-6861);
  //startPlayback(SPARKING, sizeof(SPARKING));
  //delay(4000);
  chu();
}
