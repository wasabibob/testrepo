#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Request format
# https://{accountname}.leankit.com/kanban/api/board/{boardId}/AddCard/lane/{laneId}/position/{position}
# {
#    "Title": "My New Card",
#    "Description": "New Description",
#    "TypeId": 101304,
#    "Priority": 0,
#    "Size": 2,
#    "IsBlocked": false,
#    "BlockReason": "",
#    "DueDate": "01/01/2020",
#    "ExternalSystemName": "Tracking",
#    "ExternalSystemUrl": "http://ourcompanycms.com/1234",
#    "Tags": "small,UI",
#    "ClassOfServiceId": 123222,
#    "ExternalCardID": "DSA-111",
#    "AssignedUserIds": [111,1112,2211]
# }

import sys
from urllib import urlencode
import com.xhaus.jyson.JysonCodec as json
import java.text.SimpleDateFormat as sdf

HTTP_SUCCESS = [200, 201]

result=[]

# Leankit card API Vairables for URL
account_name = 'lvvwd'
board_id = '648241354'
lane_id = '667141329'
type_id = '648315113'
position = '9999'
access_token = 'd027fa4ef8c085b0340bf9fc4d49787908e386a0a66259de340c0130169dfba45e5552afe9dabbd9c1de3a3cf45e59d034dd0dbaaf32a95cef540d45b0d86165'
headers = { "Accept" : "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + access_token }

server_base_url = "https://%s.leankit.com" % ( account_name )
service_account_username =  None
service_account_password =  None
# Build the URL for the call to the endpoint
server_base_url = "https://%s.leankit.com" % ( account_name )
URI = '/kanban/api/board/%s/AddCard/lane/%s/position/%s?token=%s'   % ( board_id, lane_id, position, access_token )
URL = "%s%s" % ( server_base_url, URI )
release_url = '${release.url}'
deployment_datetime = releaseVariables['LeankitDeploymentDatetime']
deployment_date = sdf("MM/dd/yyyy").format(releaseVariables['LeankitDeploymentDatetime'])
deployment_time = sdf("HH:mm:ss").format(releaseVariables['LeankitDeploymentDatetime'])
extra_title_mesg = releaseVariables['LeankitExtraTitleMessage']
items_for_deployment = releaseVariables['LeankitItemsForDeployment']
description_change_management = releaseVariables['LeankitDescriptionChangeManagement']
users_change_management_notification = releaseVariables['LeankitUsersChangeManagementNotification']
point_of_contact = releaseVariables['LeankitPointOfContact']
requestor = releaseVariables['LeankitRequestor']
schemas = releaseVariables['LeankitSchemas']
customer_impact = releaseVariables['LeankitCustomerImpact']

# Variables for the content/body of the message
card_title = "Testing XL ReleaseR"
card_description = "Requesting Production Deploy for App XXXX"
# Body of the http call to the server
content = {
            "Title": "{} {} - {} {}".format(
                deployment_date, deployment_time, schemas, extra_title_mesg
            ),
            "Description": """
            <b>Deployment Date</b>: {}<br>
            <b>Deployment Time</b>: {}<br>
            <b>Items for Deployment</b>:<br>
            {}<br>
            <b>Description for IT Change Management Notification</b>:<br>
            {}<br>
            <b>Users to be included on the IT Change Management notification</b>:<br>
            {}<br>
            <b>Point of Contact</b>: {}<br>
            <b>Requester</b>: {}<br>
            <b>Schemas</b>: {}<br>
            <b>Customer Impact</b>: {}<br>
            """.format(
                deployment_date, deployment_time, items_for_deployment, description_change_management,
                users_change_management_notification, point_of_contact, requestor, schemas,
                customer_impact
            ),
            "TypeId": 648315113,
            "Priority": 1 ,
            "Size": "",
            "IsBlocked": "false",
            "BlockReason": "",
            "DueDate": "{}".format(deployment_date),
            "ExternalSystemName": "XL Release",
            "ExternalSystemUrl": release_url,
            "Tags": "",
            "ClassOfServiceId": "",
            "ExternalCardID": "",
            "AssignedUserIds": []
          }


print "******"
print "This release's URL = %s"  % release_url
print "Server URL = %s%s"  % ( server_base_url, URI )
print "Headers = %s"  % headers
print "******"

request = HttpRequest( {'url':server_base_url, 'username':service_account_username, 'password':service_account_password} )
response = request.post( URI, body=json.dumps(content), headers=headers )

print "Response Status = %s" % response.status
print "Response Response = %s" % response.response
print "******"

if response.status in HTTP_SUCCESS:
    data = json.loads(response.response)
    releaseVariables['LeanKitCardID'] = data['ReplyData'][0]['CardId']
