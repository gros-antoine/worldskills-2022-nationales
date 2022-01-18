// Auto-generated. Do not edit!

// (in-package test.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Encoders {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.angular_pose_droit = null;
      this.angular_pose_gauche = null;
    }
    else {
      if (initObj.hasOwnProperty('angular_pose_droit')) {
        this.angular_pose_droit = initObj.angular_pose_droit
      }
      else {
        this.angular_pose_droit = 0;
      }
      if (initObj.hasOwnProperty('angular_pose_gauche')) {
        this.angular_pose_gauche = initObj.angular_pose_gauche
      }
      else {
        this.angular_pose_gauche = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Encoders
    // Serialize message field [angular_pose_droit]
    bufferOffset = _serializer.int32(obj.angular_pose_droit, buffer, bufferOffset);
    // Serialize message field [angular_pose_gauche]
    bufferOffset = _serializer.int32(obj.angular_pose_gauche, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Encoders
    let len;
    let data = new Encoders(null);
    // Deserialize message field [angular_pose_droit]
    data.angular_pose_droit = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [angular_pose_gauche]
    data.angular_pose_gauche = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'test/Encoders';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fc034961e6054d917c3fd8d0aec3b1d6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 angular_pose_droit
    int32 angular_pose_gauche
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Encoders(null);
    if (msg.angular_pose_droit !== undefined) {
      resolved.angular_pose_droit = msg.angular_pose_droit;
    }
    else {
      resolved.angular_pose_droit = 0
    }

    if (msg.angular_pose_gauche !== undefined) {
      resolved.angular_pose_gauche = msg.angular_pose_gauche;
    }
    else {
      resolved.angular_pose_gauche = 0
    }

    return resolved;
    }
};

module.exports = Encoders;
