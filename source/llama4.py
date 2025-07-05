from source import definitions
from openai import OpenAI
def run(querry: definitions.config) -> str:
  print('Promt: ' + querry.promt)
  client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=querry.key
)

  completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="mistralai/mistral-small-3.2-24b-instruct",
  messages=[
    {
      "role": "user",
        "content": [
          {
           "type": "text",
           "text": querry.promt
          }
        ]
      }
    ]
  )
  print('Response: ' + str(completion.choices[0].message.content))

  return str(completion.choices[0].message.content)
