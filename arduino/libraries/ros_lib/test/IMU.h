#ifndef _ROS_test_IMU_h
#define _ROS_test_IMU_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace test
{

  class IMU : public ros::Msg
  {
    public:
      typedef float _angle_x_type;
      _angle_x_type angle_x;
      typedef float _angle_y_type;
      _angle_y_type angle_y;
      typedef float _angle_z_type;
      _angle_z_type angle_z;
      typedef float _gyr_x_type;
      _gyr_x_type gyr_x;
      typedef float _gyr_y_type;
      _gyr_y_type gyr_y;
      typedef float _gyr_z_type;
      _gyr_z_type gyr_z;
      typedef float _acc_x_type;
      _acc_x_type acc_x;
      typedef float _acc_y_type;
      _acc_y_type acc_y;
      typedef float _acc_z_type;
      _acc_z_type acc_z;

    IMU():
      angle_x(0),
      angle_y(0),
      angle_z(0),
      gyr_x(0),
      gyr_y(0),
      gyr_z(0),
      acc_x(0),
      acc_y(0),
      acc_z(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_angle_x;
      u_angle_x.real = this->angle_x;
      *(outbuffer + offset + 0) = (u_angle_x.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_angle_x.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_angle_x.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_angle_x.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->angle_x);
      union {
        float real;
        uint32_t base;
      } u_angle_y;
      u_angle_y.real = this->angle_y;
      *(outbuffer + offset + 0) = (u_angle_y.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_angle_y.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_angle_y.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_angle_y.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->angle_y);
      union {
        float real;
        uint32_t base;
      } u_angle_z;
      u_angle_z.real = this->angle_z;
      *(outbuffer + offset + 0) = (u_angle_z.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_angle_z.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_angle_z.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_angle_z.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->angle_z);
      union {
        float real;
        uint32_t base;
      } u_gyr_x;
      u_gyr_x.real = this->gyr_x;
      *(outbuffer + offset + 0) = (u_gyr_x.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_gyr_x.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_gyr_x.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_gyr_x.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->gyr_x);
      union {
        float real;
        uint32_t base;
      } u_gyr_y;
      u_gyr_y.real = this->gyr_y;
      *(outbuffer + offset + 0) = (u_gyr_y.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_gyr_y.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_gyr_y.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_gyr_y.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->gyr_y);
      union {
        float real;
        uint32_t base;
      } u_gyr_z;
      u_gyr_z.real = this->gyr_z;
      *(outbuffer + offset + 0) = (u_gyr_z.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_gyr_z.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_gyr_z.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_gyr_z.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->gyr_z);
      union {
        float real;
        uint32_t base;
      } u_acc_x;
      u_acc_x.real = this->acc_x;
      *(outbuffer + offset + 0) = (u_acc_x.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_acc_x.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_acc_x.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_acc_x.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->acc_x);
      union {
        float real;
        uint32_t base;
      } u_acc_y;
      u_acc_y.real = this->acc_y;
      *(outbuffer + offset + 0) = (u_acc_y.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_acc_y.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_acc_y.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_acc_y.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->acc_y);
      union {
        float real;
        uint32_t base;
      } u_acc_z;
      u_acc_z.real = this->acc_z;
      *(outbuffer + offset + 0) = (u_acc_z.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_acc_z.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_acc_z.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_acc_z.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->acc_z);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_angle_x;
      u_angle_x.base = 0;
      u_angle_x.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_angle_x.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_angle_x.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_angle_x.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->angle_x = u_angle_x.real;
      offset += sizeof(this->angle_x);
      union {
        float real;
        uint32_t base;
      } u_angle_y;
      u_angle_y.base = 0;
      u_angle_y.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_angle_y.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_angle_y.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_angle_y.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->angle_y = u_angle_y.real;
      offset += sizeof(this->angle_y);
      union {
        float real;
        uint32_t base;
      } u_angle_z;
      u_angle_z.base = 0;
      u_angle_z.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_angle_z.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_angle_z.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_angle_z.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->angle_z = u_angle_z.real;
      offset += sizeof(this->angle_z);
      union {
        float real;
        uint32_t base;
      } u_gyr_x;
      u_gyr_x.base = 0;
      u_gyr_x.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_gyr_x.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_gyr_x.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_gyr_x.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->gyr_x = u_gyr_x.real;
      offset += sizeof(this->gyr_x);
      union {
        float real;
        uint32_t base;
      } u_gyr_y;
      u_gyr_y.base = 0;
      u_gyr_y.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_gyr_y.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_gyr_y.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_gyr_y.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->gyr_y = u_gyr_y.real;
      offset += sizeof(this->gyr_y);
      union {
        float real;
        uint32_t base;
      } u_gyr_z;
      u_gyr_z.base = 0;
      u_gyr_z.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_gyr_z.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_gyr_z.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_gyr_z.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->gyr_z = u_gyr_z.real;
      offset += sizeof(this->gyr_z);
      union {
        float real;
        uint32_t base;
      } u_acc_x;
      u_acc_x.base = 0;
      u_acc_x.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_acc_x.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_acc_x.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_acc_x.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->acc_x = u_acc_x.real;
      offset += sizeof(this->acc_x);
      union {
        float real;
        uint32_t base;
      } u_acc_y;
      u_acc_y.base = 0;
      u_acc_y.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_acc_y.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_acc_y.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_acc_y.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->acc_y = u_acc_y.real;
      offset += sizeof(this->acc_y);
      union {
        float real;
        uint32_t base;
      } u_acc_z;
      u_acc_z.base = 0;
      u_acc_z.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_acc_z.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_acc_z.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_acc_z.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->acc_z = u_acc_z.real;
      offset += sizeof(this->acc_z);
     return offset;
    }

    virtual const char * getType() override { return "test/IMU"; };
    virtual const char * getMD5() override { return "b6894b4d9810ae1193e5899d0d32ce57"; };

  };

}
#endif
