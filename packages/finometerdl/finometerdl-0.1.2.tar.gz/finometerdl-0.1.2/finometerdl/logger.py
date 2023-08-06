# Python imports
import serial
from datetime import datetime

def logger(source="/dev/ttyACM0", dest=None, encoding='utf-8'):
    """Logs serial readings

    Args:
        source (string, optional) : Source port of the serial device.
            Defaults to "/dev/ttyACM0".
        dest (string, optional) : Destination file to write serial output to.
            If None, will use the format 'output-DATETIME.csv' where DATETIME
            is the current date and time.
            Defaults to None.
        encoding (string, optional) : Encoding of serial device. 
            Defaults to 'utf-8'.

    Returns:
        return val (bool) : True if successful. False otherwise.
    """

    # Connects to source
    with serial.Serial(source, timeout=10) as ser:
        print(f"Connected to:\n{ser}")

        # Creates file
        if dest is None:
            dest = f"output-{datetime.now().strftime('%y-%m-%d_%H-%M-%S')}.csv"
        print(f"Writing to {dest}")

        # Loops over reading serial input
        cont = True
        with open(dest, "a") as f:
            while cont:
                try:
                    line = ser.readline().decode(encoding)
                    print(line)
                    f.write(line)
                except UnicodeDecodeError:
                    pass
                except KeyboardInterrupt:
                    break
    print("Finished reading data.")
    return True

if __name__ == "__main__":
    logger()
