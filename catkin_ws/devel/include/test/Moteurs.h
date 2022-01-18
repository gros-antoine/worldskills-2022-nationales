// Generated by gencpp from file test/Moteurs.msg
// DO NOT EDIT!


#ifndef TEST_MESSAGE_MOTEURS_H
#define TEST_MESSAGE_MOTEURS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace test
{
template <class ContainerAllocator>
struct Moteurs_
{
  typedef Moteurs_<ContainerAllocator> Type;

  Moteurs_()
    : moteur_droit(0)
    , moteur_gauche(0)  {
    }
  Moteurs_(const ContainerAllocator& _alloc)
    : moteur_droit(0)
    , moteur_gauche(0)  {
  (void)_alloc;
    }



   typedef int32_t _moteur_droit_type;
  _moteur_droit_type moteur_droit;

   typedef int32_t _moteur_gauche_type;
  _moteur_gauche_type moteur_gauche;





  typedef boost::shared_ptr< ::test::Moteurs_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test::Moteurs_<ContainerAllocator> const> ConstPtr;

}; // struct Moteurs_

typedef ::test::Moteurs_<std::allocator<void> > Moteurs;

typedef boost::shared_ptr< ::test::Moteurs > MoteursPtr;
typedef boost::shared_ptr< ::test::Moteurs const> MoteursConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test::Moteurs_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test::Moteurs_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::test::Moteurs_<ContainerAllocator1> & lhs, const ::test::Moteurs_<ContainerAllocator2> & rhs)
{
  return lhs.moteur_droit == rhs.moteur_droit &&
    lhs.moteur_gauche == rhs.moteur_gauche;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::test::Moteurs_<ContainerAllocator1> & lhs, const ::test::Moteurs_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace test

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::test::Moteurs_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test::Moteurs_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test::Moteurs_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test::Moteurs_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test::Moteurs_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test::Moteurs_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test::Moteurs_<ContainerAllocator> >
{
  static const char* value()
  {
    return "92e98c0f8f5930e16579b4e451e99d48";
  }

  static const char* value(const ::test::Moteurs_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x92e98c0f8f5930e1ULL;
  static const uint64_t static_value2 = 0x6579b4e451e99d48ULL;
};

template<class ContainerAllocator>
struct DataType< ::test::Moteurs_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test/Moteurs";
  }

  static const char* value(const ::test::Moteurs_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test::Moteurs_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 moteur_droit\n"
"int32 moteur_gauche\n"
;
  }

  static const char* value(const ::test::Moteurs_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test::Moteurs_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.moteur_droit);
      stream.next(m.moteur_gauche);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Moteurs_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test::Moteurs_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test::Moteurs_<ContainerAllocator>& v)
  {
    s << indent << "moteur_droit: ";
    Printer<int32_t>::stream(s, indent + "  ", v.moteur_droit);
    s << indent << "moteur_gauche: ";
    Printer<int32_t>::stream(s, indent + "  ", v.moteur_gauche);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_MESSAGE_MOTEURS_H
