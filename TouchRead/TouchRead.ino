// ESP32 Touch Sensor

//Touch Sensors possibles --> T0(4), T2(2), T3(15), T4(13), T5(12), T6(14), T7(27), T8(33), T9(32)

void setup() {
  Serial.begin(115200);
  delay(1000); // give me time to bring up serial monitor
  Serial.println("ESP32 Touch Test");
  Serial.println("Mitja touch sensor (100 mostres) cada 3 segons");
}

void loop() {
  if(Serial.available()){
    float mean = 0;
    for (int i = 0; i < 100; i++) {
      mean += touchRead(T0);
      delay(5);
    }
    mean = mean / 100;
    Serial.write(mean);
    delay(2000);
  }
}
