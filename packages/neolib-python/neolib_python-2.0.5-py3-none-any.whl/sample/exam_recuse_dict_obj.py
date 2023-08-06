test_aa ={
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:Connect",
      "Resource": "arn:aws:iot:ap-southeast-2:086869036654:client/${iot:Connection.Thing.ThingName}"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iot:Subscribe",
        "iot:Receive",
        "iot:Publish"
      ],
      "Resource": "*"
    }
  ]
}



def recurse_key_value(test_aa):
	if type(test_aa) == dict:
		for key,val in test_aa.items():
			recurse_key_value(val)
			pass
		pass
	elif type(test_aa) == list:
		for val in test_aa:
			recurse_key_value(val)

		pass
	print(test_aa)
recurse_key_value(test_aa)