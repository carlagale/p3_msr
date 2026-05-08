import os
import numpy as np
import matplotlib.pyplot as plt
from rclpy.serialization import deserialize_message
import rosbag2_py
from rosidl_runtime_py.utilities import get_message

# --- 1. TU LISTA GENERAL DE COLORES ---
# Pon aquí todos los colores que te gusten en el orden que quieras
mis_colores = ['crimson', 'deeppink', 'violet', 'indigo', 'mediumslateblue', 'cornflowerblue', 'palevioletred', 'royalblue', 'magenta']

# --- CONFIGURACIÓN ---
bag_directory = "../rosbag_msr_cga"
arm_joint_names = [
    "revolute1_link_joint", "revolute2_link_joint",
    "prismatic_scara_link_joint", "base_gripper_link_joint",
    "left_gripper_link_joint", "right_gripper_link_joint"
]
wheel_names = [
    "wheel_link_joint", "wheel.001_link_joint", "wheel.002_link_joint",
    "wheel.003_link_joint", "wheel.004_link_joint", "wheel.005_link_joint"
]

# --- LECTURA DEL ROSBAG ---
reader = rosbag2_py.SequentialReader()
storage_options = rosbag2_py.StorageOptions(uri=bag_directory, storage_id="mcap")
converter_options = rosbag2_py.ConverterOptions("", "")
reader.open(storage_options, converter_options)

joint_times_arm, joint_efforts_arm = [], []
joint_times_wheels, joint_positions_wheels = [], []
imu_times, imu_accel = [], []

while reader.has_next():
    (topic, data, t) = reader.read_next()
    time_sec = t / 1e9
    
    if topic == '/joint_states':
        msg = deserialize_message(data, get_message('sensor_msgs/msg/JointState'))
        arm_row = [abs(msg.effort[msg.name.index(n)]) if n in msg.name else 0.0 for n in arm_joint_names]
        joint_times_arm.append(time_sec)
        joint_efforts_arm.append(arm_row)
        wheel_row = [msg.position[msg.name.index(n)] if n in msg.name else np.nan for n in wheel_names]
        joint_times_wheels.append(time_sec)
        joint_positions_wheels.append(wheel_row)
        
    elif topic == '/imu/data':
        msg = deserialize_message(data, get_message('sensor_msgs/msg/Imu'))
        imu_times.append(time_sec)
        imu_accel.append([msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z])

# Procesamiento NumPy y normalización de tiempo
t_arm = np.array(joint_times_arm) - (joint_times_arm[0] if joint_times_arm else 0)
data_arm = np.array(joint_efforts_arm)
t_wheels = np.array(joint_times_wheels) - (joint_times_wheels[0] if joint_times_wheels else 0)
data_wheels = np.array(joint_positions_wheels)
t_imu = np.array(imu_times) - (imu_times[0] if imu_times else 0)
data_imu = np.array(imu_accel)

# --- GENERACIÓN DE GRÁFICAS ---
plt.style.use('seaborn-v0_8-whitegrid')

# 1. Brazo (G-Parcial)
plt.figure(figsize=(10, 6))
for i, joint in enumerate(arm_joint_names):
    # Selecciona el color de la lista maestra usando el índice i
    color_actual = mis_colores[i % len(mis_colores)]
    plt.plot(t_arm, data_arm[:, i], label=joint, color=color_actual, linewidth=1.5)
plt.title('Gasto vs Tiempo')
plt.legend()

# 2. Ruedas (Posición)
plt.figure(figsize=(10, 6))
for i, wheel in enumerate(wheel_names):
    # También usa la lista maestra
    color_actual = mis_colores[i % len(mis_colores)]
    plt.plot(t_wheels, data_wheels[:, i], label=wheel, color=color_actual, linewidth=1.5)
plt.title('Posición ruedas vs Tiempo')
plt.legend()

# 3. IMU (Aceleración)
plt.figure(figsize=(10, 6))
labels = ['X Axis', 'Y Axis', 'Z Axis']
for i in range(3):
    color_actual = mis_colores[i % len(mis_colores)]
    plt.plot(t_imu, data_imu[:, i], label=labels[i], color=color_actual, linewidth=1.2)
plt.title('Aceleración vs Tiempo')
plt.legend()

plt.show()