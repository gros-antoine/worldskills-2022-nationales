/*
 * TODO :
 *  
 * - Tester writeBits sur la config des sensibilites
 * - Commenter (norme pour la doc ?)
 * 
 */
 
#include "imu.h"
 
#ifdef ME_PORT_DEFINED
 
Imu::Imu(void) : MePort(0)
{
  deviceAddress = MPU6050_DEFAULT_ADDRESS;
}
 
#else
 
Imu::Imu(uint8_t AD0, uint8_t INT)
{
  deviceAddress = MPU6050_DEFAULT_ADDRESS;
  _AD0 = AD0;
  _INT = INT;
}
 
Imu::Imu(uint8_t AD0, uint8_t INT, uint8_t address)
{
  deviceAddress = address;
  _AD0 = AD0;
  _INT = INT;
}
#endif
 
void Imu::begin(void) {
 
  angleX = 0;
  angleY = 0;
  angleZ = 0;
 
  accX = 0;
  accY = 0;
  accZ = 0;
  gravity = 0;
 
  gyrX = 0;
  gyrY = 0;
  gyrZ = 0;
  gyrXOffset = 0;
  gyrYOffset = 0;
  gyrZOffset = 0;
 
  gyroSensitivity = setGyroSensitivity(MPU6050_GYRO_FS_500);
  accelSensitivity = setAccelSensitivity(MPU6050_ACCEL_FS_2);
 
  Wire.begin();
 
  delay(200);
 
  writeReg(MPU6050_RA_PWR_MGMT_1, 0x00); // sortir de la veille
 
  delay(100);
 
  writeReg(MPU6050_RA_CONFIG, 0x01); // Configure le filtre passe-bas
  //writeBits(MPU6050_RA_GYRO_CONFIG, MPU6050_GCONFIG_FS_SEL_BIT, MPU6050_GCONFIG_FS_SEL_LENGTH, MPU6050_GYRO_FS_500); // Configure la sensibilite du gyro
  //writeBits(MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_AFS_SEL_BIT, MPU6050_ACONFIG_AFS_SEL_LENGTH, MPU6050_ACCEL_FS_2); // Configure la sensibilite de l'accel
 
  writeReg(0x1a, 0x01);//configurate the digital low pass filter
  writeReg(0x1b, 0x08);//set the gyro scale to 500 deg/s
 
  delay(100);
 
  calibration(200);
}
 
