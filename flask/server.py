from flask import Flask, request, jsonify
import dialogflow
import os
import json

# 구글 클라우드 API와 인증하기 위해 사용
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="***************.json"

def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))


    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
       
    return response.query_result.fulfillment_text

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #jsonify encoding 문제 해결


@app.route("/")
def root():
    return 'hello world'

# root 그냥 get으로 parameter 없이 한 것
@app.route("/api/text")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    text_list = ['노인복지']
    fulfillment = {'text':''}
    dialogflow_response = detect_intent_texts('', '', text_list, 'ko')
    fulfillment['text'] = dialogflow_response
    json_fulfillment = json.dumps(fulfillment, ensure_ascii=False)

    return jsonify(fulfillment)

# GET parameter 읽는 방식
@app.route('/api/dialogflow')
def dialogflowResponse():
    question = str(request.args.get('question'))
    text_list = []
    text_list.append(question)
    fulfillment = {'text':''}
    dialogflow_response = detect_intent_texts('', '', text_list, 'ko')
    fulfillment['text'] = dialogflow_response
    json_fulfillment = json.dumps(fulfillment, ensure_ascii=False)

    return jsonify(fulfillment)

# POST sample 예제 이 방식 아직 구현 x 
@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    json = request.get_json()
    print(json)
    if len(json['text']) == 0:
        return jsonify({'error': 'invalid input'})

    return jsonify({'you sent this': json['text']})
    
# running web app in local machine
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)