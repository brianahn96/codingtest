import bs4
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    web_paths=("https://n.news.naver.com/article/437/0000378416",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            "div",
            attrs={"class": ["newsct_article _article_body", "media_end_head_title"]},
        )
    ),
    header_template={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    },
)

loader = WebBaseLoader(web_paths=("https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%9E%A5%EC%95%A0%EC%9D%B8%EB%B3%B5%EC%A7%80%EB%B2%95",))
docs = loader.load()
print(f"문서의 수: {len(docs)}")
print(docs)