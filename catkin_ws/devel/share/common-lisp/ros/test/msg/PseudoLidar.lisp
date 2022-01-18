; Auto-generated. Do not edit!


(cl:in-package test-msg)


;//! \htmlinclude PseudoLidar.msg.html

(cl:defclass <PseudoLidar> (roslisp-msg-protocol:ros-message)
  ((angular_pose
    :reader angular_pose
    :initarg :angular_pose
    :type cl:integer
    :initform 0)
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass PseudoLidar (<PseudoLidar>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PseudoLidar>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PseudoLidar)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test-msg:<PseudoLidar> is deprecated: use test-msg:PseudoLidar instead.")))

(cl:ensure-generic-function 'angular_pose-val :lambda-list '(m))
(cl:defmethod angular_pose-val ((m <PseudoLidar>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test-msg:angular_pose-val is deprecated.  Use test-msg:angular_pose instead.")
  (angular_pose m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <PseudoLidar>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test-msg:distance-val is deprecated.  Use test-msg:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PseudoLidar>) ostream)
  "Serializes a message object of type '<PseudoLidar>"
  (cl:let* ((signed (cl:slot-value msg 'angular_pose)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PseudoLidar>) istream)
  "Deserializes a message object of type '<PseudoLidar>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angular_pose) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PseudoLidar>)))
  "Returns string type for a message object of type '<PseudoLidar>"
  "test/PseudoLidar")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PseudoLidar)))
  "Returns string type for a message object of type 'PseudoLidar"
  "test/PseudoLidar")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PseudoLidar>)))
  "Returns md5sum for a message object of type '<PseudoLidar>"
  "729a5e2e97a158c163f31ff29858d7de")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PseudoLidar)))
  "Returns md5sum for a message object of type 'PseudoLidar"
  "729a5e2e97a158c163f31ff29858d7de")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PseudoLidar>)))
  "Returns full string definition for message of type '<PseudoLidar>"
  (cl:format cl:nil "int32 angular_pose~%float32 distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PseudoLidar)))
  "Returns full string definition for message of type 'PseudoLidar"
  (cl:format cl:nil "int32 angular_pose~%float32 distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PseudoLidar>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PseudoLidar>))
  "Converts a ROS message object to a list"
  (cl:list 'PseudoLidar
    (cl:cons ':angular_pose (angular_pose msg))
    (cl:cons ':distance (distance msg))
))
