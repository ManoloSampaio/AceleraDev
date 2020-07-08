from rest_framework.response import Response
from rest_framework.decorators import api_view

def AnswerFrequency(answer_list): 
    count = {} 
    solution_list = []
    for i in answer_list: 
        count[i] = count.get(i, 0) + 1
    
    sorted_list = sorted(count, key=count.get,reverse=True)
    
    for X in sorted_list:
        for i in range(0,count[X]):
            solution_list.append(X)
    
    return solution_list

@api_view(['POST'])
def lambda_function(request):
    question_data = request.data.get('question')
    question_data = sorted(question_data)
    solution_list = AnswerFrequency(question_data)
    answer = {'solution':solution_list}
    return Response(data=answer)
