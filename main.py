# main.py
from fastapi import FastAPI, HTTPException
from models import SearchRequest, SearchResponse
from praw_handler import search_subreddit

app = FastAPI()

@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    try:
        
        print(request.subreddit, request.keyword, request.sort, request.time_filter, request.limit)
        results = search_subreddit(request.subreddit, request.keyword, request.sort, request.time_filter, request.limit)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
