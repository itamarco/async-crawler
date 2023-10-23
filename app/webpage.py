# import sqlite3

def save_webpage(crawl_id: str, html_text: str):
    filename = f"{crawl_id}.html"
    with open(f"/tmp/webpages/{filename}", "w", encoding="utf-8") as file:
        file.write(html_text)

## SQLITE IMPL
# class WebpageDAO:
#     def __init__(self, db_file):
#         self.db_file = db_file
#
#     def init(self):
#         conn = sqlite3.connect(self.db_file)
#         conn.execute('''
#             CREATE TABLE IF NOT EXISTS webpages (
#                 crawl_id TEXT PRIMARY KEY,
#                 url TEXT,
#                 html TEXT
#             )
#         ''')
#
#         conn.close()
#
#     def get_webpage_by_crawl_id(self, crawl_id):
#         conn = sqlite3.connect(self.db_file)
#         cursor = conn.execute('SELECT * FROM webpages WHERE crawl_id = ?', (crawl_id,))
#         data = cursor.fetchone()
#         conn.close()
#         return data
#
#     def save_webpage(self, crawl_id, url, html):
#         conn = sqlite3.connect(self.db_file)
#         conn.execute('INSERT OR REPLACE INTO webpages VALUES (?, ?, ?)', (crawl_id, url, html))
#         conn.commit()
#         conn.close()
