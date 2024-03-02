import asyncio
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def event_generator():
    for i in range(5):
        yield {"event": "message", "data": f"message {i}"}
        await asyncio.sleep(2)
    yield {"event": "close"}


async def text_streamer():
    text = """The history of the Internet has its origin in the efforts to build and interconnect computer networks that arose from research and development in the United States and involved international collaboration, particularly with researchers in the United Kingdom and France. The English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser in 1990 while employed at CERN near Geneva, Switzerland. The browser was released outside CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991. The World Wide Web enabled the spread of information over the Internet through an easy-to-use and flexible format. It thus played an important role in popularizing use of the Internet. Although the two terms are sometimes conflated in popular use, World Wide Web is not synonymous with the Internet. The Web is an information space consisting of documents and other resources, linked by hyperlinks and URLs. The term "Internet" refers to the global information system that — is logically linked together by a globally unique address space based on the Internet Protocol (IP), is able to support communications using the Transmission Control Protocol/Internet Protocol (TCP/IP) suite or its subsequent extensions, and provides, uses or makes accessible, either publicly or privately, high-level services layered on the communications and related infrastructure. The Internet is also often referred to as the Net. The World Wide Web and the Internet are not the same thing; the World Wide Web is one of many services offered by the Internet. The Web is a collection of interconnected documents (web pages) and other web resources, linked by hyperlinks and URLs. As another point of comparison, Hypertext Transfer Protocol, or HTTP, is the language used on the Web for information transfer, yet it is just one of many languages or protocols that can be used for communication on the Internet. The term Interweb is a portmanteau of Internet and World Wide Web typically used sarcastically to parody a technically unsavvy user."""
    for word in text.split():
        yield {"event": "message", "data": word}
        await asyncio.sleep(0.05)
    yield {"event": "close"}


@app.get("/events")
async def events():
    return EventSourceResponse(text_streamer())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)