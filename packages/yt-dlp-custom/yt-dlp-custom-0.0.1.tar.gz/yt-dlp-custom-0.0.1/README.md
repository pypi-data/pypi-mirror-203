<!-- MANPAGE: BEGIN EXCLUDED SECTION -->
<div align="center">

[![YT-DLP](https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/.github/banner.svg)](#readme)

[[original package]](https://github.com/yt-dlp/yt-dlp)
</div>

## Introduce
This package only modified to get hastags and unique filename as post-id.<br>

* First modified
```python
#yt_dlp/YoutubeDL.py
def _get_filename_as_uniqid(self, info_dict):
  post_id_reg = re.compile('(?<=video\/)[0-9]+')
  post_id = post_id_reg.search(info_dict['webpage_url'])[0]
  filename = f"/tmp/{post_id}.{info_dict['ext']}"
  return filename

def prepare_filename(self, info_dict, dir_type='', *, outtmpl=None, warn=False):
  """Generate the output filename"""
  ...
  ...
  
  filename = self._get_filename_as_uniqid(info_dict)

```

* Second modified
```python
# yt_dlp/extractor/tiktok.py
def _parse_aweme_video_app(self, aweme_detail):
        aweme_id = aweme_detail['aweme_id']
        video_info = aweme_detail['video']
        author_name_info = aweme_detail['author']

        hashtags_info = []
        for hashtag_info in aweme_detail['text_extra']:
            if hashtag_info.get('hashtag_name'):
                hashtags_info.append(hashtag_info['hashtag_name'])

        return {
            ...
            ...
            'author': author_name_info,
            'hashtags_info': hashtags_info
        }
```