# Timekit API Integration

This package can be used to integration Timekit APIs with your project.

## Installation

Run the following to install

```python
pip install timekit
```

## Usage

```python
from timekit import TimekitAPIv2

client = TimekitAPIv2(api_key="<you_api_key>")
response = client.resource.list()
# the response over here is response from timekit api
```