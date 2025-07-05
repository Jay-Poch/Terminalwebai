from openai import OpenAI
from source import definitions
def run(querry: definitions.config):
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
    model="moonshotai/kimi-dev-72b:free",
    messages=[
    {
      "role": "user",
      "content": querry.promt
            }
    ]
    )
    response = str(completion.choices[0].message.content)
   # counter: int = 0
 #   for x in response:
        
    #    counter =+ 1
    return response
