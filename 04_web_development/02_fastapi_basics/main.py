from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database
import cache
import mq

app = FastAPI()

# 定义 Web 接口
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    # 先从缓存中获取数据
    cached_item = cache.get_from_cache(f"item:{item_id}")
    if cached_item:
        return {"id": item_id, "name": cached_item.decode()}

    # 如果缓存中没有数据，则从数据库中查询
    item = db.query(database.Item).filter(database.Item.id == item_id).first()
    if item:
        # 将数据存入缓存
        cache.set_in_cache(f"item:{item_id}", item.name)
        # 发送消息到消息队列
        mq.send_message(f"Item {item_id} was accessed")
        return {"id": item.id, "name": item.name}
    return {"message": "Item not found"}

@app.post("/items/{item_id}")
def set_item(item_id: int, item_name: str, db: Session = Depends(database.get_db)):
    try:
        # 将数据存入数据库
        item = database.Item(id=item_id, name=item_name)
        db.add(item)
        db.commit()
        # 将数据存入缓存
        cache.set_in_cache(f"item:{item_id}", item_name)
        return {"id": item.id, "name": item.name}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
# 启动应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)