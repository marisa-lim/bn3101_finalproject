// Retrieved from:
// https://www.learnrobotics.org/blog/arduino-data-logger-csv/?utm_source=youtube&utm_medium=description&utm_campaign=arduino_CSV_data_logger

// Initiate sensor variables, each microphone attached to a different analog pin
int sensor1 = A0;

void setup()
{
  Serial.begin(9600);
  pinMode(sensor1, INPUT);
}

// Global variables
int data1; // store data from both sensors
int freq = 100; // data collection frequency ~x milliseconds
String dataLabel1 = "Microphone A";
bool label = true;

void loop()
{
    // print out column headers at top of CSV file
    while(label){ // runs once only!
        Serial.print("Mic A");
        label=false;
    }

    // Must convert analog to digital data (Retrieved from: https://www.teachmemicro.com/arduino-microphone/)
    long data1 = 0;
    for(int i=0; i<100; i++)
    {
        data1 += analogRead(sensor1);
    }
    data1 = data1/100;

    // Display Data to Serial Monitor in [data1, data2] format
    Serial.println(data1);

    delay(freq);
}
