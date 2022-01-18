// Evite les inclusions récursives (aucune idée de ce que c'est)
#ifndef IMU_H
#define IMU_H
 
#include "math.h"
 
#include "MeConfig.h"
#ifdef ME_PORT_DEFINED
#include "MePort.h"
#endif
 
// Trucs utiles
#define I2C_BUFFER_SIZE 14
#define I2C_ERROR       (-1)
 
#define MPU6050_RA_ACCEL_XOUT_H     0x3B // Adresse du 1er octet des infos a lire (accel puis temp puis gyro)
 
#define MPU6050_DEFAULT_ADDRESS    0x68 // Adresse i2c classique du MPU6050
#define MPU6050_RA_PWR_MGMT_1      0x6B // Pour le sortir de la veille
#define MPU6050_RA_CONFIG          0x6A // Pour config le filtre passe-bas (wola aucune idée de ce que c'est)
 
#define MPU6050_RA_GYRO_CONFIG        0x1B // Adresse pour config le gyro
#define MPU6050_GCONFIG_FS_SEL_BIT    4    // Position des bits à modifier pour config le gyro
#define MPU6050_GCONFIG_FS_SEL_LENGTH 2    // Longueur des bits à modifier pour config le gyro
 
// Gyro sensitivity
#define MPU6050_GYRO_FS_250         0x00
#define MPU6050_GYRO_FS_500         0x01
#define MPU6050_GYRO_FS_1000        0x02
#define MPU6050_GYRO_FS_2000        0x03
 
#define MPU6050_RA_ACCEL_CONFIG     0x1C // Adresse pour config l'accelerometre
#define MPU6050_ACONFIG_AFS_SEL_BIT         4 // Position des bits à modifier pour config l'accelerometre
#define MPU6050_ACONFIG_AFS_SEL_LENGTH      2 // Longueur des bits à modifier pour config l'accelerometre
 
// Accel sensitivity
#define MPU6050_ACCEL_FS_2          0x00
#define MPU6050_ACCEL_FS_4          0x01
#define MPU6050_ACCEL_FS_8          0x02
#define MPU6050_ACCEL_FS_16         0x03
 
// On va faire genre que je comprends ce qu'il se passe lol
 
/**
 * Class: Imu
 * \par Description
 * Declaration de la Class Imu
 */
#ifndef ME_PORT_DEFINED
class Imu
#else // !ME_PORT_DEFINED
class Imu : public MePort
#endif // !ME_PORT_DEFINED
{
 
private:
 
// Utiliser pour la connection i2c (je crois)
  volatile uint8_t  _AD0;
  volatile uint8_t  _INT;
 
  double angleX, angleY, angleZ, angleZSmooth;                 // Angles
 
  double accX, accY, accZ;                       // Accélérations linéaires
  double gravity;                                // Norme de la gravité
  uint16_t accelSensitivity;                      // Sensibilite de l'accelerometre
 
  double gyrX, gyrY, gyrZ;                       // Accelerations angulaires
  double gyrXOffset, gyrYOffset, gyrZOffset;     // Decalages des accelerations angulaires
  uint16_t gyroSensitivity, gyroSensitivitySI;   // Sensibilite ddu gyroscope 
  double imuDrift;                               // Drift de l'imu
  double gyroDrift;															 // Drift du gyro sur z
 
  uint8_t i2cData[I2C_BUFFER_SIZE];			// Tableau des donnees en octet
  uint8_t deviceAddress;
 
  // Fais les "zeros"
  void calibration(uint16_t calibrationIterations = 200);
 
 	double getGyroSensitivity(void);
 
	double setGyroSensitivity(uint8_t gyro_config);
 
	double getAccelSensitivity(void);
 
	double setAccelSensitivity(uint8_t accel_config);
 
	int8_t readData(uint8_t start, uint8_t *buffer, uint8_t size);
 
	int8_t writeBits(uint8_t regAddr, uint8_t bitStart, uint8_t length, uint8_t data);
 
	int8_t writeReg(int16_t reg, uint8_t data);
 
 	int8_t writeData(uint8_t start, const uint8_t *pData, uint8_t size);
 
public:
 
#ifdef ME_PORT_DEFINED
  Imu(void);
#else
  Imu(uint8_t AD0, uint8_t INT);
  Imu(uint8_t AD0, uint8_t INT, uint8_t address);
#endif
 
	void begin(void); 
	void update(void);
	double getAccX(void) const;
	double getAccY(void) const;
	double getAccZ(void) const;
	double getGyrX(void) const;
	double getGyrY(void) const;
	double getGyrZ(void) const;
	double getAngleX(void) const;
	double getAngleY(void) const;
	double getAngleZ(void) const;
	void getData(float* data) const;
};
 
#endif
