import telebot
import os
from flask import Flask, request, render_template_string
from g4f import Provider, models
from langchain.llms.base import LLM
from langchain_g4f import G4FLLM
from modes import modes
from langchain.prompts import (
    SystemMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

from revChatGPT.V1 import Chatbot
chatbot = Chatbot(config={
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJwYXRyaXppb21lZGxleUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZX0sImh0dHBzOi8vYXBpLm9wZW5haS5jb20vYXV0aCI6eyJwb2lkIjoib3JnLXRqV1REaXk5UENlcW9uOWplbFZNbnNENyIsInVzZXJfaWQiOiJ1c2VyLU13aktPUUhrdURITnVneEdHVHdrQ05hbiJ9LCJpc3MiOiJodHRwczovL2F1dGgwLm9wZW5haS5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQwMzk4MTk1NjQ3MDA1NzQ3ODMiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzA4NTk2NjMyLCJleHAiOjE3MDk0NjA2MzIsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb3JnYW5pemF0aW9uLndyaXRlIG9mZmxpbmVfYWNjZXNzIn0.SRNWfOVbjNxOja7HcqGmNBk89RPafrKBB06d2F2nCflfBoXvoTeUMxk__cYAxG-GkJb-rMbxolFGOyVyxIF_dcz_Yf6QE6YiLFyYR8SxmmMq0Bh_DfT41O5UN_Vq6NAvU07uPBOssDvsQfkKolhRdp_tUYaMZl-QGuQtLt6Lyo9nApqGZCZF3nAIX8GSqIxGWtpSn0zugxlkdoJRlHCtJj-zxTh0ludBOl9pjS4nq7am05yDeTs6XRIkx8RMQz5qZhL8iD8WWoEXx7jnv0wPZ7XUpPzL42gvQ5y1mdpQq58BsF0olmEjLUJjWm4cQ9mlqyTRCyaihMQfz2c3-Cmlag"
})
prompt = "how many beaches does portugal have?"
response = ""
for data in chatbot.ask(
  prompt
):
    response = data["message"]
print(response)
