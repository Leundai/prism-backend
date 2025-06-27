from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class MediaItem(BaseModel):
    id: str | None = None
    type: str | None = None
    url: str | None = None
    display_url: str | None = None
    expanded_url: str | None = None
    dimensions: dict[str, int] | None = None
    alt_text: str | None = None


class Hashtag(BaseModel):
    text: str | None = None
    indices: list[int] | None = None


class Mention(BaseModel):
    id: str | None = None
    username: str | None = None
    name: str | None = None
    indices: list[int] | None = None


class Url(BaseModel):
    url: str | None = None
    expanded_url: str | None = None
    display_url: str | None = None
    indices: list[int] | None = None


class TweetUser(BaseModel):
    id: str | None = None
    username: str | None = None
    display_name: str | None = None
    avatar_url: str | None = None
    followers_count: int | None = None
    following_count: int | None = None
    tweets_count: int | None = None
    likes_count: int | None = None
    listed_count: int | None = None
    is_verified: bool | None = None
    is_protected: bool | None = None
    created_at: str | None = None
    professional_category: str | None = None
    website: str | None = None


class Tweet(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str
    conversation_id: str
    text: str
    created_at: str
    language: str | None = None
    likes: int
    retweets: int
    replies: int
    quotes: int
    bookmarks: int
    views: int
    is_liked: bool | None = None
    is_retweeted: bool | None = None
    is_bookmarked: bool | None = None
    is_quote_tweet: bool
    is_reply: bool
    is_thread: bool
    possibly_sensitive: bool | None = None
    media: list[MediaItem] | None = None
    user: TweetUser | None = None
    quoted_tweet: Tweet | None = None
    hashtags: list[Hashtag]
    mentions: list[Mention]
    urls: list[Url] | None = None
    parsed_at: str
