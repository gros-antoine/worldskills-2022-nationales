; Auto-generated. Do not edit!


(cl:in-package test-msg)


;//! \htmlinclude Encoders.msg.html

(cl:defclass <Encoders> (roslisp-msg-protocol:ros-message)
  ((angular_pose_droit
    :reader angular_pose_droit
    :initarg :angular_pose_droit
    :type cl:integer
    :initform 0)
   (angular_pose_gauche
    :reader angular_pose_gauche
    :initarg :angular_pose_gauche
    :type cl:integer
    :initform 0))
)

(cl:defclass Encoders (<Encoders>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Encoders>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Encoders)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test-msg:<Encoders> is deprecated: use test-msg:Encoders instead.")))

(cl:ensure-generic-function 'angular_pose_droit-val :lambda-list '(m))
(cl:defmethod angular_pose_droit-val ((m <Encoders>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test-msg:angular_pose_droit-val is deprecated.  Use test-msg:angular_pose_droit instead.")
  (angular_pose_droit m))

(cl:ensure-generic-function 'angular_pose_gauche-val :lambda-list '(m))
(cl:defmethod angular_pose_gauche-val ((m <Encoders>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test-msg:angular_pose_gauche-val is deprecated.  Use test-msg:angular_pose_gauche instead.")
  (angular_pose_gauche m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Encoders>) ostream)
  "Serializes a message object of type '<Encoders>"
  (cl:let* ((signed (cl:slot-value msg 'angular_pose_droit)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'angular_pose_gauche)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Encoders>) istream)
  "Deserializes a message object of type '<Encoders>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angular_pose_droit) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angular_pose_gauche) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Encoders>)))
  "Returns string type for a message object of type '<Encoders>"
  "test/Encoders")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Encoders)))
  "Returns string type for a message object of type 'Encoders"
  "test/Encoders")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Encoders>)))
  "Returns md5sum for a message object of type '<Encoders>"
  "fc034961e6054d917c3fd8d0aec3b1d6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Encoders)))
  "Returns md5sum for a message object of type 'Encoders"
  "fc034961e6054d917c3fd8d0aec3b1d6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Encoders>)))
  "Returns full string definition for message of type '<Encoders>"
  (cl:format cl:nil "int32 angular_pose_droit~%int32 angular_pose_gauche~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Encoders)))
  "Returns full string definition for message of type 'Encoders"
  (cl:format cl:nil "int32 angular_pose_droit~%int32 angular_pose_gauche~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Encoders>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Encoders>))
  "Converts a ROS message object to a list"
  (cl:list 'Encoders
    (cl:cons ':angular_pose_droit (angular_pose_droit msg))
    (cl:cons ':angular_pose_gauche (angular_pose_gauche msg))
))