void Imu::update(void) {
 
  static unsigned long last_time = micros();
  double dt, filter_coefficient;
	int8_t returnValue;
 
	long temp = 0;
 
	double angleXAcc = 0, angleYAcc = 0, buffer = 0;
 
	returnValue = readData(0x3b, i2cData, 14);
 
	if(returnValue != 0) {
    return;
  }
 
	dt = (double)(micros() - last_time) * 0.000001; // Pour passer dt en s
	last_time = micros();
 
	accX = ( (i2cData[0] << 8) | i2cData[1] );
	accY = ( (i2cData[2] << 8) | i2cData[3] );
	accZ = ( (i2cData[4] << 8) | i2cData[5] );
	gyrX = ( (i2cData[8] << 8) | i2cData[9] );
	gyrY = ( (i2cData[10] << 8) | i2cData[11] );
	gyrZ = ( (i2cData[12] << 8) | i2cData[13] );
 
	// On fait les 0
	gyrX -= gyrXOffset;
	gyrY -= gyrYOffset;
	gyrZ -= gyrZOffset;
 
	// Passage en rad/s
	gyrX /= gyroSensitivitySI;
	gyrY /= gyroSensitivitySI;
	gyrZ /= gyroSensitivitySI;
 
	// Différence de repère entre le repère de l'imu et celui du robot (pas sur des deux lignes qui suivent)
	// X_imu = - Y_robot
	// Y_imu = X_robot
	// Besoin d'ajustement
 
	// Transforme les vitesses angulaires dans le repere robot
	buffer = gyrY;
	gyrY = -gyrX;
	gyrX = buffer;
 
	// Transforme les accelerations lineaires dans le repere robot
	buffer = accY;
	accY = accX;
	accX = -buffer;
	accZ = -accZ; // Car l'accelerometre lie la gravite positive
	// Maintenant les accel lineaires sont dans le repere du robot
  
  // Compensation du drift
	//angleZ += gyrZ * dt; // Integration pour avoir l'angle Z
	//angleZ -= imuDrift * dt;
 
  if(abs(gyrZ) > 0.004) {
 
    angleZSmooth += gyrZ * dt;
    
     //Filtrage par passe-bas de l'angle
    double filtre = 0.5;
    angleZ = filtre * angleZSmooth + (1 - filtre) * angleZ;
    angleZ = angleZSmooth;
  }
 
	/*angleZ = angleZ - (2 * M_PI) * floor(angleZ / (2 * M_PI)); // Equivalent a modulo 2*pi, utile car sinon l'angle depasse 2*pi et -2*pi
 
	// Passe angleZ entre -pi et pi
	if(angleZ > M_PI) {
		angleZ -= 2 * M_PI;
	}*/
 
	// Intégrations pour avoir les angles X et Y
	angleX = angleX + gyrX * dt;
	angleY = angleY + gyrY * dt;
 
	// Angles deduits du vecteur acceleration donc la gravite en fait
	angleXAcc = -asin(accY / sqrt(accX*accX + accY*accY + accZ*accZ));
  angleYAcc = asin(accX / sqrt(accX*accX + accY*accY + accZ*accZ));  
 
	// Evite la divergence de l'integration des angles X et Y
	filter_coefficient = 0.5 / (0.5 + dt);
  angleX = angleX * filter_coefficient + angleXAcc * (1 - filter_coefficient);
  angleY = angleY * filter_coefficient + angleYAcc * (1 - filter_coefficient);
 
 	// Passage en g
	accX /= accelSensitivity;
  accY /= accelSensitivity;
  accZ /= accelSensitivity;
}
 
// Retourne l'acceleration lineaire sur l'axe X du robot, en g
double Imu::getAccX(void) const {
  return accX;
}
 
// Retourne l'acceleration lineaire sur l'axe Y du robot, en g
double Imu::getAccY(void) const {
  return accY;
}
 
// Retourne l'acceleration linaire sur l'axe Z du robot, en g
double Imu::getAccZ(void) const {
  return accZ;
}
 
// Retourne l'acceleration angulaire sur l'axe X du robot, en rad/s
double Imu::getGyrX(void) const {
  return gyrX;
}
 
// Retourne l'acceleration angulaire sur l'axe Y du robot, en rad/s
double Imu::getGyrY(void) const {
  return gyrY;
}
 
// Retourne l'acceleration angulaire sur l'axe Z du robot, en rad/s
double Imu::getGyrZ(void) const {
  return gyrZ;
}
 
// Retourne la rotation du robot autour de l'axe X en rad sur [-pi/2; pi/2]
double Imu::getAngleX(void) const {
  return angleX;
}
 
// Retourne la rotation du robot autour de l'axe Y en rad sur [-pi/2; pi/2]
double Imu::getAngleY(void) const {
  return angleY;
}
 
// Retourne la rotation du robot autour de l'axe Z en rad sur [-pi; pi]
double Imu::getAngleZ(void) const {
  return angleZ;
}
 
double Imu::getGyroSensitivity(void) {
  return gyroSensitivity;
}
 
void Imu::getData(float* data) const {
 
	data[0] = angleX;
	data[1] = angleY;
	data[2] = angleZ;
	data[3] = gyrX;
	data[4] = gyrY;
	data[5] = gyrZ;
	data[6] = accX;
	data[7] = accY;
	data[8] = accZ;
}
 
