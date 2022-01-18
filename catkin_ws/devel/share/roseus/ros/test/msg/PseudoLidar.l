;; Auto-generated. Do not edit!


(when (boundp 'test::PseudoLidar)
  (if (not (find-package "TEST"))
    (make-package "TEST"))
  (shadow 'PseudoLidar (find-package "TEST")))
(unless (find-package "TEST::PSEUDOLIDAR")
  (make-package "TEST::PSEUDOLIDAR"))

(in-package "ROS")
;;//! \htmlinclude PseudoLidar.msg.html


(defclass test::PseudoLidar
  :super ros::object
  :slots (_angular_pose _distance ))

(defmethod test::PseudoLidar
  (:init
   (&key
    ((:angular_pose __angular_pose) 0)
    ((:distance __distance) 0.0)
    )
   (send-super :init)
   (setq _angular_pose (round __angular_pose))
   (setq _distance (float __distance))
   self)
  (:angular_pose
   (&optional __angular_pose)
   (if __angular_pose (setq _angular_pose __angular_pose)) _angular_pose)
  (:distance
   (&optional __distance)
   (if __distance (setq _distance __distance)) _distance)
  (:serialization-length
   ()
   (+
    ;; int32 _angular_pose
    4
    ;; float32 _distance
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _angular_pose
       (write-long _angular_pose s)
     ;; float32 _distance
       (sys::poke _distance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _angular_pose
     (setq _angular_pose (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _distance
     (setq _distance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get test::PseudoLidar :md5sum-) "729a5e2e97a158c163f31ff29858d7de")
(setf (get test::PseudoLidar :datatype-) "test/PseudoLidar")
(setf (get test::PseudoLidar :definition-)
      "int32 angular_pose
float32 distance

")



(provide :test/PseudoLidar "729a5e2e97a158c163f31ff29858d7de")


