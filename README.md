# python-timekit

This package can be used to integration Timekit APIs with your project.
for more information [click here](https://developers.timekit.io/reference#getting-started)

## Installation

Run the following to install

```python
pip install python_timekit
```

## Usage

```python
from timekit.client import TimekitAPI

client = TimekitAPI(app_token="<you_api_key>")
response = client.apps.get()
# Response data from timekit
response.data
# Response status code from timekit
response.status
```

## Endpoints Available

### App

```python
response = client.apps.get()
response = client.apps.invite(data)
```

for more information on App related APIs [click here](https://developers.timekit.io/reference#app)

### Booking

```python
response = client.bookings.create(data, dynamic_includes)
response = client.bookings.list(limit, page, dynamic_includes, search, order_by, sorted_by)
response = client.bookings.retrieve(id)
response = client.bookings.update_state(id, action)
response = client.bookings.update_meta(id, data)
response = client.bookings.create_in_bulk(data)
response = client.bookings.update_in_bulk(data)
response = client.bookings.groups.list(limit, page, search)
response = client.bookings.groups.retrieve(id)
response = client.bookings.delete(id)
```

for more information on Booking related APIs [click here](https://developers.timekit.io/reference#bookings)

### Project

```python
response = client.projects.create(data)
response = client.projects.list(limit, page, search)
response = client.projects.update(id, data)
response = client.projects.create(data)
response = client.projects.delete(id)
response = client.projects.add_resources(id, data)
response = client.projects.set_resources(id, data)
response = client.projects.remove_resources(id, resource_id)
response = client.projects.get_resources(id)
```

for more information on Project related APIs [click here](https://developers.timekit.io/reference#projects)

### Resource

```python
response = client.resources.create(data)
response = client.resources.list(limit, page, search)
response = client.resources.retrieve(id, dynamic_includes)
response = client.resources.update(id, data)
response = client.resources.delete(id)
response = client.resources.availability_constraints(id, data)
```

for more information on Resource related APIs [click here](https://developers.timekit.io/reference#resources)

### Availability

```python
response = client.availability.list(data)
```

for more information on Availability related APIs [click here](https://developers.timekit.io/reference#availability-v2)
