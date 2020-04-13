





# records = {
#     'Records': [{
#         'eventVersion': '2.1',
#         'eventSource': 'aws:s3',
#         'awsRegion': 'ap-southeast-1',
#         'eventTime': '2020-04-11T05:56:23.848Z',
#         'eventName': 'ObjectCreated:Put',
#         'userIdentity': {
#             'principalId': 'AWS:AIDA5V5WGNMDHDBJ3OVTT'
#         },
#         'requestParameters': {
#             'sourceIPAddress': '139.5.134.122'
#         },
#         'responseElements': {
#             'x-amz-request-id': 'BD826B45CC42A68E',
#             'x-amz-id-2': 'P1Jd2wXat1kFAG1zqsoeroHlb+ZrH+HbsHVM1gbISKk+jml77X/1bYkntGy64fbRA1MqpkQvNwnWUgJJIznzbNbWwE2tQi2J'
#         },
#         's3': {
#             's3SchemaVersion': '1.0',
#             'configurationId': 'read jobs url ',
#             'bucket': {
#                 'name': 'jobstext',
#                 'ownerIdentity': {
#                     'principalId': 'A36NS3RMO1UTEA'
#                 },
#                 'arn': 'arn:aws:s3:::jobstext'
#             },
#             'object': {
#                 'key': 'Test+9.txt',
#                 'size': 543,
#                 'eTag': '6deb9f3768e0e569043ce882b77b020d',
#                 'sequencer': '005E915C09119234DE'
#             }
#         }
#     }]
# }
#
#
# def lambda_handler(event, context):
#     for records in event['Records']:
#         x = records["s3"]["object"]["key"]
#         print(x)
#
#
# lambda_handler(records, {})
