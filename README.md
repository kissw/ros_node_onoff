## Ros Node On Off

ROS Node On Off 프로그램  </br></br>

## 사용법
ros_node_onoff.yaml 파일에서 파라미터를 변경하여 원하는 node를 끄고 킬수있고  
필요하면 src/ros_node_onoff.py 파일을 import해서 사용하면 됨.

### Example Code
```python
from ros_node_onoff import RosNodeOnOff
...
rnoo = RosNodeOnOff()
rnoo.ros_node_off() # node 종료 함수
rnoo.ros_node_on() # node 시작 함수
```

### 파라미터
```yaml
ros_pakage_name: turtlesim # ROS 패키지 이름
ros_excutable_file_name: turtle_teleop_key # ROS 실행파일 이름 
ros_node_name: teleop_turtle # ROS Node 이름.
# 대부분 excutable file과 node name이 동일하나 turtle teleop key 처럼 다른 경우도 있으니 참고.
```

</br>
</br>

### 명령어
conda 환경설치 방법은 상위 폴더를 참조
```
(base) $ conda activate 3w

(3w) $ python src/ros_node_onoff.py
```