from openai import OpenAI

OPEN_AI_KEY = "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"


print("Welcome")
print("Let's ask ChatGPT something within our code:")
question=input("Ask a question:")





client=OpenAI(api_key=OPEN_AI_KEY)

completion=client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
    {"role": "system", "content": "You are a friendly Canadian and an aristocrat from the Shakespeare era.All your responses should incorporate Canadian slang and Shakespeare type language"},
    {"role": "user", "content": question}
  ]
)
print(completion.choices[0].message.content)




