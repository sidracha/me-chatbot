me-chatbot
==========

http://sidsail.ddns.net

I fine-tuned a llama 7B model with ~25,000 of my messages that I scraped from discord.

Using qlora 4-bit quantization for fine tuning and inference

Took ~40 hours on a single 2070 Super 8gb card running on a headless ubuntu server

Deployed with flask

However, the chatbot is really afwul and does not understand what it is saying or what you are saying. I will to to tweak the prompt and see if it responds better.


The data was in alpaca format: 

.. code-block::text 
{

 "Instruction": "Respond to this message sent by a human",
 
 "Input": <message I responded to>,
 
 "Output": <my message>

}
