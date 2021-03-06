#!/usr/bin/env python3
 
import rospy
from std_msgs.msg import Float32MultiArray, String
from sensor_msgs.msg import Joy
from numpy import sign
from test.msg import Moteurs
 
# Paramètres
turning_vitesse_max = 150
turning_vitesse_min = 40
vitesse_avance_max = 255
vitesse_avance_min = 60
vitesse_bras_max = 200
vitesse_bras_min = 50
 
pub = rospy.Publisher('chatter_move', Moteurs, queue_size=10)
 
def pec(vmax_s, vmin_s, vmax_e, vmin_e, r):
    return r * (vmax_s - vmin_s) / (vmax_e - vmin_e) + sign(r)*vmin_s
 
def callback(data):
 
    global pub
    
    moteurs = Moteurs()
     
    msg = Float32MultiArray();
 
    axes = data.axes                                  # tableau des axes
                                                      # [joy_gauche_left_right, joy_gauche_up_down, gach_gauche, joy_droit_left_right, joy_gauche_up]
    buttons = data.buttons                            # tableau des boutons (
 
    joy_gauche_left_right = axes[0]                   # compris entre -1 et 1, gauche : 1, droite : -1
 
    joy_droit_up_down = axes[4]                       # 
 
    but_A = buttons[0]                                #
 
    but_X = buttons[2]                                # 
 
    if(joy_gauche_left_right == 0):
 
        if(joy_droit_up_down == 0):
 
            if(but_X == 0):
 
                if(but_A == 0):
 
                    gach_droite = - axes[5]                # compris entre -1 et 1, off : -1, on : 1
                    gach_gauche = axes[2]                  # compris entre -1 et 1, off : 1, on : -1
                    
                    gach_droite += 1                       # compris entre 0 et 2, off : 0, on : 2
                    gach_gauche -= 1                       # compris entre -2 et 0, off : 0, on : -2
 
                    vitesse = gach_droite + gach_gauche    # compris entre -2 et 2, entre -2 et 0, recul de moins en moins vite, entre 0 et 2, avance de plus en plus vite, 0, ne bouge pas
 
                    vitesse_moteurs = int(pec(vitesse_avance_max, vitesse_avance_min, 2, 0, vitesse))  # produit en croix, compris entre -255 et -100 puis 0 puis 100 et 255
 
                    #msg.data = [vitesse_moteurs, vitesse_moteurs, 0, 0]
                    moteurs.moteur_droit = vitesse_moteurs
                    moteurs.moteur_gauche = vitesse_moteurs
                    pub.publish(moteurs)
                    #pub.publish(msg)
 
                else:
                    #msg.data = [0, 0, 0, 100]
                    moteurs.moteur_droit = 0
                    moteurs.moteur_gauche = 0
                    #pub.publish(msg)
            else:
                #msg.data = [0, 0, 0, -100]
                moteurs.moteur_droit = 0
                moteurs.moteur_gauche = 0
                #pub.publish(msg)
        else:
            
            vitesse_bras = pec(vitesse_bras_max, vitesse_bras_min, 1, 0, joy_droit_up_down)
            #msg.data = [0, 0, int(vitesse_bras), 0]
            moteurs.moteur_droit = 0
            moteurs.moteur_gauche = 0
            #pub.publish(msg)

    else:
        
        turning_vitesse = int(pec(turning_vitesse_max, turning_vitesse_min, 1, 0, joy_gauche_left_right))
        #msg.data = [turning_vitesse, -turning_vitesse, 0, 0]
        moteurs.moteur_droit = turning_vitesse
        moteurs.moteur_gauche = -turning_vitesse
        pub.publish(moteurs)
 
def listener():
     rospy.init_node('interface', anonymous=True)
     rospy.Subscriber("joy", Joy, callback)
     rospy.spin()
 
if __name__ == '__main__':
     try:
          listener()
     except:
          pass
