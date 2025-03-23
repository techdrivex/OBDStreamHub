import obd
import time
import json

class OBDHandler:
    def __init__(self, config):
        self.port = config.get("port", "/dev/ttyUSB0")  # Default for USB adapters
        self.protocol = config.get("protocol", "AUTO")  # OBD-II protocol
        self.is_obd1 = config.get("is_obd1", False)    # Toggle OBD-I mode
        self.connection = None
        self.connect()

    def connect(self):
        """Establish connection to OBD adapter."""
        try:
            if self.is_obd1:
                # Placeholder for OBD-I connection (custom logic needed)
                print("OBD-I mode: Custom connection logic not implemented yet.")
                self.connection = None  # Replace with OBD-I adapter logic
            else:
                # OBD-II connection using python-OBD
                self.connection = obd.OBD(self.port, protocol=self.protocol, baudrate=38400)
                if self.connection.is_connected():
                    print("Connected to OBD-II adapter.")
                else:
                    print("Failed to connect to OBD-II adapter.")
        except Exception as e:
            print(f"Connection error: {e}")

    def get_live_data(self):
        """Fetch live OBD data (OBD-II or OBD-I)."""
        if not self.connection:
            return {"error": "No OBD connection"}

        if self.is_obd1:
            # Placeholder for OBD-I data retrieval
            # Replace with manufacturer-specific protocol parsing (e.g., ALDL, PWM)
            return {
                "timestamp": time.time(),
                "mode": "OBD-I",
                "data": {"example_param": "N/A"}  # Custom OBD-I data here
            }
        else:
            # OBD-II data retrieval
            speed = self.connection.query(obd.commands.SPEED).value
            rpm = self.connection.query(obd.commands.RPM).value
            throttle = self.connection.query(obd.commands.THROTTLE_POS).value

            return {
                "timestamp": time.time(),
                "mode": "OBD-II",
                "data": {
                    "speed": str(speed) if speed else "N/A",
                    "rpm": str(rpm) if rpm else "N/A",
                    "throttle_position": str(throttle) if throttle else "N/A"
                }
            }

    def close(self):
        """Close OBD connection."""
        if self.connection:
            self.connection.close()
            print("OBD connection closed.")