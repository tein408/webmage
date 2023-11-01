from django.urls import path
from . import views_feed

urlpatterns = [
    # Feed related URLs
    path('<int:user_id>/', views_feed.return_feed, name='user_feed'),
    path('<int:user_id>/log/', views_feed.feed_log, name='user_feed_log'),
    path('timeline/<int:user_id>/', views_feed.timeline, name='user_timeline'),
    path('write/', views_feed.write_feed, name='write_feed'),
    path('<int:feed_id>/', views_feed.edit_feed, name='edit_feed'), # Assuming PATCH method is handled in this view.
    path('<int:feed_id>/set_emoji/', views_feed.set_feed_emoji, name='set_feed_emoji'),
    path('<int:feed_id>/comment/', views_feed.add_comment, name='add_comment'),
    path('<int:feed_id>/comment/<int:comment_id>/', views_feed.edit_comment, name='edit_comment'),
]