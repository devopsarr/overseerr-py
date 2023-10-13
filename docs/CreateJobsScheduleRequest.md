# CreateJobsScheduleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | **str** |  | [optional] 

## Example

```python
from overseerr.models.create_jobs_schedule_request import CreateJobsScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobsScheduleRequest from a JSON string
create_jobs_schedule_request_instance = CreateJobsScheduleRequest.from_json(json)
# print the JSON string representation of the object
print CreateJobsScheduleRequest.to_json()

# convert the object into a dict
create_jobs_schedule_request_dict = create_jobs_schedule_request_instance.to_dict()
# create an instance of CreateJobsScheduleRequest from a dict
create_jobs_schedule_request_form_dict = create_jobs_schedule_request.from_dict(create_jobs_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


