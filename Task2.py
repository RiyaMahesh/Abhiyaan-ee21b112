import rospy
from std_msgs.msg import String
 
def node1():
    pub = rospy.Publisher('/team_abhiyaan', String, queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "Team Abhiyaan rocks: %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        
    def listener
    ():
    
        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('listener', anonymous=True)
   
        rospy.Subscriber("/team_abhiyaan", String, callback)
   
        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
   
if __name__ == '__main__':
    listener()

def node3():
    pub = rospy.Publisher('/naayihba_maet', String, queue_size=10) 
    rospy.init_node('node3', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        revhello_str = reverse(hello_str) % rospy.get_time()
        rospy.loginfo(revhello_str)
        pub.publish(revhello_str)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        node3()
    except rospy.ROSInterruptException:
        pass