double Imu::setGyroSensitivity(uint8_t gyro_config) {
 
  switch (gyro_config) {
 
    case MPU6050_GYRO_FS_250:
      gyroSensitivity = 131.0;
      break;
 
    case MPU6050_GYRO_FS_500:
      gyroSensitivity = 65.5;
      break;
 
    case MPU6050_GYRO_FS_1000:
      gyroSensitivity = 32.8;
      break;
 
    case MPU6050_GYRO_FS_2000:
      gyroSensitivity = 16.4;
      break;
 
    default:
      gyroSensitivity = 65.5;
      break;
  }
 
	gyroSensitivitySI = gyroSensitivity * 180 / M_PI;
 
  return gyroSensitivity;
}
 
double Imu::getAccelSensitivity(void) {
  return accelSensitivity;
}
 
double Imu::setAccelSensitivity(uint8_t accel_config) {
 
  switch (accel_config) {
 
    case MPU6050_ACCEL_FS_2:
      accelSensitivity = 16384.0;
      break;
 
    case MPU6050_ACCEL_FS_4:
      accelSensitivity = 8192.0;
      break;
 
    case MPU6050_ACCEL_FS_8:
      accelSensitivity = 4096.0;
      break;
 
    case MPU6050_ACCEL_FS_16:
      accelSensitivity = 2048.0;
      break;
 
    default:
      accelSensitivity = 16384.0;
      break;
  }
 
  return accelSensitivity;
}
 
void Imu::calibration(uint16_t calibrationIterations) {
 
	// Ici on enleve l'erreur initale presente sur le gyro
 
	// En testant, on s'est rendu compte que la norme du vecteur gravite (sense etre égale a 1)
	// ne vaut pas 1, donc on calcule la norme du vecteur gravite pour pouvoir l'enlever
	// correctement lors des mesures plus tard
 
	int8_t returnValue;
	long accXTemp = 0, accYTemp = 0, accZTemp = 0, gravitySum = 0;
	long gyroXSum = 0, gyroYSum = 0, gyroZSum = 0;
 
	for(size_t i = 0; i < calibrationIterations; i++) {
 
		returnValue = readData(MPU6050_RA_ACCEL_XOUT_H, i2cData, I2C_BUFFER_SIZE);
 
		accXTemp = ( (i2cData[0] << 8) | i2cData[1] );
		accYTemp = ( (i2cData[2] << 8) | i2cData[3] );
		accZTemp = ( (i2cData[4] << 8) | i2cData[5] );
 
		gravitySum += sqrt(accXTemp*accXTemp + accYTemp*accYTemp + accZTemp*accZTemp);
 
		gyroXSum += ( (i2cData[8] << 8) | i2cData[9] );
		gyroYSum += ( (i2cData[10] << 8) | i2cData[11] );
		gyroZSum += ( (i2cData[12] << 8) | i2cData[13] );
 
		delay(3);
	}
 
  gravity = gravitySum / calibrationIterations;
 
  gyrXOffset = gyroXSum / calibrationIterations;
  gyrYOffset = gyroYSum / calibrationIterations;
  gyrZOffset = gyroZSum / calibrationIterations;
 
 

  // Calibration de l'angle z de l'imu par compensation du drift 1

  unsigned long debut = micros() * 0.000001;
  int delai = 14;
  int nbrRepet = 10000 / delai;
  long gyroZCalib = 0;
  double angleZCalib = 0;
  long last_time = micros();
  double dt;
 
  delay(delai);
 
  for(size_t i = 0; i < nbrRepet; i++) {
 
    dt = (double)(micros() - last_time) * 0.000001; // Pour passer dt en s
    last_time = micros();
 
    returnValue = readData(MPU6050_RA_ACCEL_XOUT_H, i2cData, I2C_BUFFER_SIZE);
    gyroZCalib = ( (i2cData[12] << 8) | i2cData[13] );
 
    gyroZCalib /= gyroSensitivitySI;
    gyroZCalib -= gyrZOffset;
 
    angleZCalib += gyroZCalib * dt;
 
    delay(delai);
 
  }
 
  imuDrift = angleZCalib / (micros() * 0.000001 - debut);
 
	// Calibration de l'angle z de l'imu par compensation du drift 2
 
	/*returnValue = readData(MPU6050_RA_ACCEL_XOUT_H, i2cData, I2C_BUFFER_SIZE);
  gyroZInit = ( (i2cData[12] << 8) | i2cData[13] );
 
  delay(delai);
 
  returnValue = readData(MPU6050_RA_ACCEL_XOUT_H, i2cData, I2C_BUFFER_SIZE);
  imuDrift = (((i2cData[12] << 8) | i2cData[13]) - gyroZInit) / gyroSensitivitySI / delai;*/
}
 
 
/**
 * \par Function
 *   readData
 * \par Description
 *   Write the data to i2c device.
 * \param[in]
 *   start - the address which will write the data to.
 * \param[in]
 *   pData - the head address of data array.
 * \param[in]
 *   size - set the number of data will be written to the devide.
 * \par Output
 *   None
 * \return
 *   Return the error code.
 *   the definition of the value of variable return_value:
 *   0:success
 *   1:BUFFER_LENGTH is shorter than size
 *   2:address send, nack received
 *   3:data send, nack received
 *   4:other twi error
 *   refer to the arduino official library twi.c
 * \par Others
 *   Calling the official i2c library to read data.
 */
