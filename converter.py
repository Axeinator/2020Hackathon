import os


def toCPP(times):

    with open("./led/led.ino", "w") as f:
        f.write("int led1 = 8; \n")
        f.write("int led2 = 9; \n")
        f.write("int led3 = 10; \n")
        f.write("int led4 = 11; \n")
        f.write("int led5 = 12; \n")
        f.write("int led6 = 13; \n")

        f.write("void setup() { \n")
        for i in range(6):
            f.write(f"pinMode(led{i+1}, OUTPUT); \n")
        f.write(("} \n"))

        f.write("void loop() { \n")

        for i in range(3):
            led = 1
            for time in times[i]:
                if time is True:
                    f.write(f"digitalWrite(led{led}, HIGH); \n")
                elif time is False:
                    f.write(f"digitalWrite(led{led}, LOW); \n")
                led += 1
            f.write("delay(2000); \n \n")

        f.write("}")

    os.system("./arduinoUpload.sh")






