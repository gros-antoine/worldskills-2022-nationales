
(cl:in-package :asdf)

(defsystem "test-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Encoders" :depends-on ("_package_Encoders"))
    (:file "_package_Encoders" :depends-on ("_package"))
    (:file "IMU" :depends-on ("_package_IMU"))
    (:file "_package_IMU" :depends-on ("_package"))
    (:file "Moteurs" :depends-on ("_package_Moteurs"))
    (:file "_package_Moteurs" :depends-on ("_package"))
    (:file "PseudoLidar" :depends-on ("_package_PseudoLidar"))
    (:file "_package_PseudoLidar" :depends-on ("_package"))
  ))