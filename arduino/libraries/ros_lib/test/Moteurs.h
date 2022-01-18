#ifndef _ROS_test_Moteurs_h
#define _ROS_test_Moteurs_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace test
{

  class Moteurs : public ros::Msg
  {
    public:
      typedef int32_t _moteur_droit_type;
      _moteur_droit_type moteur_droit;
      typedef int32_t _moteur_gauche_type;
      _moteur_gauche_type moteur_gauche;

    Moteurs():
      moteur_droit(0),
      moteur_gauche(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_moteur_droit;
      u_moteur_droit.real = this->moteur_droit;
      *(outbuffer + offset + 0) = (u_moteur_droit.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_moteur_droit.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_moteur_droit.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_moteur_droit.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->moteur_droit);
      union {
        int32_t real;
        uint32_t base;
      } u_moteur_gauche;
      u_moteur_gauche.real = this->moteur_gauche;
      *(outbuffer + offset + 0) = (u_moteur_gauche.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_moteur_gauche.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_moteur_gauche.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_moteur_gauche.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->moteur_gauche);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_moteur_droit;
      u_moteur_droit.base = 0;
      u_moteur_droit.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_moteur_droit.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_moteur_droit.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_moteur_droit.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->moteur_droit = u_moteur_droit.real;
      offset += sizeof(this->moteur_droit);
      union {
        int32_t real;
        uint32_t base;
      } u_moteur_gauche;
      u_moteur_gauche.base = 0;
      u_moteur_gauche.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_moteur_gauche.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_moteur_gauche.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_moteur_gauche.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->moteur_gauche = u_moteur_gauche.real;
      offset += sizeof(this->moteur_gauche);
     return offset;
    }

    virtual const char * getType() override { return "test/Moteurs"; };
    virtual const char * getMD5() override { return "92e98c0f8f5930e16579b4e451e99d48"; };

  };

}
#endif
