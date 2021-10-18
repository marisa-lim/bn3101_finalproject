// Retrieved from:
// https://www.learnrobotics.org/blog/arduino-data-logger-csv/?utm_source=youtube&utm_medium=description&utm_campaign=arduino_CSV_data_logger

// Initiate sensor variables, each microphone attached to a different analog pin
int sensor1 = A0;
int sensor2 = A1;

void setup()
{
  Serial.begin(9600);
  pinMode(sensor1, INPUT);
  pinMode(sensor2, INPUT);
}

// Global variables
int data1, int data 2; // store data from both sensors
int freq = 1000; // data collection frequency ~x milliseconds
String dataLabel1 = "Microphone A";
String dataLabel2 = "Microphone B";
bool label = true;

void loop()
{
    // print out column headers at top of CSV file
    while(label){ // runs once only!
        Serial.print(dataLabel1);
        Serial.print(",");
        Serial.println(dataLabel2);
        label=false;
    }

    // Must convert analog to digital data (Retrieved from: https://www.teachmemicro.com/arduino-microphone/)
    long data1 = 0;
    long data2 = 0;
    for(int i=0; i<100; i++)
    {
        data1 += analogRead(sensor1);
        data2 += analogRead(sensor2);
    }
    data1 = data1/100;
    data2 = data2/100;

    // Display Data to Serial Monitor in [data1, data2] format
    Serial.print(data1);
    Serial.print(",");
    Serial.println(data2);

    delay(freq);
}
