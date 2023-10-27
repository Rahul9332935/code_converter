import requests
import os

api_key = os.environ['KEY']#  Replace with your

endpoint = "https://api.openai.com/v1/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
query="payar"

def codeDebuger(code):

  data = {
      "model": "text-davinci-002",  # Choose a suitable GPT-3 model
      "prompt": f"You are a skilled code debugger. Please review the following code {code} and identify and fix any issues. Explain each problem and then fix clearly.",
      "max_tokens": 250
  }

  response = requests.post(endpoint, headers=headers, json=data)

  if response.status_code == 200:
      response_json = response.json()
      if 'choices' in response_json and len(response_json['choices']) > 0:
          generated_text = response_json['choices']
          return generated_text[0] 
      else:
          return "No text generated in response."
  else:
    return ("Error:", response.text)



def code_quality_checker(code):
  data = {
      "model": "text-davinci-002",  # Choose a suitable GPT-3 model
      "prompt": f"You are a skilled code quality checker. Please review the following code {code} and identify any potential issues. Explain each issue and then fix clearly.",
      "max_tokens": 250
  }
  response = requests.post(endpoint, headers=headers, json=data)
  if response.status_code == 200:
    response_json = response.json()
    if 'choices' in response_json and len(response_json['choices']) > 0:
        generated_text = response_json['choices']
        return generated_text[0] 
    else:
        return "No text generated in response."
  else:
    return ("Error:", response.text)


def code_converter(code, lang):
  data = {
      "model": "text-davinci-002",  # Choose a suitable GPT-3 model
      "prompt": f"You are a skilled code converter. Please convert the following code {code} to {lang}. don't miss any line of code. you just have to convert whatever code given to you don't add extra info.",
      "max_tokens": 250
  }
  response = requests.post(endpoint, headers=headers, json=data)
  if response.status_code == 200:
    response_json = response.json()
    if 'choices' in response_json and len(response_json['choices']) > 0:
      generated_text = response_json['choices']
      return generated_text[0]
    else:
      return "No text generated in response."
  else:
    return ("Error:", response.text)






# code= """
# public static void bubbleSort(int[] arr) {
#         int n = arr.length;
#         for (int i = 0; i < n - 1; i++) {
#             for (int j = 0; j < n - i - 1; j++) {
#                 if (arr[j] > arr[j + 1]) {
#                     // Swap arr[j] and arr[j+1]
#                     int temp = arr[j];
#                     arr[j] = arr[j + 1];
#                     arr[j + 1] = temp;
#                 }
#             }
#         }
#     }

# """
# lang = 'javascript'

# da= code_converter(code, lang)
# print(da)