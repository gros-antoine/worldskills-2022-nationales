#ifndef _ROS_test_PseudoLidar_h
#define _ROS_test_PseudoLidar_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace test
{

  class PseudoLidar : public ros::Msg
  {
    public:
      typedef int32_t _angular_pose_type;
      _angular_pose_type angular_pose;
      typedef float _distance_type;
      _distance_type distance;

    PseudoLidar():
      angular_pose(0),
      distance(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_angular_pose;
      u_angular_pose.real = this->angular_pose;
      *(outbuffer + offset + 0) = (u_angular_pose.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_angular_pose.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_angular_pose.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_angular_pose.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->angular_pose);
      union {
        float real;
        uint32_t base;
      } u_distance;
      u_distance.real = this->distance;
      *(outbuffer + offset + 0) = (u_distance.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_distance.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_distance.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_distance.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->distance);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_angular_pose;
      u_angular_pose.base = 0;
      u_angular_pose.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_angular_pose.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_angular_pose.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_angular_pose.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->angular_pose = u_angular_pose.real;
      offset += sizeof(this->angular_pose);
      union {
        float real;
        uint32_t base;
      } u_distance;
      u_distance.base = 0;
      u_distance.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_distance.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_distance.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_distance.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->distance = u_distance.real;
      offset += sizeof(this->distance);
     return offset;
    }

    virtual const char * getType() override { return "test/PseudoLidar"; };
    virtual const char * getMD5() override { return "729a5e2e97a158c163f31ff29858d7de"; };

  };

}
#endif
