from datetime import datetime
## Call records used in this question.
records = [
    {
    'source': '48-996355555', 
    'destination': '48-666666666', 
    'end': 1564610974, 
    'start': 1564610674},
    {
    'source': '41-885633788', 
    'destination': '41-886383097', 
    'end': 1564506121, 
    'start': 1564504821
    },
    {
    'source': '48-996383697', 
    'destination': '41-886383097', 
    'end': 1564630198, 
    'start': 1564629838
    },
    {
    'source': '48-999999999', 
    'destination': '41-885633788',
    'end': 1564697158,
    'start': 1564696258
    },
    {
    'source': '41-833333333', 
    'destination': '41-885633788',
    'end': 1564707276,
    'start': 1564704317
    },
    {
    'source': '41-886383097',
    'destination': '48-996384099', 
    'end': 1564505621, 
    'start': 1564504821
    },
    {
    'source': '48-999999999', 
    'destination': '48-996383697', 
    'end': 1564505721, 
    'start': 1564504821
    },
    {
    'source': '41-885633788', 
    'destination': '48-996384099', 
    'end': 1564505721, 
    'start': 1564504821
    },
    {
    'source': '48-996355555', 
    'destination': '48-996383697', 
    'end': 1564505821, 
    'start': 1564504821
    },
    {
    'source': '48-999999999', 
    'destination': '41-886383097', 
    'end': 1564610750, 
    'start': 1564610150
    },
    {
    'source': '48-996383697', 
    'destination': '41-885633788', 
    'end': 1564505021, 
    'start': 1564504821
    },
    {
    'source': '48-996383697', 
    'destination': '41-885633788', 
    'end': 1564627800, 
    'start': 1564626000
    }
]

def organize_answer(source_dictonary):
	answer = [] 
	# Sort the dictionary in the reverse direction,
	# sorted returns a list of tuples.
	sorted_source_dictonary = sorted(source_dictonary.items(), key=lambda x: x[1],reverse=True)
	# Creates the dictionary list.
	for touple_element in sorted_source_dictonary:
		answer.append({'source':touple_element[0],'total':float("{:.2f}".format(touple_element[1]))})
	return answer
def classify_by_phone_number(report):
	CONSTANT_TAX = 0.36 # Constant tax per call.
	DAY_TAX =  0.09 # Tax charged from 6 to 22 hours. 
	source_cost ={} # A dictionary that groups the source and its cumulative call costs.
	for call_record in report:
		# Gets the call source.
		call_source = call_record['source']
		
		# Gets the time the call starts and ends,
		# it converts from timestamp to datetime object.
		begin_time_in_timestamp = call_record['start']
		end_time_in_timestamp = call_record['end']
		begin = datetime.fromtimestamp(begin_time_in_timestamp)
		end = datetime.fromtimestamp(end_time_in_timestamp)
		
		# Calculates the time difference,
		# it creates a delta datetime object.
		time_delta = end - begin # time difference.
		begin_hour = begin.hour # the time the call starts.

		# Checks whether the tax is applicable,
		# and calculates the cost of the call.
		cost = CONSTANT_TAX
		if begin_hour>=6 and begin_hour<=22:
			difference_minutes =(time_delta.seconds//60)%60
			cost = cost+difference_minutes*DAY_TAX
		
		# Make sure the source is already in the dictionary,
		# to increase its call costs
		# If not in the dictionary, 
		#create a key with the cost of the call.
		if call_source in source_cost:
			source_cost[call_source] = source_cost[call_source]+cost
		else:
			source_cost[call_source] = cost
	# The answer of the chalenge.
	answer = organize_answer(source_cost)
	return answer
print(classify_by_phone_number(records))
