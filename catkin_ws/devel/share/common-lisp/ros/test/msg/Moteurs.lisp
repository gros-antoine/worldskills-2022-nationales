; Auto-generated. Do not edit!


(cl:in-package test-msg)


;//! \htmlinclude Moteurs.msg.html

(cl:defclass <Moteurs> (roslisp-msg-protocol:ros-message)
  ((moteur_droit
    :reader moteur_droit
    :initarg :moteur_droit
    :type cl:integer
    :initform 0)
   (moteur_gauche
    :reader moteur_gauche
    :initarg :moteur_gauche
    :type cl:integer
    :initform 0))
)

(cl:defclass Moteurs (<Moteurs>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Moteurs>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Moteurs)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test-msg:<Moteurs> is deprecated: use test-msg:Moteurs instead.")))

(cl:ensure-generic-function 'moteur_droit-val :lambda-list '(m))
(cl:defmethod moteur_droit-val ((m <Moteurs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test-msg:moteur_droit-val is deprecated.  Use test-msg:moteur_droit instead.")
  (moteur_droit m))

(cl:ensure-generic-function 'moteur_gauche-val :lambda-list '(m))
(cl:defmethod moteur_gauche-val ((m <Moteurs>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test-msg:moteur_gauche-val is deprecated.  Use test-msg:moteur_gauche instead.")
  (moteur_gauche m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Moteurs>) ostream)
  "Serializes a message object of type '<Moteurs>"
  (cl:let* ((signed (cl:slot-value msg 'moteur_droit)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'moteur_gauche)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Moteurs>) istream)
  "Deserializes a message object of type '<Moteurs>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'moteur_droit) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'moteur_gauche) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Moteurs>)))
  "Returns string type for a message object of type '<Moteurs>"
  "test/Moteurs")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Moteurs)))
  "Returns string type for a message object of type 'Moteurs"
  "test/Moteurs")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Moteurs>)))
  "Returns md5sum for a message object of type '<Moteurs>"
  "92e98c0f8f5930e16579b4e451e99d48")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Moteurs)))
  "Returns md5sum for a message object of type 'Moteurs"
  "92e98c0f8f5930e16579b4e451e99d48")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Moteurs>)))
  "Returns full string definition for message of type '<Moteurs>"
  (cl:format cl:nil "int32 moteur_droit~%int32 moteur_gauche~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Moteurs)))
  "Returns full string definition for message of type 'Moteurs"
  (cl:format cl:nil "int32 moteur_droit~%int32 moteur_gauche~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Moteurs>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Moteurs>))
  "Converts a ROS message object to a list"
  (cl:list 'Moteurs
    (cl:cons ':moteur_droit (moteur_droit msg))
    (cl:cons ':moteur_gauche (moteur_gauche msg))
))