int8_t Imu::readData(uint8_t start, uint8_t *buffer, uint8_t size) {
 
  int16_t i = 0;
  int8_t return_value = 0;
 
  Wire.beginTransmission(deviceAddress);
  return_value = Wire.write(start);
 
  if(return_value != 1) {
    return(I2C_ERROR);
  }
 
  return_value = Wire.endTransmission(false);
 
  if(return_value != 0) {
    return(return_value);
  }
 
  delayMicroseconds(1);
 
  /* Third parameter is true: relase I2C-bus after data is read. */
 
  Wire.requestFrom(deviceAddress, size, (uint8_t)true);
  while(Wire.available() && i < size) {
    buffer[i++] = Wire.read();
  }
 
  delayMicroseconds(1);
 
  if(i != size) {
    return(I2C_ERROR);
  }
 
  return(0); //return: no error 
}
 
/** Write multiple bits in an 8-bit device register.
 * @param regAddr Register regAddr to write to
 * @param bitStart First bit position to write (0-7)
 * @param length Number of bits to write (not more than 8)
 * @param data Right-aligned value to write
 * @return Status of operation
 */
int8_t Imu::writeBits(uint8_t regAddr, uint8_t bitStart, uint8_t length, uint8_t data) {
    //      010 value to write
    // 76543210 bit numbers
    //    xxx   args: bitStart=4, length=3
    // 00011100 mask byte
    // 10101111 original value (sample)
    // 10100011 original & ~mask
    // 10101011 masked | value
    uint8_t b;
    if (readData(regAddr, &b, 1) == 0) {
        uint8_t mask = ((1 << length) - 1) << (bitStart - length + 1);
        data <<= (bitStart - length + 1); // shift data into correct position
        data &= mask; // zero all non-important bits in data
        b &= ~(mask); // zero all important bits in existing byte
        b |= data; // combine data with existing byte
        return writeData(regAddr, &b, 1);
    } else {
        return 4;
    }
}
 
// Ecrit un octet reg à l'adresse data
int8_t Imu::writeReg(int16_t reg, uint8_t data) {
  int8_t return_value = 0;
  return_value = writeData(reg, &data, 1);
  return(return_value);
}
 
// Ecrit des octets pData de nombres size a l'adresse start
int8_t Imu::writeData(uint8_t start, const uint8_t *pData, uint8_t size) {
  int8_t return_value = 0;
  Wire.beginTransmission(deviceAddress);
  return_value = Wire.write(start); 
  if(return_value != 1)
  {
    return(I2C_ERROR);
  }
  Wire.write(pData, size);  
  return_value = Wire.endTransmission(true); 
  return(return_value); //return: no error                     
}
