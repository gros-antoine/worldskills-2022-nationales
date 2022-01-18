;; Auto-generated. Do not edit!


(when (boundp 'test::Encoders)
  (if (not (find-package "TEST"))
    (make-package "TEST"))
  (shadow 'Encoders (find-package "TEST")))
(unless (find-package "TEST::ENCODERS")
  (make-package "TEST::ENCODERS"))

(in-package "ROS")
;;//! \htmlinclude Encoders.msg.html


(defclass test::Encoders
  :super ros::object
  :slots (_angular_pose_droit _angular_pose_gauche ))

(defmethod test::Encoders
  (:init
   (&key
    ((:angular_pose_droit __angular_pose_droit) 0)
    ((:angular_pose_gauche __angular_pose_gauche) 0)
    )
   (send-super :init)
   (setq _angular_pose_droit (round __angular_pose_droit))
   (setq _angular_pose_gauche (round __angular_pose_gauche))
   self)
  (:angular_pose_droit
   (&optional __angular_pose_droit)
   (if __angular_pose_droit (setq _angular_pose_droit __angular_pose_droit)) _angular_pose_droit)
  (:angular_pose_gauche
   (&optional __angular_pose_gauche)
   (if __angular_pose_gauche (setq _angular_pose_gauche __angular_pose_gauche)) _angular_pose_gauche)
  (:serialization-length
   ()
   (+
    ;; int32 _angular_pose_droit
    4
    ;; int32 _angular_pose_gauche
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _angular_pose_droit
       (write-long _angular_pose_droit s)
     ;; int32 _angular_pose_gauche
       (write-long _angular_pose_gauche s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _angular_pose_droit
     (setq _angular_pose_droit (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _angular_pose_gauche
     (setq _angular_pose_gauche (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get test::Encoders :md5sum-) "fc034961e6054d917c3fd8d0aec3b1d6")
(setf (get test::Encoders :datatype-) "test/Encoders")
(setf (get test::Encoders :definition-)
      "int32 angular_pose_droit
int32 angular_pose_gauche

")



(provide :test/Encoders "fc034961e6054d917c3fd8d0aec3b1d6")


