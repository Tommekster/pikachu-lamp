#include <PCM.h>
#include "pika.h"
#include "pi.h"
#include "chu.h"
#include "sparking.h"

//const int repro_pin = 11;
const int button_pin = 4;

void setup()
{
  pinMode(button_pin, INPUT);
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

void pika() { playOnce(PIKA_WAV, sizeof(PIKA_WAV)); }
void pi() { playOnce(PI_WAV, sizeof(PI_WAV)); }
void chu() { playOnce(CHU_WAV, sizeof(CHU_WAV)); }
void spark() { playOnce(SPARKING_WAV, sizeof(SPARKING_WAV)); }

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
