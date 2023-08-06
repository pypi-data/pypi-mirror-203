# Finometer Data Logger

This project is intended to use an Arduino as a data logger for a Finometer Medical System.
The project consists of two parts: `finometer_logger.ino` and `logger.py`.

## finometer_logger.ino

`finometer_logger.ino` is a C++ script designed to be loaded on to an Arduino board to interact with the analogue (BNC) outputs of the Finometer.
The pins should be set up as follows:

- Finometer Analogue Output 1 -> Arduino Pin A1 (Finger cuff pressure)
- Finometer Analogue Output 2 -> Arduino Pin A2 (Hydrostatic finger height)
- Finometer Analogue Output 3 -> Arduino Pin A3 (Arm cuff pressure)
- Finometer Analogue Output 4 -> Arduino Pin A4 (Finger plethysmogram)

These output values are sent via a serial connection along with the elapsed time since the Arduino started.

## logger.py

The `logger.py` script is a simple python script that logs the values read from a serial port to an output csv file.
If no name is provided the output file is named `output-` followed by the current date an time.
