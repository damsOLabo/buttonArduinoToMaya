
const int buttonPin = 4;

int buttonState = 0;

void setup()
{
    Serial.begin(9600);
    pinMode(buttonPin, INPUT);
}

void loop()
{
    buttonState = digitalRead(buttonPin);
    Serial.println(buttonState);
    delay(100); // Delay a little bit to improve simulation performance
}