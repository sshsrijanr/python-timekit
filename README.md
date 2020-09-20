# Timekit API Integration

This package can be used to integration Timekit APIs with your project.

## Installation

Run the following to install

```python
pip install timekit
```

## Usage

```python
from timekit import TimekitAPI

client = TimekitAPI(app_token="<you_api_key>")
response = client.resources.list()
# Response data from timekit
response.data
# Response status code from timekit
response.status
```

## Endpoints Available

```python
from timekit import TimekitAPI

client = TimekitAPI(app_token="<you_api_key>")
# NOTE: Endpoints for Apps
response = client.apps.invite(data)

# NOTE: Endpoints for Bookings
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

# NOTE: Endpoints for Projects
response = client.projects.create(data)
response = client.projects.list(limit, page, search)
response = client.projects.update(id, data)
response = client.projects.create(data)
response = client.projects.delete(id)
response = client.projects.add_resources(id, data)
response = client.projects.set_resources(id, data)
response = client.projects.remove_resources(id, resource_id)
response = client.projects.get_resources(id)


# NOTE: Endpoints for Resources
response = client.resources.create(data)
response = client.resources.list(limit, page, search)
response = client.resources.retrieve(id, dynamic_includes)
response = client.resources.update(id, data)
response = client.resources.delete(id)
response = client.resources.availability_constraints(id, data)

```
