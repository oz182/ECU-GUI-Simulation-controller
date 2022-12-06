const int ledPin = 13;
const int CranckSimPin = 12;

int incomingByte;

unsigned long Start_time;
unsigned long Current_time;

int TeethCounter;
int CranckFreq;
int RPM_MicroSec;

const byte numChars = 32;
char receivedChars[numChars];   // an array to store the received data

boolean newData = false;


void setup() {

  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
  pinMode(CranckSimPin, OUTPUT);

  Start_time = micros();
  TeethCounter = 0;
  CranckFreq = 0;

}




void loop() {

    if (Serial.available() > 0)
  {
    incomingByte = Serial.readString().toInt();
  }

  //recvWithEndMarker();

  RpmController();

  PinControl();

  //showNewData();




  //Serial.println(int(incomingByte)); // Making the loop 10 times slower

}




void recvWithEndMarker() {
    static byte ndx = 0;
    char endMarker = '\n';
    char rc;
    
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (rc != endMarker) {
            receivedChars[ndx] = rc;
            ndx++;
            if (ndx >= numChars) {
                ndx = numChars - 1;
            }
        }
        else {
            receivedChars[ndx] = '\0'; // terminate the string
            ndx = 0;
            newData = true;
        }
    }
}



void showNewData() {
    if (newData == true) {
        Serial.print("This just in ... ");
        Serial.println(receivedChars);
        newData = false;
    }
}



void RpmController()
{

  RPM_MicroSec = 1000/(((int(incomingByte)/60)*120)/1000);

  Current_time = micros();
  if (Current_time - Start_time >= incomingByte) //416 is 1200 RPM
  {
    if (TeethCounter < 58)
    {
      digitalWrite(CranckSimPin, !digitalRead(CranckSimPin));
      Start_time = Current_time;
      if (digitalRead(CranckSimPin) == 1)
      {
        TeethCounter += 1;
      }

    }else
    {
      Start_time = Current_time;
      digitalWrite(CranckSimPin, 0);
      TeethCounter += 1;
      if (TeethCounter == 63)
      {
        TeethCounter = 0;
      }
    }
  }
}


void PinControl()
{
    if (incomingByte == 'H') 
  {
  digitalWrite(ledPin, HIGH);
  Serial.println("Getting H");
  Serial.flush();
  }

  if (incomingByte == 'L')
  {
  digitalWrite(ledPin, LOW);
  Serial.println("Getting L");
  Serial.flush();
  }
}


void DummyFunc()
{
  int dum = Current_time - Start_time/60;
}
