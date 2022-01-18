;; Auto-generated. Do not edit!


(when (boundp 'test::Moteurs)
  (if (not (find-package "TEST"))
    (make-package "TEST"))
  (shadow 'Moteurs (find-package "TEST")))
(unless (find-package "TEST::MOTEURS")
  (make-package "TEST::MOTEURS"))

(in-package "ROS")
;;//! \htmlinclude Moteurs.msg.html


(defclass test::Moteurs
  :super ros::object
  :slots (_moteur_droit _moteur_gauche ))

(defmethod test::Moteurs
  (:init
   (&key
    ((:moteur_droit __moteur_droit) 0)
    ((:moteur_gauche __moteur_gauche) 0)
    )
   (send-super :init)
   (setq _moteur_droit (round __moteur_droit))
   (setq _moteur_gauche (round __moteur_gauche))
   self)
  (:moteur_droit
   (&optional __moteur_droit)
   (if __moteur_droit (setq _moteur_droit __moteur_droit)) _moteur_droit)
  (:moteur_gauche
   (&optional __moteur_gauche)
   (if __moteur_gauche (setq _moteur_gauche __moteur_gauche)) _moteur_gauche)
  (:serialization-length
   ()
   (+
    ;; int32 _moteur_droit
    4
    ;; int32 _moteur_gauche
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _moteur_droit
       (write-long _moteur_droit s)
     ;; int32 _moteur_gauche
       (write-long _moteur_gauche s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _moteur_droit
     (setq _moteur_droit (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _moteur_gauche
     (setq _moteur_gauche (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get test::Moteurs :md5sum-) "92e98c0f8f5930e16579b4e451e99d48")
(setf (get test::Moteurs :datatype-) "test/Moteurs")
(setf (get test::Moteurs :definition-)
      "int32 moteur_droit
int32 moteur_gauche

")



(provide :test/Moteurs "92e98c0f8f5930e16579b4e451e99d48")


