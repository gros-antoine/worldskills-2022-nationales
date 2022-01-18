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

class Moteurs {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.moteur_droit = null;
      this.moteur_gauche = null;
    }
    else {
      if (initObj.hasOwnProperty('moteur_droit')) {
        this.moteur_droit = initObj.moteur_droit
      }
      else {
        this.moteur_droit = 0;
      }
      if (initObj.hasOwnProperty('moteur_gauche')) {
        this.moteur_gauche = initObj.moteur_gauche
      }
      else {
        this.moteur_gauche = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Moteurs
    // Serialize message field [moteur_droit]
    bufferOffset = _serializer.int32(obj.moteur_droit, buffer, bufferOffset);
    // Serialize message field [moteur_gauche]
    bufferOffset = _serializer.int32(obj.moteur_gauche, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Moteurs
    let len;
    let data = new Moteurs(null);
    // Deserialize message field [moteur_droit]
    data.moteur_droit = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [moteur_gauche]
    data.moteur_gauche = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'test/Moteurs';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '92e98c0f8f5930e16579b4e451e99d48';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 moteur_droit
    int32 moteur_gauche
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Moteurs(null);
    if (msg.moteur_droit !== undefined) {
      resolved.moteur_droit = msg.moteur_droit;
    }
    else {
      resolved.moteur_droit = 0
    }

    if (msg.moteur_gauche !== undefined) {
      resolved.moteur_gauche = msg.moteur_gauche;
    }
    else {
      resolved.moteur_gauche = 0
    }

    return resolved;
    }
};

module.exports = Moteurs;
