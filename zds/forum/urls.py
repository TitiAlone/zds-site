# coding: utf-8

from django.conf.urls import patterns, url

from . import feeds
from zds.forum.views import CategoriesForumsListView, CategoryForumsDetailView, ForumTopicsListView, TopicPostsListView


urlpatterns = patterns('',

                       # Feeds
                       url(r'^flux/messages/rss/$', feeds.LastPostsFeedRSS(), name='post-feed-rss'),
                       url(r'^flux/messages/atom/$', feeds.LastPostsFeedATOM(), name='post-feed-atom'),
                       
                       url(r'^flux/sujets/rss/$',
                           feeds.LastTopicsFeedRSS(),
                           name='topic-feed-rss'),
                       url(r'^flux/sujets/atom/$',
                           feeds.LastTopicsFeedATOM(),
                           name='topic-feed-atom'),

                       # Developers warning: if you update something here, check and update help_text
                       # on Category slug field

                       # Followed topics
                       url(r'^notifications/$',
                           'zds.forum.views.followed_topics'),

                       # Moderation
                       url(r'^resolution_alerte/$',
                           'zds.forum.views.solve_alert'),

                       # Viewing a thread
                       url(r'^sujet/nouveau/$',
                           'zds.forum.views.new'),
                       url(r'^sujet/editer/$',
                           'zds.forum.views.edit'),
                       url(r'^sujet/deplacer/$',
                           'zds.forum.views.move_topic'),
                       url(r'^sujet/(?P<topic_pk>\d+)/(?P<topic_slug>.+)/$', TopicPostsListView.as_view(), name='topic-posts-list'),
                       url(r'^sujets/membre/(?P<user_pk>\d+)/$',
                           'zds.forum.views.find_topic'),
                       url(r'^sujets/tag/(?P<tag_pk>\d+)/(?P<tag_slug>.+)/$',
                           'zds.forum.views.find_topic_by_tag'),
                       url(r'^sujets/recherche/$',
                           'zds.forum.views.complete_topic'),

                       # Message-related
                       url(r'^message/editer/$',
                           'zds.forum.views.edit_post'),
                       url(r'^message/nouveau/$',
                           'zds.forum.views.answer'),
                       url(r'^message/utile/$',
                           'zds.forum.views.useful_post'),
                       url(r'^message/nonlu/$',
                           'zds.forum.views.unread_post'),
                       url(r'^message/like/$',
                           'zds.forum.views.like_post'),
                       url(r'^message/dislike/$',
                           'zds.forum.views.dislike_post'),
                       url(r'^messages/(?P<user_pk>\d+)/$',
                           'zds.forum.views.find_post'),

                       # Categories and forums list.
                       url(r'^$', CategoriesForumsListView.as_view(), name='cats-forums-list'),

                       # Forum details
                       url(r'^(?P<cat_slug>.+)/(?P<forum_slug>.+)/$', ForumTopicsListView.as_view(), name='forum-topics-list'),

                       # Forums belonging to one category
                       url(r'^(?P<slug>.+)/$',CategoryForumsDetailView.as_view(), name='cat-forums-list'),
                       )
