# Home Assistant Door Magnetic Sensor

Lets you connect an existing magnetic door sensor to Home Assistant. This server will
constantly check the state of the door and make it available to query via an API that is
compatible with Home Assistant.


# Requirements
To develop this template on your computer, you need:

- Python 3
- Flask (`pip3 install flask`)

# Setting up on your Pi
Setting it up on a fresh install of Raspbian is supported in the provided install script. Simply `cd` to the root of this repository on your Raspberry Pi and run the `install.sh`.

# Connect to Home Assistant
Add this to the configuration file of your Home Assistant:

```yaml
binary_sensor:
  - platform: rest
    resource: http://IP_ADDRESS/state
    name: Door
    value_template: '{{ value_json.is_active }}'
    headers:
      Content-Type: application/json
    verify_ssl: true
    device_class: door
```