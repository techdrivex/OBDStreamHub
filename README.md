# OBDStreamHub

![Project Status](https://img.shields.io/badge/status-in%20development-orange)  
![License](https://img.shields.io/badge/license-MIT-blue)  
Live sharing of OBD-I and OBD-II commands remotely from a running vehicle.

## Overview

**OBDStreamHub** is an open-source project that captures and streams On-Board Diagnostics (OBD) data in real-time from a vehicle to a remote endpoint. It supports both OBD-I (with custom logic TBD) and OBD-II protocols, making it versatile for modern and legacy vehicles. Ideal for automotive enthusiasts, developers, and diagnostics applications, OBDStreamHub delivers fast, low-latency data streaming.

### Tech Stack
- **Backend**: Python 3.11 with FastAPI (async web framework) and WebSockets.
- **OBD Library**: `python-obd` for OBD-II; placeholder for OBD-I logic.
- **Data Transport**: WebSockets for real-time streaming.
- **Deployment**: Docker for portability.

## Features

- **Real-Time Streaming**: Live OBD data (e.g., speed, RPM, throttle) over WebSockets.
- **OBD-I & OBD-II Support**: Works with OBD-II now; OBD-I support in progress.
- **High Performance**: Asynchronous design for minimal latency.
- **Open Source**: Licensed under MIT—fork, modify, and contribute freely.

## Getting Started

### Prerequisites
- OBD-I or OBD-II compatible vehicle.
- OBD adapter (e.g., ELM327 for OBD-II via USB/Bluetooth/Wi-Fi).
- Python 3.11+.
- Docker (optional).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/techdrivex/OBDStreamHub.git
   cd OBDStreamHub
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your OBD adapter in `config.json`:
   ```json
   {
       "port": "/dev/ttyUSB0",  // e.g., COM3 on Windows
       "protocol": "AUTO",      // OBD-II protocol
       "is_obd1": false         // Set true for OBD-I (custom logic needed)
   }
   ```

### Usage
1. Start the server:
   ```bash
   python main.py
   ```
2. Connect to the WebSocket stream at `ws://localhost:8000/ws` using a client (e.g., `wscat`):
   ```bash
   wscat -c ws://localhost:8000/ws
   ```
3. View live OBD-II data (e.g., speed, RPM, throttle). OBD-I support requires custom implementation.

#### Docker Option
```bash
docker build -t obdstreamhub .
docker run -p 8000:8000 obdstreamhub
```

### Example Output
```json
{
    "timestamp": 1711139200.123,
    "mode": "OBD-II",
    "data": {
        "speed": "60 km/h",
        "rpm": "2500 rpm",
        "throttle_position": "25 %"
    }
}
```

## Project Status
- **In Development**: OBD-II streaming is functional; OBD-I support is a placeholder.
- **Planned Features**:
  - Full OBD-I protocol support (e.g., ALDL, PWM).
  - Web dashboard for data visualization.
  - Authentication for secure remote access.
- Track progress in the [Issues](https://github.com/techdrivex/OBDStreamHub/issues) tab.

## Contributing
Contributions are welcome! Fork the repo, make changes, and submit a pull request. For major features, open an issue to discuss first.

### Notes for Contributors
- OBD-I support requires custom parsing logic per manufacturer protocol.
- Add more OBD-II commands via `obd.commands` in `obd_handler.py`.

## License
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

## Contact
- GitHub: [techdrivex](https://github.com/techdrivex)
