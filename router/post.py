from fastapi import FastAPI ,HTTPException,APIRouter
from schemas import Post,Comment
from typing import List

app = FastAPI()
router = APIRouter(
    prefix="/posts",
    tags=["post"],
)
posts = []
post_id_counter = 1
comment_id_counter = 1

@app.post("/", response_model=Post)
def create_post(post: Post):
    global post_id_counter
    post.id = post_id_counter
    posts.append(post)
    post_id_counter += 1
    return post

@app.delete("/{post_id}")
def delete_post(post_id: int):
    global posts
    for index, post in enumerate(posts):
        if post.id == post_id:
            del posts[index]
            return {"message": "Post deleted successfully"}
    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/", response_model=List[Post])
def get_posts():
    return posts

@app.post("/{post_id}/comments/", response_model=Comment)
def create_comment(post_id: int, comment: Comment):
    global comment_id_counter
    for post in posts:
        if post.id == post_id:
            comment.id = comment_id_counter
            post.comments.append(comment)
            comment_id_counter += 1
            return comment
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/{post_id}/comments/{comment_id}")
def delete_comment(post_id: int, comment_id: int):
    for post in posts:
        if post.id == post_id:
            for index, comment in enumerate(post.comments):
                if comment.id == comment_id:
                    del post.comments[index]
                    return {"message": "Comment deleted successfully"}
            raise HTTPException(status_code=404, detail="Comment not found")
    raise HTTPException(status_code=404, detail="Post not found")
