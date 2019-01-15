#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import sys
import com.xhaus.jyson.JysonCodec as json

HTTP_SUCCESS = [200, 201]

result=[]

# Leankit card API Vairables for URL
account_name = 'lvvwd'
board_id = '648241354'
lane_id = '667141327'
card_id = releaseVariables['LeanKitCardID']
position = '0'
content =''

access_token = 'd027fa4ef8c085b0340bf9fc4d49787908e386a0a66259de340c0130169dfba45e5552afe9dabbd9c1de3a3cf45e59d034dd0dbaaf32a95cef540d45b0d86165'
headers = { "Accept" : "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + access_token }

server_base_url = "https://%s.leankit.com" % ( account_name )
service_account_username =  None
service_account_password =  None
# Build the URL for the call to the endpoint
server_base_url = "https://%s.leankit.com" % ( account_name )
URI = '/kanban/api/board/%s/MoveCard/%s/lane/%s/position/%s?token=%s'   % ( board_id, card_id, lane_id, position, access_token )
URL = "%s%s" % ( server_base_url, URI )

print "******"
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
    print data
else:
    response.errorDump()
    sys.exit(1)
