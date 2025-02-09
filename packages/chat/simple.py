import os, requests as req
MODEL ="llama3.1:8b"


def main(args):
    #get secrets
    host = args.get("OLLAMA_HOST",os.getenv("OLLAMA_HOSTS"))
    auth = args.get("AUTH",os.getenv("AUTH"))
    base = f"https://{auth}@{host}"
    print(base)

    #talking with the model
    out = f"Welcome to {MODEL}"
    inp = args.get("input")

    if inp:
        #preparing request
        msg = {"model": MODEL,"prompt":inp,"stream": False}
        url = f"{base}/api/generate"

        #making request
        import requests as req
        res = req.post(url,json=msg).json()
        out = res.get("response","error")

    return {"body" : {"output" : out}}


    