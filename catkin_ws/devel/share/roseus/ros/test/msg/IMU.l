;; Auto-generated. Do not edit!


(when (boundp 'test::IMU)
  (if (not (find-package "TEST"))
    (make-package "TEST"))
  (shadow 'IMU (find-package "TEST")))
(unless (find-package "TEST::IMU")
  (make-package "TEST::IMU"))

(in-package "ROS")
;;//! \htmlinclude IMU.msg.html


(defclass test::IMU
  :super ros::object
  :slots (_angle_x _angle_y _angle_z _gyr_x _gyr_y _gyr_z _acc_x _acc_y _acc_z ))

(defmethod test::IMU
  (:init
   (&key
    ((:angle_x __angle_x) 0.0)
    ((:angle_y __angle_y) 0.0)
    ((:angle_z __angle_z) 0.0)
    ((:gyr_x __gyr_x) 0.0)
    ((:gyr_y __gyr_y) 0.0)
    ((:gyr_z __gyr_z) 0.0)
    ((:acc_x __acc_x) 0.0)
    ((:acc_y __acc_y) 0.0)
    ((:acc_z __acc_z) 0.0)
    )
   (send-super :init)
   (setq _angle_x (float __angle_x))
   (setq _angle_y (float __angle_y))
   (setq _angle_z (float __angle_z))
   (setq _gyr_x (float __gyr_x))
   (setq _gyr_y (float __gyr_y))
   (setq _gyr_z (float __gyr_z))
   (setq _acc_x (float __acc_x))
   (setq _acc_y (float __acc_y))
   (setq _acc_z (float __acc_z))
   self)
  (:angle_x
   (&optional __angle_x)
   (if __angle_x (setq _angle_x __angle_x)) _angle_x)
  (:angle_y
   (&optional __angle_y)
   (if __angle_y (setq _angle_y __angle_y)) _angle_y)
  (:angle_z
   (&optional __angle_z)
   (if __angle_z (setq _angle_z __angle_z)) _angle_z)
  (:gyr_x
   (&optional __gyr_x)
   (if __gyr_x (setq _gyr_x __gyr_x)) _gyr_x)
  (:gyr_y
   (&optional __gyr_y)
   (if __gyr_y (setq _gyr_y __gyr_y)) _gyr_y)
  (:gyr_z
   (&optional __gyr_z)
   (if __gyr_z (setq _gyr_z __gyr_z)) _gyr_z)
  (:acc_x
   (&optional __acc_x)
   (if __acc_x (setq _acc_x __acc_x)) _acc_x)
  (:acc_y
   (&optional __acc_y)
   (if __acc_y (setq _acc_y __acc_y)) _acc_y)
  (:acc_z
   (&optional __acc_z)
   (if __acc_z (setq _acc_z __acc_z)) _acc_z)
  (:serialization-length
   ()
   (+
    ;; float32 _angle_x
    4
    ;; float32 _angle_y
    4
    ;; float32 _angle_z
    4
    ;; float32 _gyr_x
    4
    ;; float32 _gyr_y
    4
    ;; float32 _gyr_z
    4
    ;; float32 _acc_x
    4
    ;; float32 _acc_y
    4
    ;; float32 _acc_z
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _angle_x
       (sys::poke _angle_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _angle_y
       (sys::poke _angle_y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _angle_z
       (sys::poke _angle_z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gyr_x
       (sys::poke _gyr_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gyr_y
       (sys::poke _gyr_y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _gyr_z
       (sys::poke _gyr_z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _acc_x
       (sys::poke _acc_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _acc_y
       (sys::poke _acc_y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _acc_z
       (sys::poke _acc_z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _angle_x
     (setq _angle_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _angle_y
     (setq _angle_y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _angle_z
     (setq _angle_z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gyr_x
     (setq _gyr_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gyr_y
     (setq _gyr_y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _gyr_z
     (setq _gyr_z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _acc_x
     (setq _acc_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _acc_y
     (setq _acc_y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _acc_z
     (setq _acc_z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get test::IMU :md5sum-) "b6894b4d9810ae1193e5899d0d32ce57")
(setf (get test::IMU :datatype-) "test/IMU")
(setf (get test::IMU :definition-)
      "float32 angle_x
float32 angle_y
float32 angle_z
float32 gyr_x
float32 gyr_y
float32 gyr_z
float32 acc_x
float32 acc_y
float32 acc_z

")



(provide :test/IMU "b6894b4d9810ae1193e5899d0d32ce57")


