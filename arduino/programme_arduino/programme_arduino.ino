/*
 * TODO :
 * 
 * - potentiellement renommer les topics ayant 'chatter' dans leur nom
 * - tenter de changer le baud pour etre plus opti
 * - mettre tout en camelCase
 * 
 */


#include "MeMegaPi.h"
#include <Wire.h>
#include <ros.h>
#include <imu.h>
#include <std_msgs/String.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/Float32.h>
#include <MeUltrasonicSensor.h>
#include <test/IMU.h>
#include <test/PseudoLidar.h>
#include <test/Encoders.h>
#include <test/Moteurs.h>
#include <OneButton.h>

/*
 * ROS
 */

// Declaration du node de l'Arduino
ros::NodeHandle nh;


/*
 * Temps
 */

std_msgs::Float32 time;

float last_time = millis();

ros::Publisher pub_time("pub_temps", &time);


std_msgs::String ok;
ros::Publisher pub_ok("pub_ok", &ok);

/*
 * Moteurs des roues
 */

// Declaration des moteurs gauche et droit
MeMegaPiDCMotor motorDroit(PORT1B);
MeMegaPiDCMotor motorGauche(PORT2B);

// Declaration des encodeurs sur les moteurs gauche et droit
MeEncoderOnBoard encoderDroit(SLOT1);
MeEncoderOnBoard encoderGauche(SLOT2);

// Declaration du capteur ultrason
MeUltrasonicSensor ultraSensor(PORT_6);

// Vitesses des moteurs
int motorSpeedDroit = 0;
int motorSpeedGauche = 0;

// Message transmsis contenant les informations des encodeurs
test::Encoders encodersData;

// Definit la vitesse des moteurs des roues
// en fonction du message recu sur le topic pub_move
void setMotorSpeedMove(const test::Moteurs& moteursMsg) {
  motorSpeedDroit = moteursMsg.moteur_droit;
  motorSpeedGauche = moteursMsg.moteur_gauche;
}
// Declaration du subscriber au topic pub_move pour recuperer les vitesses des moteurs
ros::Subscriber<test::Moteurs> sub_move("pub_move", &setMotorSpeedMove);

void setFin(const std_msgs::String& fin) {
  digitalWrite(2, LOW);
}

void led_clign(const std_msgs::String& msg) {
  
  for(int i = 0; i < 3; i++){
    digitalWrite(2, LOW);
    delay(300);
    digitalWrite(2, HIGH);
    delay(300);
    time.data = 0.5;
    pub_time.publish(&time);
  }

  pub_ok.publish(&ok);
}

// ecoute de la demande de signal
ros::Subscriber<std_msgs::String> sub_signal("pub_signal", &led_clign);

// Declaration du subscriber au topic pub_fin pour indiquer quand le programme est fini
ros::Subscriber<std_msgs::String> sub_fin("pub_fin", &setFin);

// Declaration du publisher sur le topic pub_encoders pour publier les donnees des encodeurs
ros::Publisher pub_encoders("pub_encoders", &encodersData);

// Utilise par l'encodeur (droit) 
void isrProcessEncoderDroit(void) {
  
  if(digitalRead(encoderDroit.getPortB()) == 0) {
    encoderDroit.pulsePosMinus();
  } else {
    encoderDroit.pulsePosPlus();
  }
}

// Utilise par l'encodeur (gauche)
void isrProcessEncoderGauche(void) {
  
  if(digitalRead(encoderGauche.getPortB()) == 0) {
    encoderGauche.pulsePosMinus();
  } else {
    encoderGauche.pulsePosPlus();
  }
}


/*
 * IMU
 */

// Declaration de l'imu
Imu imu;


// Message transmsis contenant les donnees mesurees par l'imu
test::IMU imuData;

// Declaration du publisher sur le topic pub_imu pour publier les donnees mesurees par l'imu
ros::Publisher imuPublisher("pub_imu", &imuData);


/*
 * Distance
 */

std_msgs::Float32 distance;

float last_distance = 0;

ros::Publisher pub_distance("pub_distance", &distance);

/*
 * initialisation bouton
 */
bool boolaru = 0;
bool boolpres = 0;
bool boolready = 1;

#define BUTTON_PIN_ARU 5
#define BUTTON_PIN_RUN A1

