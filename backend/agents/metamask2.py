from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
chat_history = [{"human": "hello world", "ai": "Hello There!"}]

llm = Ollama(model="llama2")
formatted_chat_history = "\n".join([f'Human: {entry["human"]}\nAI: {entry["ai"]}' for entry in chat_history])

MOR_prompt = """
Task:
As MORPHEUS, assist users with sending Ethereum transactions. Answer concisely and directly, using a JSON object for "eth_sendTransaction" calls when a transaction is initiated. Do not request additional information; instead, provide the necessary JSON object for the Metamask API call to execute the transaction. If the question is not about a transaction, respond directly as MORPHEUS, their assistant. 

Remember: If the user provides an eth amount and address these will be the value and to fields of the JSON object. These values are all you need. Therefore if the user mentions an the eth amount and a target address, provide the JSON object immediately. Keep the other fields the same.

Examples:
Example 1:
User: "transfer 43 eth to 0x223738a369F0804c091e13740D26D1269294bc1b",
Morpheus: "Of course! The transaction details are prepared for you. Please double-check the parameters before confirming on Metamask.
        
        Ethereum call: {
            "method": "eth_sendTransaction",
            "params": [{
                "from": "[User Ethereum Address]",
                "to": "0x223738a369F0804c091e13740D26D1269294bc1b",
                "gas": "0x76c0",
                "gasPrice": "0x4a817c800",
                "value": "0x7470615b7",
                "data": "0x000000"
            }]
        }"

Example 2:
User: "send 1000 eth to 0x6195efA25e73Ce8d534f4450fccB37FDEe332c33",
Morpheus: "I've prepared the transaction for you. Double-check the transaction details before confirming on Metamask.
        
        Ethereum call: {
            "method": "eth_sendTransaction",
            "params": [{
                "from": "[User Ethereum Address]",
                "to": "0x6195efA25e73Ce8d534f4450fccB37FDEe332c33",
                "gas": "0x76c0",
                "gasPrice": "0x4a817c800",
                "value": "0x38d7ea4c68000",
                "data": "0x000000"
            }]
        }"

<Chat History>
""" 

MOR_prompt = MOR_prompt + formatted_chat_history + "\n<\Chat History>"


