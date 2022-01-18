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

class PseudoLidar {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.angular_pose = null;
      this.distance = null;
    }
    else {
      if (initObj.hasOwnProperty('angular_pose')) {
        this.angular_pose = initObj.angular_pose
      }
      else {
        this.angular_pose = 0;
      }
      if (initObj.hasOwnProperty('distance')) {
        this.distance = initObj.distance
      }
      else {
        this.distance = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PseudoLidar
    // Serialize message field [angular_pose]
    bufferOffset = _serializer.int32(obj.angular_pose, buffer, bufferOffset);
    // Serialize message field [distance]
    bufferOffset = _serializer.float32(obj.distance, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PseudoLidar
    let len;
    let data = new PseudoLidar(null);
    // Deserialize message field [angular_pose]
    data.angular_pose = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [distance]
    data.distance = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'test/PseudoLidar';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '729a5e2e97a158c163f31ff29858d7de';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 angular_pose
    float32 distance
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PseudoLidar(null);
    if (msg.angular_pose !== undefined) {
      resolved.angular_pose = msg.angular_pose;
    }
    else {
      resolved.angular_pose = 0
    }

    if (msg.distance !== undefined) {
      resolved.distance = msg.distance;
    }
    else {
      resolved.distance = 0.0
    }

    return resolved;
    }
};

module.exports = PseudoLidar;
