# Práctica 3 MSR
## Carla García Alejandre
-------------------------------------------------------------------------------------

## Introducción
El objetivo de esta práctica es configurar el modelo de rover realizado en la práctica anterior en blender para poder visualizarlo y manipularlo en el framework de moveit con ros2.

## Creación de xacros
La primera etapa de esta ráctica consiste en separar el archivo urdf generado por blender en la práctica anterior en archivo separados en xacros.

```bash
urdf
├── arm
│   ├── gripper.urdf.xacro
│   └── scara.urdf.xacro
├── base
│   └── robot_base.urdf.xacro
├── ros2_control.urdf.xacro
├── sensors
│   ├── camera.urdf.xacro
│   ├── gps.urdf.xacro
│   └── imu_sensor.urdf.xacro
├── utils
│   └── utils.urdf.xacro
└── wheels
    └── wheels.urdf.xacro
```

La estructura de estos archivos es [...]

Una vez hecho esto se llama a todo en un único archoivo `robot.urdf.xacro` dentro de robots que en el que se llama a todos los otros xacros y se crean las instancias de cada uno con sus padres y sus ubicaciones.

## Modelo del robot
Para visualizar el modelo del robot en rviz generamos el launcher robot_state_publisher que [...] 

foto modelo del robot

Segun el modelo del robot diseñado estas son las tfs

foto tfs y tfs con el robot.

foto arbol de tfs

### Joints

para comprobar que está bien podemos mover los trackbars para ver si se mueven correctamente bla bla bla

foto sin mover joints

foto con joints movidos

gif moviendo los joints

## Entorno

El mundo donde se desarrolla la practica es urjc excavation msr link al repo, que tiene el robot en el 00 y tres cubos 3, 0, 0, 3, 0 -3. vamos a tener que coger el cubo verde guardar en el maletero y poner el cubop azxul encima del rojo

foto entorno

para poder lanzarlo robot_gazebo.launch.py

## Moveit setup assistant

Para poder generar las posiciones del rover usamos moveit setup assistante de primeras te genera el paquete tal y del paquete tenemos las poses en rover srdf y mas cosas en config qu etienen los limites de los joints y eso

hablar de las cosas que hay que quiatr y poner

## Controladores
ros2 controller tal lanzar joint broadcaster scara gripper y rover son tres controladores separados y ahora qu etenemos todoo lanzamos launch 1 launch 2 launch 3 y teclado par amover las ruedas que estan definidas es ros2 control urdf de rover description.


## Ejecución
### Cubo verde

bla bla bla

fotoc ubo verde en el aure

video cubo verde en el aire

### Cubos azul y rojo 

bal bal bla

foto a puntpo de colocar cosa

video colocando

### Rosbag

GRabar rosbag con los topics cmdvel imu data y joint statte para luego poder analizar gasto y cosas y tal link al rosbag 

## Análisis del mecanismo

Graficas que s ehan generado del rosbag bla bla bla

### Gasto

### Posición de ruedas

### Aceleración imu

## Conclusiones