static void aruClick() {
  if(boolaru == 1){
    digitalWrite(4, LOW);
    boolpres = 1;
  } else {
    boolaru = 1;
    boolpres = 0;
    digitalWrite(4, HIGH);
    digitalWrite(2, LOW);
  }
}

OneButton aru = OneButton(
  BUTTON_PIN_ARU,  // Input pin for the button
  false,       // Button is active Low
  false        // Disable internal pull-up resistor
);

static void runClick() {
  if(boolaru == 0 and boolready == 1){
    pub_ok.publish(&ok);
    boolready = 0;
    digitalWrite(2, HIGH);
  }
  if (boolpres == 1){
    boolaru = 0;
    boolpres = 0;
    digitalWrite(2, HIGH);
  }
}

OneButton run = OneButton(
  BUTTON_PIN_RUN,  // Input pin for the button
  false,       // Button is active Low
  false        // Disable internal pull-up resistor
);


void setup() {
  Serial.begin(57600);

  /*
   * ROS
   */

  nh.getHardware()-> setBaud(57600);
  // Initialisation du node de l'Arduino
  nh.initNode();

  /*
   * ecoute du publisher du signal
   */
  
  nh.subscribe(sub_signal);

  /*
   * Moteurs des roues
   */
  
  // Abonnement au subscriber de la vitesse des moteurs des roues
  nh.subscribe(sub_move);

  // Advertisement ud publisher des donnees des encodeurs
  nh.advertise(pub_encoders);

  // Utilise par les encodeurs
  attachInterrupt(encoderDroit.getIntNum(), isrProcessEncoderDroit, RISING);
  attachInterrupt(encoderGauche.getIntNum(), isrProcessEncoderGauche, RISING);

  pinMode(4, OUTPUT);
  pinMode(2, OUTPUT);

  /*
   * IMU
   */
  
  // Advertisement du publisher des donnes de l'imu
  nh.advertise(imuPublisher);

  // Initialisation de l'imu (fait les zeros, etc)
  imu.begin();

  /*
   * Temps
   */
  nh.advertise(pub_time);
  nh.advertise(pub_distance);

  /*
   * ecoute de la fin
   */
  nh.subscribe(sub_fin);

  /*
   * setup digital_ports
   */

aru.attachClick(aruClick);
run.attachClick(runClick);

nh.advertise(pub_ok);
ok.data = "ok";
}
 
void loop() {
 /*
  * bouton
  */
  aru.tick();
  run.tick();

  /*
   * suite de la loop
   */
  nh.spinOnce();
  
  // Mesure du temps d'execution de la loop
  time.data = millis() - last_time;
  last_time = millis();

  // Publication du temps d'execution
  pub_time.publish(&time);

  
  distance.data = ultraSensor.distanceCm();
  pub_distance.publish(&distance);
  
    if(boolaru == 0){
      // Modification de la vitesse du moteur de la roue droite
      if(motorSpeedDroit == 0) {
        motorDroit.stop();
      } else {
        motorDroit.run(-motorSpeedDroit);
      }
    
      // Modification de la vitesse du moteur de la roue gauche
      if(motorSpeedGauche == 0) {
        motorGauche.stop();
      } else {
        motorGauche.run(motorSpeedGauche);
      }
    } else {
      motorDroit.stop();
      motorGauche.stop();
    }
  
  // Mise a jour des valeurs des encodeurs des roues gauche et droite
  encoderDroit.loop();
  encoderGauche.loop();

  encodersData.angular_pose_droit = encoderDroit.getCurPos();
  encodersData.angular_pose_gauche = encoderGauche.getCurPos();
  
  pub_encoders.publish(&encodersData);

  nh.spinOnce();
  
  // Mise a jour de l'imu
  imu.update();
  
  // Recuperation des donnees mesurees par l'imu
  imuData.angle_x = imu.getAngleX();
  imuData.angle_y = imu.getAngleY();
  imuData.angle_z = imu.getAngleZ();
  imuData.gyr_x = imu.getGyrX();
  imuData.gyr_y = imu.getGyrY();
  imuData.gyr_z = imu.getGyrZ();
  imuData.acc_x = imu.getAccX();
  imuData.acc_y = imu.getAccY();
  imuData.acc_z = imu.getAccZ();

  imuPublisher.publish(&imuData);
  nh.spinOnce();
}
