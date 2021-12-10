import sys, os
import yaml


class RosNodeOnOff():
    def __init__(self):
        ### load param
        try:
            config_name = './param/' + 'ros_node_onoff.yaml'
            with open(config_name) as file:
                self.yaml = yaml.load(file, Loader=yaml.FullLoader)
        except:
            exit('ERROR: ros_node_onoff.yaml not defined.') 

    
    def ros_node_off(self):
        os.system("rosnode kill " + self.yaml['ros_node_name'])
    
    def ros_node_on(self):
        os.system(  "rosrun "
                   + self.yaml['ros_pakage_name'] + " "
                   + self.yaml['ros_excutable_file_name'])
                    
def main():
    try:
        
        rnoo = RosNodeOnOff()
        rnoo.ros_node_off()
        rnoo.ros_node_on()
        
        
    except KeyboardInterrupt:
        pass
    finally:
        print("\nBye...")    

if __name__ == '__main__':
    main()