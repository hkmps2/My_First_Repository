class LED {
  public:
    unsigned long last_time = 0;
    int brightness = 0;
    bool increasing = true;
    int breathing_delayY = 10;
    int maxbright = 225;
    int minbright = 0;
    int fadeamount = 10;
    int delaytime = 50;
    int pin;
    bool breathing = false;

    LED(int led_pin) {
      pin = led_pin;
      pinMode(pin, OUTPUT);
    }

    void lightbright() {
      if (breathing) {
        if (millis() - last_time > delaytime) {

          if (increasing) {
            brightness = brightness + fadeamount;
          }
          else {
            brightness = brightness - fadeamount;
          }
          if (brightness > maxbright) {
            increasing = false;
            analogWrite(pin, maxbright);
          } else if (brightness < minbright) {
            increasing = true;
            analogWrite(pin, minbright);
          } else {
            analogWrite(pin, brightness);
          }
          last_time = millis();
        }
      } else {
        analogWrite(pin, 0);
      }
    }

};

//
LED light_R(3);
LED light_Y(5);
LED light_B(6);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  String bb = "";
  String cc = "";
  String ww = "";
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0) {
    char s1 = Serial.read();
    char x1;
    char c1;
    char p1;
    char p2;
    char p3;
    char e1;
    Serial.println(s1);
    Serial.println("1");
    if (s1 == 's') {
      delay(1);
      Serial.println("2");
      x1 = Serial.read();
      if (x1 == 'd') {
        delay(20);
        c1 = Serial.read();
        p1 = Serial.read();
        p2 = Serial.read();
        p3 = Serial.read();
        e1 = Serial.read();
        Serial.println("3");

        if (e1 == 'e') {                          //先判斷字尾是否為e再判斷顏色和讀取延遲時間!!(精簡化)
          bb = bb + p1;
          bb = bb + p2;
          bb = bb + p3;
          int new_delay_time = bb.toInt();
          Serial.println("4");
          if (c1 == 'r') {
            light_R.delaytime = new_delay_time;
            Serial.println("red");
//            light_R.breathing = true;
          }
          if (c1 == 'y') {
            light_Y.delaytime = new_delay_time;
            Serial.println("yellow");
//            light_Y.breathing = true;
          }
          if (c1 == 'b') {
            light_B.delaytime = new_delay_time;
            Serial.println("blue");
//            light_B.breathing = true;
          }
        }
      }
      else if (x1 == 'c') {
        delay(10);
        Serial.println("5");
        c1 = Serial.read();
        p1 = Serial.read();
        e1 = Serial.read();
        if (e1 == 'e') {                          //先判斷字尾是否為e再判斷顏色和讀取延遲時間!!(精簡化)
          Serial.println("6");
          if (c1 == 'r') {
            if (p1 == '1') {
              light_R.breathing = true;
            }
            else if (p1 == '0') {
              light_R.breathing = false;
              Serial.println("red_off");
            }
          }
          if (c1 == 'y') {
            if (p1 == '1') {
              light_Y.breathing = true;
            }
            else if (p1 == '0') {
              light_Y.breathing = false;
              Serial.println("yellow_off");
            }
          }
          if (c1 == 'b') {
            if (p1 == '1') {
              light_B.breathing = true;
            }
            else if (p1 == '0') {
              light_B.breathing = false;
              Serial.println("blue_off");
            }
          }
        }
      }
    }
  }
  light_R.lightbright();             //不能該在判斷式內，應不斷執行(在Serial.available>0裡面一開始就不會亮)
  light_Y.lightbright();
  light_B.lightbright();
}
