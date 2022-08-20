from src.resources import hparams
from src.trainer import trainer
from typing import Union
from fastapi import FastAPI
import uvicorn
import torch

infer_path="checkpoint/envibert_cased/checkpoint_envibert_cased_2.pt"
cuda = 'cpu'
trainer = trainer(cuda="cpu", mode="infer", infer_path=infer_path, bert_type="envibert_uncased")        
app = FastAPI()
@app.get("/infer")
def infer(raw_text:Union[str, None] = None):
    raw_text, out_text , inp_text = trainer.do_restore(raw_text=raw_text)

    return {
        "raw_text":raw_text,
        "inp_text":inp_text,
        "out_text": out_text
        }
    
if __name__ == '__main__':
    
    uvicorn.run(app, host="127.0.0.1", port=8000)

