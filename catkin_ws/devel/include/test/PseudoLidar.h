// Generated by gencpp from file test/PseudoLidar.msg
// DO NOT EDIT!


#ifndef TEST_MESSAGE_PSEUDOLIDAR_H
#define TEST_MESSAGE_PSEUDOLIDAR_H


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
struct PseudoLidar_
{
  typedef PseudoLidar_<ContainerAllocator> Type;

  PseudoLidar_()
    : angular_pose(0)
    , distance(0.0)  {
    }
  PseudoLidar_(const ContainerAllocator& _alloc)
    : angular_pose(0)
    , distance(0.0)  {
  (void)_alloc;
    }



   typedef int32_t _angular_pose_type;
  _angular_pose_type angular_pose;

   typedef float _distance_type;
  _distance_type distance;





  typedef boost::shared_ptr< ::test::PseudoLidar_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test::PseudoLidar_<ContainerAllocator> const> ConstPtr;

}; // struct PseudoLidar_

typedef ::test::PseudoLidar_<std::allocator<void> > PseudoLidar;

typedef boost::shared_ptr< ::test::PseudoLidar > PseudoLidarPtr;
typedef boost::shared_ptr< ::test::PseudoLidar const> PseudoLidarConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test::PseudoLidar_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test::PseudoLidar_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::test::PseudoLidar_<ContainerAllocator1> & lhs, const ::test::PseudoLidar_<ContainerAllocator2> & rhs)
{
  return lhs.angular_pose == rhs.angular_pose &&
    lhs.distance == rhs.distance;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::test::PseudoLidar_<ContainerAllocator1> & lhs, const ::test::PseudoLidar_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace test

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::test::PseudoLidar_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test::PseudoLidar_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test::PseudoLidar_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test::PseudoLidar_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test::PseudoLidar_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test::PseudoLidar_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test::PseudoLidar_<ContainerAllocator> >
{
  static const char* value()
  {
    return "729a5e2e97a158c163f31ff29858d7de";
  }

  static const char* value(const ::test::PseudoLidar_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x729a5e2e97a158c1ULL;
  static const uint64_t static_value2 = 0x63f31ff29858d7deULL;
};

template<class ContainerAllocator>
struct DataType< ::test::PseudoLidar_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test/PseudoLidar";
  }

  static const char* value(const ::test::PseudoLidar_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test::PseudoLidar_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 angular_pose\n"
"float32 distance\n"
;
  }

  static const char* value(const ::test::PseudoLidar_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test::PseudoLidar_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.angular_pose);
      stream.next(m.distance);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PseudoLidar_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test::PseudoLidar_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test::PseudoLidar_<ContainerAllocator>& v)
  {
    s << indent << "angular_pose: ";
    Printer<int32_t>::stream(s, indent + "  ", v.angular_pose);
    s << indent << "distance: ";
    Printer<float>::stream(s, indent + "  ", v.distance);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_MESSAGE_PSEUDOLIDAR_H
