import telebot
import os
import asyncio, json
from flask import Flask, request, render_template_string
from langchain.llms.base import LLM
from EdgeGPT.EdgeUtils import Query






q = Query("Hello")
print(q)
