import random
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

CHAT_STORAGE = [
    "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
]

VIPBOY = MongoCli(random.choice(CHAT_STORAGE))
chatdb = VIPBOY.Anonymous
chatai = chatdb.Word.WordDb
storeai = VIPBOY.Anonymous.Word.NewWordDb  
